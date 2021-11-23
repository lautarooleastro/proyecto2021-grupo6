from wtforms import Form, validators
from wtforms.fields.core import IntegerField


class ConfigurationForm(Form):
    elements_per_page = IntegerField(u"Elementos por pagina", validators=[
                                     validators.input_required(message="Debe ingresar un numero"), validators.data_required(message="Ingrese un numero valido"), validators.number_range(min=1, max=25, message="Ingrese un numero entre 1 y 25")])
