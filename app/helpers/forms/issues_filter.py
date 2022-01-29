
from sqlalchemy import false, true
from sqlalchemy.sql.sqltypes import Integer, String
from wtforms import Form
from wtforms import validators
from wtforms.validators import DataRequired, Length, NoneOf
from wtforms.fields.core import StringField, RadioField, SelectField
from app.models.status import Status
from app.models.category import Category


class IssuesFilter(Form):
    tittle = StringField(u'Titulo', validators=[Length(max=40,message="Máximo 40 caracteres, letras o números"), NoneOf(",+*[]_%&@", message="Caracteres no permitidos: ,+*[]_%&")], default ='')
    status = SelectField(u'Estado', choices= [('In Progress','3'),('New','1'),('Todo','2')])
    category = SelectField(u'Categoria', choices= [('Bug','1'),('Question','2')])

@staticmethod
def statuses():
    ret=[]
    for status in Status.get_all():
        ret.append([str(status.name),str(status.id)])
    return ret

@staticmethod
def categories():
    ret=[]
    for category in Category.get_all():
        ret.append([str(category.name),str(category.id)])
    return ret
