
from sqlalchemy.sql.sqltypes import String
from wtforms import Form
from wtforms.validators import DataRequired, Length
from wtforms.fields.core import StringField, BooleanField
from app.models.flood_zone import FloodZone


class NewFloodZoneForm(Form):
    name = StringField('Nombre', validators=[DataRequired()])
    code = StringField('Código', validators=[DataRequired(), Length(max=10), Length(min=6)])
    color = StringField('Color', validators=[DataRequired(), Length(max=7)])
    status = BooleanField('Publicar')

    

