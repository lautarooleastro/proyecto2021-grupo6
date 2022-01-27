from datetime import datetime
from sqlalchemy.sql.annotation import EMPTY_ANNOTATIONS
from sqlalchemy.sql.schema import ForeignKey
from app.db import db
from sqlalchemy import Column, Integer, String, Date, Text, true, ForeignKey
from app.models.category import Category
from app.models.status import Status
from app.models.issue_comment import IssueComment
from sqlalchemy.orm import relationship


class Issue(db.Model):
    """ Define una entidad Issue que se corresponde con la tabla issues de la BD. """

    __tablename__ = "issues"
    id = Column(Integer, primary_key=True)
    tittle = Column(String(50))
    date_open=Column(Date, index=True)
    date_closed=Column(Date)
    description = Column(Text)
    latitude = Column(String(25))
    longitude = Column(String(25))
    operator = Column(Integer, ForeignKey('users.id'))
    last_name = Column(String(40))
    first_name = Column(String(40))
    email = Column(String(40))
    phone = Column(String(25))
    category_id = Column(Integer, ForeignKey("categories.id"))
    """category = relationship(Category)"""
    status_id = Column(Integer, ForeignKey("statuses.id"))
    """status = relationship(Status)"""
    issue_comment = relationship("IssueComment", cascade="all, delete") 


    def __init__(self, email=None, tittle=None, description=None, status_id=None, category_id=None, first_name=None, last_name=None, latitude=None, longitude=None, operator_id=None):
        self.tittle = tittle
        self.email = email
        self.description = description
        self.status_id = status_id
        self.category_id = category_id
        self.date_open = datetime.date()
        self.latitude = latitude
        self.longitude = longitude
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def get_all():
        return Issue.query.all()        

    @staticmethod
    def with_operator(operator):
        return Issue.query.filter(Issue.operator == operator)

    @staticmethod
    def with_email(email):
        return Issue.query.filter(Issue.email == email)

    @staticmethod
    def with_status(status):
        return Issue.query.filter(Issue.status_id == status)

    @staticmethod
    def with_category(category):
        return Issue.query.filter(Issue.category_id == category)
    
    @staticmethod
    def with_id(id):
        return Issue.query.filter(Issue.id == id).first()
    
    @staticmethod
    def destroy(issue):
        """ Elimina una denuncia de la BD. """
        db.session.delete(issue)
        db.session.commit()  
        
    def save(self):
        """Salva una nueva denuncia en la BD"""
        db.session.add(self)
        db.session.commit()
        return self
    
    def modify(self):
        """Modifica una denuncia en la BD"""
        db.session.commit()
        return self

    @staticmethod
    def n_with_operator(operator):
        return Issue.query.filter(Issue.operator == operator).count()

    @staticmethod
    def n_with_email(email):
        return Issue.query.filter(Issue.email == email).count()
    
    @staticmethod
    def filter_date(origin=None, top=None):
        if (origin!=None):
            origin=Date(origin)
            if not top != None:
                top=datetime.date()
            return Issue.query.filter(Issue.date_open.between(origin,top))
        return None

   