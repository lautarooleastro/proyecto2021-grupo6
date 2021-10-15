from sqlalchemy import Column, Integer, String, Table, ForeignKey, Boolean
from sqlalchemy.orm import backref, query, relationship, session
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
    first_name = Column(String(30), unique=True)
    last_name = Column(String(30), unique=True)
    email = Column(String(30), unique=True)
    password = Column(String(30), unique=True)
    active = Column(Boolean)
    roles = relationship('Role', secondary=user_has_role_table,
                         backref=backref('users', lazy=True), lazy=True)

    def __init__(self, first_name=None, last_name=None, email=None, password=None, active=True):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.active = active

    def all():
        return User.query.all()

    def with_email(email):
        return User.query.filter(User.email == email).first()

    def with_id(user_id):
        return User.query.filter(User.id == user_id).first()

    def already_exists(email):
        """ Devuelve True si ya existe un usuario con el mail recibido como parametro. False caso contrario. """
        query = User.with_email(email)
        return (query != None)

    def destroy(user):
        """ Elimina un usuario de la BD. """
        print("se quiere eliminar: {user.id}")
        db.session.delete(user)
        db.session.commit()

    def check_permission(user, permission):
        user_permissions = []
        for role in user.roles:
            for perm in role.permissions:
                user_permissions.append(perm.name)
        return(permission in user_permissions)
