from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from app.db import db


class Colour(db.Model):
    __tablename__ = "colors"
    id = Column(Integer, primary_key=True)
    rgb = Column(String(6))
    configuration_id = Column(Integer, ForeignKey("configuration.id"))


class Configuration(db.Model):
    __tablename__ = "configuration"
    id = Column(Integer, primary_key=True)
    elements_per_page = Column(Integer)
    order = Column(String(10))

    @staticmethod
    def get():
        return Configuration.query.all()[0]

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def per_page():
        return Configuration.get().elements_per_page
