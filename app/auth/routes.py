from flask import render_template, request, flash, redirect, url_for
from . import auth
from .models import Usuario
from .forms import LoginForm, SignupForm
from flask_login import login_user, logout_user

from app import login_manager


@login_manager.user_loader
def load_user(user_id):
    """ Permite obtener al usuario de la base de datos, se llama en cada un de
    las peticiones
    Utiliza el decorador user_loader"""

    return Usuario.get_by_id(user_id)


@auth.route('/')
def index():
    return render_template('index.html', title="INDEX")


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm(request.form)

    if form.validate_on_submit():

        user = Usuario.get_by_username(form.username.data)

        if user and user.verificar_password(form.password.data):
            login_user(user)
            flash("Usuario autentificado exitosamente", "success")
            return redirect(url_for('admin.dashboard'))
        else:
            flash("Usuario o contraseña errónea", "danger")
    return render_template('signin.html', title="Iniciar Sesión", form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash("Cerraste sesión exitosamente", "success")
    return redirect(url_for('auth.signin'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)

    if form.validate_on_submit():
        user = Usuario.crear_usuario(form.username.data, form.password.data, form.email.data)

        if user.id:
            flash("Usuario creado exitosamente", "success")
            login_user(user)
            return redirect(url_for("admin.dashboard"))

    return render_template('signup.html', title="Registrar", form=form)
