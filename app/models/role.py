from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import backref, relationship
from app.db import db
from app.models.permission import Permission

role_has_permission_table = Table('role_has_permission', db.metadata,
                                  Column('role_id', Integer,
                                         ForeignKey('roles.id')),
                                  Column('permission_id', Integer,
                                         ForeignKey('permissions.id')),
                                  )


class Role(db.Model):
    """ Define una entidas Role que se corresponde con la tabla roles de la BD. """

    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)

    permissions = relationship('Permission', secondary=role_has_permission_table,
                               backref=backref('roles', lazy=True), lazy=True)

    def __init__(self, name=None):
        self.name = name
