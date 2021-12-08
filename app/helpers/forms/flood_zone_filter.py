
from sqlalchemy.sql.sqltypes import String
from wtforms import Form
from wtforms.validators import DataRequired, Length
from wtforms.fields.core import StringField, BooleanField


class NewFilter(Form):
    code = StringField('', validators=[Length(max=10)])
    status = BooleanField('Publicada', default=False)

    

