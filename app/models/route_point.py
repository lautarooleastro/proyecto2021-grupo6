from sqlalchemy import String, Column, Integer, ForeignKey
from app.db import db


class RoutePoint(db.Model):
    __tablename__ = "route_points"
    id = Column(Integer, primary_key=True)
    lat = Column(String(30))
    long = Column(String(30))
    route_id = Column(Integer, ForeignKey('evacuation_routes.id'))

    def __init__(self, lat=None, long=None):
        self.lat = lat
        self.long = long
