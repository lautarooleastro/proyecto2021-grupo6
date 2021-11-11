from wtforms import Form, validators
from wtforms.fields.core import StringField


class UserForm(Form):
    first_name = StringField(u'Nombre', validators=[
                             validators.input_required()])
    last_name = StringField(u'Nombre', validators=[
                            validators.input_required()])
    email = StringField(u'Nombre', validators=[
                        validators.input_required(), validators.Email()])
    password = StringField(u'Contraseña', validators=[
                           validators.input_required(), validators.EqualTo('confirm_password', message='Las contraseñas no coinciden.'), validators.Length(min=6, max=32, message='La contraseña debe tener entre 6 y 32 caracteres.')])
    confirm_password = StringField('Confirmar contraseña', validators=[
                                   validators.input_required()])
