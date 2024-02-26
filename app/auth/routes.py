from flask import render_template, request, flash
from . import auth
from .models import Usuario
from .forms import LoginForm, SignupForm
import flask_login
from app import login_manager

@login_manager.user_loader
def load_user(id):
    return Usuario.get_by_id(id)

@auth.route('/')
def index():
    return render_template('index.html', title="INDEX")

@auth.route('/signin', methods=['GET','POST'])
def signin():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = Usuario.get_by_username(form.username.data)
        if user and user.verificar_password(form.password.data):
            flask_login.login_user(user) # generamos una sesion
            flash("Usuario autentificado exitosamente","success")
            return render_template('signin.html', title = "Iniciar Sesión", form = form)
        
        flash("Usuario o contraseña errónea", "danger")
    return render_template('signin.html', title = "Iniciar Sesión", form = form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)

    if form.validate_on_submit():
        user = Usuario.crear_usuario(form.username.data, form.password.data, form.email.data)
        flash("Usuario create exitosamente")

    return render_template('signup.html', title="Registrar", form=form)