from flask_wtf import FlaskForm
from wtforms import TextField,BooleanField,PasswordField,StringField
from wtforms.validators import DataRequired

class Login(FlaskForm):
    name=TextField('Name',validators=[DataRequired()])
    name=StringField('Name',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    remenber_me=BooleanField('Remenber me',default=False)