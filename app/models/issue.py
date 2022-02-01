from datetime import datetime
from app.db import db
from sqlalchemy import Column, Integer, String, Date, Text, true, ForeignKey, desc
from app.models.category import Category
from app.models.status import Status
from app.models.issue_comment import IssueComment
from app.models.configuration import Configuration
from sqlalchemy.orm import relationship, backref


class Issue(db.Model):
    __tablename__ = "issues"
    id = Column(Integer, primary_key=True)
    tittle = Column(String(50))
    date_open=Column(Date)
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
    category = relationship(Category, backref=backref('issues', uselist=True))
    status_id = Column(Integer, ForeignKey("statuses.id"))
    status = relationship(Status, backref=backref('issues', uselist=True))
    issue_comment = relationship("IssueComment", cascade="all, delete") 


    def __init__(self, email=None, tittle=None, description=None, status_id=None, category_id=None, first_name=None, last_name=None, latitude=None, longitude=None, phone=None):
        self.tittle = tittle
        self.email = email
        self.description = description
        self.status_id = status_id
        self.category_id = category_id
        self.date_open = datetime.now().date()
        self.latitude = latitude
        self.longitude = longitude
        self.last_name = last_name
        self.first_name = first_name
        self.phone = phone

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
    def all_paginate(pos=1):
        return Issue.query.paginate(page=int(pos), per_page=Configuration.per_page())

    @staticmethod
    def filter_date(pos=1, origin=None, top=None):
        if (origin!=None):
            origin=Date(origin)
            if not top != None:
                top=datetime.date()
            consulta= Issue.query.filter(Issue.date_open.between(origin,top))
        else:
            consulta= Issue.query.order_by(desc(Issue.date_open))
        return consulta.paginate(page=int(pos), per_page=Configuration.per_page())
