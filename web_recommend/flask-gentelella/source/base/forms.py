from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField

## login and registration


class LoginForm(FlaskForm):
    username = TextField('用户名', id='username_login')
    password = PasswordField('密码', id='pwd_login')


class CreateAccountForm(FlaskForm):
    username = TextField('用户名', id='username_create')
    password = PasswordField('密码', id='pwd_create')
