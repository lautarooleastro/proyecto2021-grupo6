from sqlalchemy.sql.sqltypes import String
from wtforms import Form, validators
from wtforms.fields.core import BooleanField, StringField


class EvacuationRouteForm(Form):
    name = StringField(u'Nombre', validators=[validators.input_required(
        message="El nombre no puede estar vacio"), validators.data_required(message="El nombre no puede estar vacio")])
    description = StringField(u'Descripcion', validators=[
                              validators.input_required(message="La descripcion no puede estar vacia"), validators.data_required(message="La descripcion no puede estar vacia")])
    latitude = StringField(u'Latitud', validators=[
                           validators.input_required(), validators.data_required(message="Latitud no puede estar vacia")])
    longitude = StringField(u'Longitud', validators=[
                            validators.input_required(), validators.data_required(message="Longitud no puede estar vacia")])


class EditEvacuationRouteForm(Form):
    name = StringField(u'Nombre', validators=[validators.input_required(
        message="El nombre no puede estar vacio"), validators.data_required(message="El nombre no puede estar vacia")])
    description = StringField(u'Descripcion', validators=[
                              validators.input_required(
                                  message="La descripcion no puede estar vacia"), validators.data_required(message="La descripcion no puede estar vacia")])
