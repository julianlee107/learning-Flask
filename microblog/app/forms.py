from flask_wtf import FlaskForm
from wtforms import TextField,BooleanField,PasswordField,StringField,SubmitField
from wtforms.validators import DataRequired,Email,Length

class LoginForm(FlaskForm):
    user_name = StringField('user_name', validators=[
        DataRequired(), Length(max=128)])
    remember_me = BooleanField('remember me', default=False)
    submit = SubmitField('Log in')

class SignUpForm(FlaskForm):
    user_name = StringField('user_name', validators=[
       DataRequired(), Length(max=128)])
    user_email = StringField('user email', validators=[
        Email(), DataRequired(), Length(max=128)])
    submit = SubmitField('Sign up')