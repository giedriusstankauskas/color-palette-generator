from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    image_url = StringField('Enter image link', validators=[DataRequired()])
    submit = SubmitField('Submit')
