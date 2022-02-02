from sqlalchemy import Column, Integer, String
from app.db import db


class Status(db.Model):
    """ Define una entidad Status que se corresponde con la tabla statuses de la BD. """

    __tablename__ = "statuses"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)

  
    def __init__(self, name=None):
        self.name = name

    @staticmethod
    def get_all():
        return Status.query.all()    

    @staticmethod
    def with_id(id):
        return Status.query.filter(Status.id == id).first()
    
    @staticmethod
    def with_name(name):
        return Status.query.filter(Status.name == name).first()