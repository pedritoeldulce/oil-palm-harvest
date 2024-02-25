import datetime
from app import db

class Usuario(db.Model):
    __tablename__="usuarios"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(93), nullable = False)
    email = db.Column(db.String(100), unique=True)
    created_at = db.Column(db.DateTime, default= datetime.datetime.now())

    def __str__(self):
        return self.username
    
    @classmethod
    def crear_usuario(cls, username, password, email):
        user = Usuario(username=username, password = password, email=email)
        db.session.add(user)
        db.session.commit()
        return user
