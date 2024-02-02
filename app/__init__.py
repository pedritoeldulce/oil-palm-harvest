from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

# instancias
bootstrap = Bootstrap()
csrf = CSRFProtect()

def create_app(my_settings_module):
    app = Flask(__name__)
    app.config.from_object(my_settings_module) # carga las configuraciones
    
    csrf.init_app(app)
    bootstrap.init_app(app)

    from app.admin import admin
    app.register_blueprint(admin)

    return app