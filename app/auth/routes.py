from flask import render_template, request, flash
from . import auth
from .models import Usuario
from .forms import LoginForm, SignupForm

@auth.route('/')
def index():
    return render_template('index.html', title="INDEX")

@auth.route('/signin', methods=['GET','POST'])
def signin():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = Usuario.get_by_username(form.username.data)
        if user and user.verificar_password(form.password.data) :
            flash("Usuario autentificado exitosamente")
        
        else:
            print("usuario o password invalido")
        #print(form.username.data)
        #print(form.password.data)

    return render_template('signin.html', title = "Iniciar Sesión", form = form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)

    if form.validate_on_submit():
        user = Usuario.crear_usuario(form.username.data, form.password.data, form.email.data)
        flash("Usuario create exitosamente")

    return render_template('signup.html', title="Registrar", form=form)