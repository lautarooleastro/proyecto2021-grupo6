
from wtforms import Form, SubmitField
from wtforms.validators import DataRequired, Length, NoneOf, Optional
from wtforms.fields.core import StringField, RadioField, SelectField
from wtforms.fields import DateField
from datetime import date



class IssuesFilter(Form):
    tittle = StringField(u'Titulo', validators=[Optional(), Length(max=40,message="Máximo 40 caracteres, letras o números"), NoneOf(",+*[]_%&@", message="Caracteres no permitidos: ,+*[]_%&")], default ='')
    status = SelectField(u'Estado', choices= [('0','All'),('3','In Progress'),('1','New'),('2','Closed')], default='0')
    category = SelectField(u'Categoria', choices= [('0','All'),('1','Bug'),('2','Question')], default='0')
    date_1= DateField(u'Desde',default=date.today)
    date_2= DateField(u'Hasta',default=date.today)
    submit = SubmitField('Filtrar')

    def validate_on_submit(self):
            result = super(Form, self).validate()
            if (self.date_1.data>self.date_2.data):
                return False
            else:
                return result

