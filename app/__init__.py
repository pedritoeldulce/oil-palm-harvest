import flask_login
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy


# instancias
db = SQLAlchemy()
bootstrap = Bootstrap()
csrf = CSRFProtect()
login_manager = flask_login.LoginManager()


def create_app(my_settings_module):
    app = Flask(__name__)
    app.config.from_object(my_settings_module)  # carga las configuraciones
    db.init_app(app)
    csrf.init_app(app)
    bootstrap.init_app(app)

    from app.admin import admin
    from app.auth import auth

    login_manager.init_app(app)
    login_manager.login_view = "auth.signin"
    login_manager.login_message = 'Por favor, inicie sesión'
    login_manager.login_message_category = "warning"

    app.register_blueprint(admin)
    app.register_blueprint(auth)

    with app.app_context():
        
        db.create_all()

    return app