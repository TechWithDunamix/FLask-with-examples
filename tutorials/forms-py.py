from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField('Todo', validators=[DataRequired()])
    submit = SubmitField('Add Todo')
