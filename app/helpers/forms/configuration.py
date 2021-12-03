from wtforms import Form, validators
from wtforms.fields.core import IntegerField, StringField


class ConfigurationForm(Form):
    elements_per_page = IntegerField(u"Elementos por pagina", validators=[
                                     validators.input_required(message="Debe ingresar un numero"), validators.data_required(message="Ingrese un numero valido"), validators.number_range(min=1, max=25, message="Ingrese un numero entre 1 y 25")])
    order = StringField(u"Orden", validators=[validators.data_required(
        message="Debe seleccionar un orden por defecto"), validators.any_of(['ASC', 'DESC'])])
