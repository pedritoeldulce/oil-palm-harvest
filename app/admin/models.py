import datetime
from app import db

class CosechaJCM(db.Model):
    __tablename__ = "cosechas_jcm"
    id = db.Column(db.Integer, primary_key = True)
    encargado = db.Column(db.String(60), nullable=False)
    n_cosecha = db.Column(db.Integer,unique=True, nullable=False)
    n_bolsas = db.Column(db.Integer, nullable=False)
    p_1 =  db.Column(db.Integer, nullable=False)
    p_2 = db.Column(db.Integer, nullable=False)
    p_3 = db.Column(db.Integer, nullable=False)
    p_4 = db.Column(db.Integer, nullable=False)
    p_5 = db.Column(db.Integer, nullable=False)
    p_6 = db.Column(db.Integer, nullable=False)
    p_7 = db.Column(db.Integer, nullable=False)
    p_8 = db.Column(db.Integer, nullable=False)
    total =  db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default= datetime.datetime.utcnow)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        print("datos cuardados")

    def __str__(self):
        return self.n_cosecha