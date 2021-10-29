from sqlalchemy import Column, Integer, String, Boolean
from app.db import db


class MeetingPoint(db.Model):
    __tablename__ = "meeting_points"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    adress = Column(String(30))
    coordinates = Column(String(30))
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
