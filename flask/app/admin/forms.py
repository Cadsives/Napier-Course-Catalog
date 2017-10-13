from flask_wtf import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired

class LocationPageForm(Form):
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])

class CoursePageForm(Form):
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    price = IntegerField('price', validators=[DataRequired()])
