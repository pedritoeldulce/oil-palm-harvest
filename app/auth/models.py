import datetime
from flask_login import UserMixin
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model, UserMixin):
    __tablename__="usuarios"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    encrypted_password = db.Column(db.String, nullable = False)
    email = db.Column(db.String(100), unique=True)
    created_at = db.Column(db.DateTime, default= datetime.datetime.now())

    def verificar_password(self, password):
        return check_password_hash(self.encrypted_password, password)

    @property
    def password(self):
        pass

    @password.setter
    def password (self, value):
        self.encrypted_password = generate_password_hash(value)
        

    def __str__(self):
        return self.username
    
    @classmethod
    def crear_usuario(cls, username, password, email):
        user = Usuario(username=username, password = password, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def get_by_username(cls, username):
        return Usuario.query.filter_by(username=username).first()
    
    @classmethod
    def get_by_email(cls, email):
        return Usuario.query.filter_by(email=email).first()
    
    @classmethod
    def get_by_id(cls, id):
        return Usuario.query.filter_by(id=id).first()