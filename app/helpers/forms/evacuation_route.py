from sqlalchemy.sql.sqltypes import String
from wtforms import Form, validators
from wtforms.fields.core import BooleanField, StringField


class EvacuationRouteForm(Form):
    name = StringField(u'Nombre', validators=[validators.input_required(
        message="El nombre no puede estar vacio")])
    description = StringField(u'Descripcion', validators=[
                              validators.input_required(message="La descripcion no puede estar vacia")])
    latitude = StringField(u'Latitud', validators=[
                           validators.input_required()])
    longitude = StringField(u'Longitud', validators=[
                            validators.input_required()])


class EditEvacuationRouteForm(Form):
    name = StringField(u'Nombre', validators=[validators.input_required(
        message="El nombre no puede estar vacio")])
    description = StringField(u'Descripcion', validators=[
                              validators.input_required(message="La descripcion no puede estar vacia")])
