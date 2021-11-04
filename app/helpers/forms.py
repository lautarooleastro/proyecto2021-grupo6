from wtforms import Form, validators
from wtforms.fields.core import BooleanField, StringField


class SignupForm(Form):
    first_name = StringField(u'Nombre', validators=[
                             validators.input_required()])
    last_name = StringField(u'Apellido', validators=[
                            validators.input_required()])
    email = StringField(u'E-Mail', validators=[
                        validators.input_required()])
    password = StringField(u'Contraseña', validators=[
                           validators.input_required(), validators.Length(min=6, max=24)])


class NewPointForm(Form):
    name = StringField(u'Nombre', validators=[validators.input_required()])
    adress = StringField(u'Direccion', validators=[
                         validators.input_required()])
    coordinates = StringField(u'Coordenadas', validators=[
                              validators.input_required()])
    status = BooleanField(u'Estado', validators=[validators.input_required()])
    phone = StringField(u'Telefono', validators=[validators.input_required()])
    email = StringField(u'E-mail', validators=[validators.input_required()])

    # def validate_coordinates():
    #    return True
