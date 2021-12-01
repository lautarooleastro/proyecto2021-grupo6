from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db import db
from app.models.route_point import RoutePoint


class EvacuationRoute(db.Model):
    __tablename__ = "evacuation_routes"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    description = Column(String(255))
    status = Column(Boolean)
    points = relationship("RoutePoint", cascade="all, delete")

    def __init__(self, name=None, description=None, status=True):
        self.name = name
        self.description = description
        self.status = status

    @staticmethod
    def all():
        return EvacuationRoute.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_published():
        return EvacuationRoute.query.filter(EvacuationRoute.status == True)

    @staticmethod
    def with_id(id):
        return EvacuationRoute.query.filter(EvacuationRoute.id == id).first()

    def destroy(self):
        db.session.delete(self)
        db.session.commit()

    def as_dict(self):
        ret = {}
        for attr in self.__table__.columns:
            ret[attr.name] = getattr(self, attr.name)
        points = []
        for point in self.points:
            points.append(point.as_list())
        ret['points'] = points
        return ret
