from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SearchField,SelectField
from wtforms.validators import DataRequired,input_required,email_validator
from wtforms.widgets import TextArea

class SearchForm(FlaskForm):
    search = StringField("search", validators=[DataRequired()])
    submit = SubmitField("submit")