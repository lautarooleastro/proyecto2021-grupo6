from wtforms import Form
from wtforms.validators import DataRequired, Length
from wtforms.fields.core import StringField, BooleanField
from wtforms.fields import FileField 

class FloodZoneFile(Form):
    zones_import = FileField('Zonas:', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired(), Length(max=7)])
    status = BooleanField('Publicar', default=False)