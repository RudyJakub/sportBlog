import email
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired         

class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Post')
