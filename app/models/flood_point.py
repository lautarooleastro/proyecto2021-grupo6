from sqlalchemy import Column, Integer, String, Table, ForeignKey, Boolean
from app.db import db
from sqlalchemy.orm import backref, query, relationship, session
from app.models.flood_zone import FloodZone 


class FloodPoint(db.Model):
    __tablename__ = 'flood_points'
    id = Column(Integer, primary_key=True)
    latitude = Column(String(25))
    longitude = Column(String(25))
    flood_zone_id = Column(Integer, ForeignKey('flood_zones.id'))
    flood_zone = relationship('FloodZone', 
                                backref=backref('flood_points', 
                                uselist=True,
                                cascade='delete,all'))
    

    def __init__(self, latitude=None, longitude=None, flood_zone_id=None):
        self.latitude = latitude
        self.longitude = longitude
        self.flood_zone_id = flood_zone_id

    def get_all():
        return FloodPoint.query.all()

    def destroy(point):
        """ Elimina un punto de la BD. """
        db.session.delete(point)
        db.session.commit() 

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self