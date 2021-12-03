from sqlalchemy import Column, Integer, String, Boolean, desc
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

    @staticmethod
    def all_paginated(page, name_query, config):
        if not name_query:
            name_query = ''
        if config.order == 'ASC':
            query = EvacuationRoute.query.filter(EvacuationRoute.name.like('%'+name_query+'%')).paginate(
                page=page, per_page=config.elements_per_page)
        else:
            query = EvacuationRoute.query.filter(EvacuationRoute.name.like('%'+name_query+'%')).order_by(desc(EvacuationRoute.id)).paginate(
                page=page, per_page=config.elements_per_page)
        return query

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_published():
        return EvacuationRoute.query.filter(EvacuationRoute.status == True)

    @ staticmethod
    def with_id(id):
        return EvacuationRoute.query.filter(EvacuationRoute.id == id).first()

    def destroy(self):
        db.session.delete(self)
        db.session.commit()
