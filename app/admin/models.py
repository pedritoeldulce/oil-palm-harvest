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
    

# corregir el n_cosecha: tiene que ser correlativo
class CosechaBAT(db.Model):

    __tablename__ = "cosechas_bat"
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
    p_9 = db.Column(db.Integer, nullable=False)
    p_10 = db.Column(db.Integer, nullable=False)
    p_11= db.Column(db.Integer, nullable=False)
    p_12= db.Column(db.Integer, nullable=False)
    total =  db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default= datetime.datetime.utcnow)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        print("cosecha guardada de Buenos Aires")

    def __str__(self):
        return self.n_cosecha
    
    @staticmethod
    def get_cosechas():
        return CosechaBAT.query.filter_by().all()
    

class Empleados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String, nullable=False)
    apellidos = db.Column(db.String, nullable=False)
    dni = db.Column(db.Integer, nullable=False)
    telefono = db.Column(db.String(9), nullable = False)
    #f_inicio = db.Column(db.Datetime, default=datetime.datetime.now())
    #f_fin 
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())


    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        print("Empleado guardado")