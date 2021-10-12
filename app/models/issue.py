from sqlalchemy.sql.annotation import EMPTY_ANNOTATIONS
from sqlalchemy.sql.schema import ForeignKey
from app.db import db
from app.models.category import Category
from app.models.status import Status

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Issue(db.Model):
    """ Define una entidad Issue que se corresponde con la tabla issues de la BD. """

    __tablename__ = "issues"
    id = Column(Integer, primary_key=True)
    email = Column(String(30), unique=True)
    description = Column(String(30), unique=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship(Category)
    status_id = Column(Integer, ForeignKey("statuses.id"))
    status = relationship(Status)

    def __init__(self, email=None, description=None, status_id=None, category_id=None):
        self.email = email
        self.description = description
        self.status_id = status_id
        self.category_id = category_id
