# Flask-WTF Forms for user interaction

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    content = TextAreaField('Feedback', validators=[DataRequired()])
    submit = SubmitField('Submit Feedback')