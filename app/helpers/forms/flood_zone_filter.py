
from sqlalchemy import false, true
from sqlalchemy.sql.sqltypes import Integer, String
from wtforms import Form
from wtforms import validators
from wtforms.validators import DataRequired, Length, NoneOf
from wtforms.fields.core import StringField, BooleanField, IntegerField


class NewFilter(Form):
    code = StringField('code', validators=[Length(max=10,message="Máximo 10 caracteres, letras o números"), NoneOf(",+*[]_%&@", message="Caracteres no permitidos: ,+*[]_%&")], default ='')
    status = BooleanField('Publicada',default=True)

    

