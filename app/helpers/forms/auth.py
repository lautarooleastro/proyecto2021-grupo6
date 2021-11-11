from wtforms import Form, validators
from wtforms.fields.core import BooleanField, StringField


class SignInForm(Form):
    email = StringField(u'E-Mail', validators=[
                        validators.input_required(message="Olvido ingresar el email"), validators.Email("Formato de email invalido")])
    password = StringField(u'Contraseña', validators=[
                           validators.input_required(message="Olvido ingresar la contraseña"), validators.Length(min=6, max=32, message="La contraseña tiene entre 6 y 32 caracteres")])
