from sqlalchemy import Column, Integer, String, Table, Boolean
from app.db import db


class EvacuationRoute(db.Model):
    __tablename__ = "evacuation_routes"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    description = Column(String(255))
    points = Column(String(255))
    status = Column(Boolean)

    def __init__(self, name=None, description=None, points=None, status=True):
        self.name = name
        self.description = description
        self.points = points
        self.status = status

    def all():
        return EvacuationRoute.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_published():
        return EvacuationRoute.query.filter(EvacuationRoute.status == True)
