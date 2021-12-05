from sqlalchemy import Column, Integer, String, Table, ForeignKey, Boolean
from app.db import db
from sqlalchemy.orm import query, relationship, session
from app.models.flood_point import FloodPoint 


class FloodZone(db.Model):
    __tablename__ = "flood_zones"
    id = Column(Integer, primary_key=True)  
    name = Column(String(40), unique=True)  # nombre de la zona inundable
    code = Column(String(10), unique=True)  # código de la zona inundable
    status = Column(Boolean)    # Publicado o no
    color = Column(String(6))   # Color RGB
    flood_points = relationship("FloodPoint", cascade="all, delete") 

    
    def __init__(self, name=None, code=None, status=False, color=None):
        self.name = name
        self.code = code
        self.status = status
        self.color = color

    @staticmethod
    def get_all():
        return FloodZone.query.all()

    @staticmethod
    def with_name(name):
        return FloodZone.query.filter(FloodZone.name == name).first()

    @staticmethod
    def with_code(code):
        return FloodZone.query.filter(FloodZone.code == code).first()
    
    @staticmethod
    def with_id(id):
        return FloodZone.query.filter(FloodZone.id == id).first()
    
    @staticmethod
    def destroy(zone):
        """ Elimina una zona de la BD. """
        db.session.delete(zone)
        db.session.commit()  
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def modify(self):
        db.session.commit()
        return self

    @staticmethod
    def n_with_name(name):
        return FloodZone.query.filter(FloodZone.name == name).count()

    @staticmethod
    def n_with_code(code):
        return FloodZone.query.filter(FloodZone.code == code).count()
    