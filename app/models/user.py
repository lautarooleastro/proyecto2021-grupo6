import this
from sqlalchemy import Column, Integer, String, Table, ForeignKey, Boolean, desc
from sqlalchemy.orm import backref, query, relationship, session
from flask_login import current_user
from sqlalchemy.sql.functions import user
from app.db import db
from app.models.role import Role


user_has_role_table = Table('user_has_role', db.metadata,
                            Column('user_id', Integer,
                                   ForeignKey('users.id')),
                            Column('role_id', Integer,
                                   ForeignKey('roles.id'))
                            )


class User(db.Model):
    """ Define una entidad User que se corresponde con la tabla users de la BD. """

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(30), unique=True)
    username = Column(String(30), unique=True)
    password = Column(String(30))
    active = Column(Boolean)
    roles = relationship('Role', secondary=user_has_role_table,
                         backref=backref('users', lazy=True), lazy=True)

    def __init__(self, first_name=None, last_name=None, email=None, password=None, active=True):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.active = active

    @staticmethod
    def all_paginated(page, name_query, status_query, config):
        if not name_query:
            name_query = ''

        query = User.query.filter(
            User.username != current_user.username, User.username.like('%'+name_query+'%'))

        if status_query == 'active':
            query = query.filter(User.active == True)
        elif status_query == 'inactive':
            query = query.filter(User.active == False)

        if config.order == 'DESC':
            query = query.order_by(desc(User.id))

        query = query.paginate(
            page=page, per_page=config.elements_per_page)
        return query

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def with_email(email):
        return User.query.filter(User.email == email).first()

    @staticmethod
    def with_username(username):
        return User.query.filter(User.username == username).first()

    @staticmethod
    def with_id(user_id):
        return User.query.filter(User.id == user_id).first()

    @staticmethod
    def already_exists(user):
        """ 
            Devuelve diccionario con:
            - resultado de encontrar un usuario con ese nombre y mail.
            - errores en caso de encontrarlos. 
        """
        ret = {
            'exists': False,
            'errors': []
        }
        if (User.with_email(user.email) != None):
            ret['exists'] = True
            ret['errors'].append(
                "Ya existe un usuario con mail: " + user.email)
        if (User.with_username(user.username) != None):
            ret['exists'] = True
            ret['errors'].append(
                "Ya existe un usuario con nombre de usuario: " + user.username)
        return ret

    def destroy(user):
        """ Elimina un usuario de la BD. """
        db.session.delete(user)
        db.session.commit()

    def check_permission(user, permission):
        user_permissions = []
        for role in user.roles:
            for perm in role.permissions:
                user_permissions.append(perm.name)
        return(permission in user_permissions)

    def update(user_id, data):
        """ 
            Recibe un id de User y un diccionario. 
            Busca el usuario por id y edita los valores que hay en el diccionario. 
            Luego inserta el usuario con los cambios en la bd. 
            Retorna el usuario con los cambios hechos.
        """
        # TODO:
        # - juntar con el metodo update_profile()
        # - agregar validaciones

        roles = []
        for role_name in data.keys():
            if data[role_name] == 'role':
                roles.append(Role.with_name(role_name))

        user = User.with_id(user_id)
        user.email = data['email']
        user.password = data['password']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.roles = roles
        db.session.commit()
        return user

    def update_profile(data):
        """ Actualiza mail, contrase??a, nombre y apellido del usuario actual. """
        # TODO:
        # - juntar con el metodo update()
        # - agregar validaciones

        current_user.email = data['email']
        current_user.password = data['password']
        current_user.first_name = data['first_name']
        current_user.last_name = data['last_name']
        db.session.commit()

    def toggle(user):
        user.active = not user.active
        db.session.commit()
        return user.active

    @property
    def is_active(self):
        return self.active

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def hasRole(self, role_name):
        role = Role.with_name(role_name)
        return (role in self.roles)

    @staticmethod
    def get_all():
        return User.query.all() 