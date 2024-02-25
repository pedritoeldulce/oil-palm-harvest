from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import validators

from .models import Usuario
class LoginForm(FlaskForm):
    username = StringField('Usuario',validators=[DataRequired(), 
                                                 Length(min=3, max=50),
                                                 ])
    password= PasswordField('Contraseña',validators=[DataRequired()])


# funciones para validar campos
def username_validator(form, field):
    if field.data == 'francescoly' or field.data == 'Francescoly':
        print(field.data)
        raise validators.ValidationError("El username no está permitido XD")

class SignupForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(), username_validator])
    email = EmailField('Correo Electronico',
                       validators=[DataRequired(), 
                                   Length(min=4, max=90), 
                                   Email(message="Ingrese un email válido")])
    password = PasswordField('Contraseña',
                             validators=[DataRequired(),
                                        EqualTo('confirm_password', message="La contraseña no coincide")])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired(message="Este campo es requerido")])
    accept = BooleanField(validators=[DataRequired()])

    def validate_username(self, username):
        if Usuario.get_by_username(username.data):
            raise validators.ValidationError("El usuario ya se encuentra en uso")

    def validate_email(self, email):
        if Usuario.get_by_email(email.data):
            raise validators.ValidationError("El email ya se encuentra en uso")