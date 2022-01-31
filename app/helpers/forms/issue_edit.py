
from wtforms import Form, validators, SubmitField
from wtforms.validators import DataRequired, Length, NoneOf, NumberRange, Email
from wtforms.fields import FormField, TextAreaField, DateField
from wtforms.fields.core import StringField, SelectField, IntegerField, FormField
from wtforms.fields.html5 import EmailField



class IssueEdit(Form):
    tittle = StringField(u'Titulo', validators=[DataRequired(), Length(max=50,message="Máximo 40 caracteres")])
    category = SelectField(u'Categoria', choices= [('1','Error'),('2','Pregunta')], validators=[DataRequired()])
    description =TextAreaField(u'Descripción', validators=[DataRequired()])
    status = SelectField(u'Estado', choices= [('0','All'),('3','In Progress'),('1','New'),('2','Closed')],validators=[DataRequired()])
    first_name = StringField(u'Nombre', validators=[DataRequired(), Length(max=40,message="Máximo 40 caracteres")])
    last_name = StringField(u'Apellido', validators=[DataRequired(), Length(max=40,message="Máximo 40 caracteres")])
    email = EmailField(u'Correo electrónico', validators=[DataRequired(), Email(), Length(min=6,max=40,message="6 a 40 caracteres")])
    phone = IntegerField('Teléfono de contacto', validators=[NumberRange(min=0, max=99999999999999999999999)])
    latitude = StringField(u'Latitud', validators=[DataRequired(), Length(max=25)])
    longitude = StringField(u'Longitud', validators=[DataRequired(), Length(max=25)])
    date_open= DateField(u'Fecha apertura', validators=[DataRequired()])
    date_closed= DateField(u'Fecha cierre')    
    operator = IntegerField('Operador', validators=[NumberRange(min=0)])
    submit = SubmitField('Editar')