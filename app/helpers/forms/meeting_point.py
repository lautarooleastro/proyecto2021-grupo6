from wtforms import Form, validators
from wtforms.fields.core import BooleanField, StringField


class PointForm(Form):
    name = StringField(u'Nombre', validators=[
                       validators.input_required(),
                       validators.length(max=30, message="El nombre no puede tener mas de 30 caracteres.")])
    adress = StringField(u'Direccion', validators=[
                         validators.input_required(),
                         validators.length(max=30, message="La dirección no puede tener mas de 30 caracteres.")])
    lat = StringField(u'Latitud', validators=[
        validators.input_required()])
    lng = StringField(u'Longitud', validators=[
        validators.input_required()])
    status = BooleanField(u'Estado')
    phone = StringField(u'Telefono', validators=[validators.input_required(),
                                                 validators.length(max=30, message="El teléfono no puede tener mas de 30 caracteres.")])
    email = StringField(u'E-mail', validators=[validators.input_required(),
                                               validators.length(max=30, message="El mail no puede tener mas de 30 caracteres.")])

    # def validate_coordinates():
    #    return True
