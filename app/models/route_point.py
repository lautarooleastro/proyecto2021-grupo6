from sqlalchemy import String, Column, Integer, ForeignKey
from app.db import db


class RoutePoint(db.Model):
    __tablename__ = "route_points"
    id = Column(Integer, primary_key=True)
    lat = Column(String(30))
    lng = Column(String(30))
    route_id = Column(Integer, ForeignKey('evacuation_routes.id'))

    def __init__(self, lat=None, lng=None):
        self.lat = lat
        self.lng = lng

    def toJSONstringify(self):
        return '{"lat":'+self.lat+',"lng":'+self.lng+'}'

    def as_list(self):
        return [self.lat, self.lng]
