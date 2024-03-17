import datetime
from app import db


class Encargado(db. Model):
    __tablename__="encargados"
    id = db.Column(db.Integer, primary_key = True)
    n_nombres = db.Column(db.String(90), nullable = False )
    n_apellidos = db.Column(db.String(90), nullable=False)
    telefono = db.Column(db.String(9), nullable=False)
    correo = db.Column(db.String(90))
    parcelas = db.relationship("Parcela", backref="encargado", lazy=True, cascade="all,delete-orphan")

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        print("Encargado guardado", "success")

    def get_encargados(self):
        e = Encargado().query.all()
        return e

    @classmethod
    def get_by_id(cls, id):
        return Encargado.query.filter_by(id=id).first()

    @classmethod
    def updated_encargado(cls, mid, nombres, apellidos, telefono, correo):
        e = Encargado.get_by_id(mid)

        if e is None:
            return False

        e.n_nombres, e.n_apellidos, e.telefono, e.correo = nombres, apellidos, telefono, correo
        db.session.commit()
        return e

    @classmethod
    def delete_encargado(cls, encargado_id):
        e = Encargado.get_by_id(encargado_id)

        if e:
            db.session.delete(e)
            db.session.commit()

        return e


class Parcela(db.Model):
    __tablename__="parcelas"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(90), nullable=False)
    direccion = db.Column(db.String(120), nullable=False)
    area = db.Column(db.Float, nullable=False)
    n_puestos = db.Column(db.Integer, nullable=False)
    #clave foranea
    encargado_id = db.Column(db.Integer, db.ForeignKey('encargados.id'), nullable=False)
    
    cosechas = db.relationship("Cosecha", backref="parcela", lazy=True)

    def get_parcelas(self):
        p = Parcela().query.all()
        return p

    @classmethod
    def crear_parcela(cls, nombre, direccion, area, n_puestos, encargado_id):
        parcela = Parcela(nombre=nombre, direccion=direccion, area=area, n_puestos=n_puestos, encargado_id=encargado_id)

        db.session.add(parcela)
        db.session.commit()
        return parcela

    @classmethod
    def get_by_id(cls, id):
        return Parcela.query.filter_by(id=id).first()

    @classmethod
    def updated_parcela(cls, id, nombre, direccion, area, n_puestos, encargado_id):
        parcela = Parcela.get_by_id(id)

        if parcela is None:
            return False

        parcela.nombre, parcela.direccion, parcela.area = nombre, direccion, area
        parcela.n_puestos, parcela.encargado_id = n_puestos, encargado_id

        db.session.commit()
        return parcela

    @classmethod
    def delete_parcela(cls, parcela_id):
        p = Parcela.get_by_id(parcela_id)

        if p:
            db.session.delete(p)
            db.session.commit()

        return p


class Cosecha(db.Model):
    __tablename__ = "cosechas"
    id = db.Column(db.Integer, primary_key = True)
    f_inicio = db.Column(db.DateTime, nullable = False)
    f_fin = db.Column(db.DateTime, nullable = False)
    n_cosecha = db.Column(db.Integer, nullable = False)
    n_bolsa = db.Column(db.Integer, nullable=False)
    # clave foranea
    parcela_id = db.Column(db.Integer, db.ForeignKey('parcelas.id'), nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        print("Cosecha guardado")

    @classmethod
    def crea_cosecha(cls, f_inicio, f_fin, n_cosecha, n_bolsa, parcela_id):
        cosecha = Cosecha(f_inicio=f_inicio, f_fin=f_fin, n_cosecha=n_cosecha, n_bolsa=n_bolsa, parcela_id=parcela_id)

        db.session.add(cosecha)
        db.session.commit()
        return cosecha

    @classmethod
    def get_by_id(cls, id):
        return Cosecha.query.filter_by(id=id).first()

    @classmethod
    def update_cosecha(cls, id, inicio, fin, n_cosecha, bolsa, parcela):
        cosecha = Cosecha.get_by_id(id)
        if cosecha is None:
            return False

        cosecha.f_inicio, cosecha.f_fin , cosecha.n_cosecha= inicio,fin, n_cosecha
        cosecha.n_bolsa, cosecha.parcela_id = bolsa, parcela

        db.session.commit()
        return cosecha


    @classmethod
    def delete_cosecha(cls, id):
        c_del = Cosecha.get_by_id(id)

        if c_del:
            db.session.delete(c_del)
            db.session.commit()

        return c_del

    # lazy: Espedifica como se deben cargar los elementos relacionados, dafult select (True)
    #    - select: los elementos deben cargarse de forma diferida cuando se accede a la propiedad por primera vez
        
    # backref: referencia a un nombre de relacion en cadena o una construccion backref(), que se utilizara para generar 
    #    - automaticamente una nueva clase relacionada relationship()  que luego se refiere a esta mediante una configuracion bidireccional.
        
    # para aplicacione modernas se debe preferir el uso de back_populates
    # el parámetro indica el nombre dela relacion en al direccion inversa.

""" class Cosecha(db.Model):
    __tablename__ = "cosechas"
    id = db.Column(db.Integer, primary_key=True)
    f_inicio = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    n_cosecha = db.Column(db.Integer)
    puestos = db.relationship("Puesto")

class Puesto(db.Model):
    __tablename__ = "puestos"
    id= db.Column(db.Integer, primary_key=True)
    numero= db.Column(db.Integer)
    cantidad = db.Column(db.Integer) 
    cosecha_id = db.Column(db.Integer, db.ForeignKey('cosechas.id'))
    cosecha = db.relationship("Cosecha", backref='cosecha', lazy=True)
 """

""" class CosechaJCM(db.Model):
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
        print("Empleado guardado") """