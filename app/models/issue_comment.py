from datetime import datetime
from sqlalchemy.sql.annotation import EMPTY_ANNOTATIONS
from sqlalchemy.sql.schema import ForeignKey
from app.db import db
from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey


class IssueComment(db.Model):
    """ Define una entidad IssueComment, que representa los comentarios de seguimiento de una denuncia """

    __tablename__ = "issue_comments"
    id = Column(Integer, primary_key=True)
    issue_id = Column(Integer, ForeignKey("issues.id"))
    author_id = Column(Integer, ForeignKey('users.id'))
    date=Column(Date, index=True)
    description = Column(Text)

    def __init__(self, description=None, author_id=None, issue_id=None):
        self.author_id = author_id
        self.issue_id = issue_id
        self.description = description
        self.date = datetime.date()

    @staticmethod
    def get_all():
        """Retorna todos los comentarios"""
        return IssueComment.query.all()        

    @staticmethod
    def with_author_id(author_id):
        """Retorna los comentarios realizados por el autor de #id pasado por parámetro"""
        return IssueComment.query.filter(IssueComment.author_id == author_id)

    @staticmethod
    def with_issue(issue_id):
        """Retorna los comentarios sobre la issue del #id pasado por parámetro"""
        return IssueComment.query.filter(IssueComment.issue_id == issue_id)
    
    @staticmethod
    def with_id(id):
        return IssueComment.query.filter(IssueComment.id == id).first()
    
    @staticmethod
    def destroy(issue):
        """ Elimina un comentario de la BD. """
        db.session.delete(issue)
        db.session.commit()  
        
    def save(self):
        """Salva un nuevo comentario en la BD"""
        db.session.add(self)
        db.session.commit()
        return self
    
    def modify(self):
        """Modifica un comentario en la BD"""
        db.session.commit()
        return self