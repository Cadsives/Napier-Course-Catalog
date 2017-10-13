from flask_wtf import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms import FileField
from wtforms.validators import DataRequired

class LocationPageForm(Form):
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    image = FileField('image', validators=[DataRequired()])
    image_alt = StringField('image_alt', validators=[DataRequired()])
    lat = StringField('lat', validators=[DataRequired()])
    lon = StringField('lon', validators=[DataRequired()])


class CoursePageForm(Form):
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    price = IntegerField('price', validators=[DataRequired()])


