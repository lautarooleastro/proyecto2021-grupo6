from sqlalchemy.sql.schema import Table
from app.db import db
from sqlalchemy import Column, Integer, String, ForeignKey

role_has_permission_table = Table('role_has_permission', db.metadata,
                                  Column('role_id', Integer,
                                         ForeignKey('roles.id')),
                                  Column('permission_id', Integer,
                                         ForeignKey('permissions.id')),
                                  )


class Permission(db.Model):
    """ Define una entidad que se corresponde con la tabla permissions de la BD. """
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    description = Column(String(120))

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description
