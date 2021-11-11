from wtforms import Form, validators
from wtforms.fields.core import BooleanField, StringField


class EvacuationRouteForm(Form):
    name = StringField(u'Nombre', validators=[validators.input_required(
        message="El nombre no puede estar vacio")])
    description = StringField(u'Descripcion', validators=[
                              validators.input_required(message="La descripcion no puede estar vacia")])
    points = StringField(u'Puntos', validators=[validators.input_required(
        message="Tiene que ingresar coordenadas de los puntos del recorrido")])
    status = BooleanField(u'Estado', validators=[validators.optional()])
