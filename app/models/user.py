from sqlalchemy import Column, Integer, String, Table, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship
from app.db import db
from app.models.role import Role

user_has_role_table = Table('user_has_role', db.metadata,
                            Column('user_id', Integer,
                                   ForeignKey('users.id')),
                            Column('role_id', Integer,
                                   ForeignKey('roles.id')),
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

    def __init__(self, first_name=None, last_name=None, email=None, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
