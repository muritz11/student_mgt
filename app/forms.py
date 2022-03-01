from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class NewStudentForm(FlaskForm):
    # name = StringField('name', validators=[DataRequired(), length(min=4, max=10)])
    name = StringField('name', validators=[DataRequired()])
    address = StringField('addreess', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    pincode = IntegerField('pincode', validators=[DataRequired(), NumberRange(min=1000, max=900)])
    send = SubmitField('send')

