from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import backref, relationship
from app.db import db


class Role(db.Model):
    """ Define una entidas Role que se corresponde con la tabla roles de la BD. """

    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)

    def __init__(self, name=None):
        self.name = name
