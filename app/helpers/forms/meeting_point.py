from wtforms import Form, validators
from wtforms.fields.core import BooleanField, StringField


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
