from sqlalchemy import Column, Integer, String, Boolean, desc
from app.db import db
from app.models.evacuation_route import EvacuationRoute


class MeetingPoint(db.Model):
    __tablename__ = "meeting_points"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    adress = Column(String(30))
    lat = Column(String(30))
    lng = Column(String(30))
    status = Column(Boolean)
    phone = Column(String(30))
    email = Column(String(30))

    def __init__(self, name=None, adress=None, coordinates=None, status=False, phone=None, email=None):
        self.name = name
        self.adress = adress
        self.coordinates = coordinates
        self.status = status
        self.phone = phone
        self.email = email

    @staticmethod
    def all_paginated(page, name_query, status_query, config):
        if not name_query:
            name_query = ''

        query = MeetingPoint.query.filter(MeetingPoint.name.like(
            '%'+name_query+'%'))

        if status_query == 'active':
            query = query.filter(MeetingPoint.status == True)
        elif status_query == 'inactive':
            query = query.filter(MeetingPoint.status == False)

        if config.order == 'DESC':
            query = query.order_by(desc(MeetingPoint.id))

        query = query.paginate(page=page,  per_page=config.elements_per_page)
        return query

    def with_id(id):
        return MeetingPoint.query.filter(MeetingPoint.id == id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def destroy(self):
        db.session.delete(self)
        db.session.commit()
