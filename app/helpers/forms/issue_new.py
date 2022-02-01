
from wtforms import Form, SubmitField
from wtforms.validators import DataRequired, Length, NoneOf, NumberRange, Email, Optional
from wtforms.fields import TextAreaField
from wtforms.fields.core import StringField, SelectField, IntegerField
from wtforms.fields.html5 import EmailField

class IssueNew(Form):
    tittle = StringField(u'Titulo', validators=[DataRequired(), Length(max=50,message="Máximo 40 caracteres"), NoneOf(",+*[]_%&@", message="Caracteres no permitidos: ,+*[]_%&")], default ='')
    category = SelectField(u'Categoria', validators=[DataRequired()])
    description =TextAreaField(u'Descripción', validators=[DataRequired()], default ='')
    first_name = StringField(u'Nombre', validators=[DataRequired(), Length(max=40,message="Máximo 40 caracteres")], default ='')
    last_name = StringField(u'Apellido', validators=[DataRequired(), Length(max=40,message="Máximo 40 caracteres")], default ='')
    email = EmailField(u'Correo electrónico', validators=[DataRequired(), Email(), Length(min=6,max=40,message="6 a 40 caracteres")], default ='')
    phone = IntegerField('Teléfono de contacto', validators=[NumberRange(min=0, max=99999999999999999999999), Optional()])
    latitude = StringField(u'Latitud', validators=[DataRequired(), Length(max=25)])
    longitude = StringField(u'Longitud', validators=[DataRequired(), Length(max=25)])
    submit = SubmitField('Registrar')