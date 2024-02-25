from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Usuario',validators=[DataRequired(), Length(min=3, max=50)])
    password= PasswordField('Contraseña',validators=[DataRequired()])


class SignupForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    email = EmailField('Correo Electronico',
                       validators=[DataRequired(), 
                                   Length(min=4, max=90), 
                                   Email(message="Ingrese un email válido")])
    password = PasswordField('Contraseña',
                             validators=[DataRequired(),
                                        EqualTo('confirm_password', message="La contraseña no coincide")])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired(message="Este campo es requerido")])
    accept = BooleanField(validators=[DataRequired()])