from wtforms import Form, validators
from wtforms.fields.core import StringField


class SignupForm(Form):
    first_name = StringField(u'Nombre', validators=[
                             validators.input_required()])
    last_name = StringField(u'Apellido', validators=[
                            validators.input_required()])
    email = StringField(u'E-Mail', validators=[
                        validators.input_required, validators.email])
    password = StringField(u'Contraseña', validators=[
                           validators.input_required, validators.Length(min=6, max=24)])
