from wtforms import Form
from wtforms.validators import DataRequired, Length
from wtforms.fields.core import StringField, BooleanField
from wtforms.fields import FileField 

class FloodZoneFile(Form):
    zones_import = FileField('Zonas:', validators=[DataRequired( message="Campo requerido")])
    color = StringField('Color', validators=[DataRequired( message= "Campor requerido"), Length(max=7, message="No puede tener mas de 7 caracteres (#RRGGBB)")])
    status = BooleanField('Publicar', default=False)