from app import db


class Encargado(db. Model):
    __tablename__ = "encargados"
    id = db.Column(db.Integer, primary_key = True)
    n_nombres = db.Column(db.String(90), nullable = False )
    n_apellidos = db.Column(db.String(90), nullable=False)
    telefono = db.Column(db.String(9), nullable=False)
    correo = db.Column(db.String(90))

    #parcelas = db.relationship("Parcela", backref="encargado", lazy=True, cascade="all,delete-orphan")
    parcelas = db.relationship("Parcela", backref="encargado", lazy=True)

    def get_encargados(self):
        e = Encargado().query.all()
        return e

    @classmethod
    def name_encargado(cls, a):
        n = []
        for pos in a:
            e = Encargado().query.filter_by(id=pos).first()
            n.append(e.n_nombres)
        # mejorar esta funcion
        #n = [encargado.n_nombres for encargado in a]
        return n

    @classmethod
    def get_by_id(cls, id):
        return Encargado.query.filter_by(id=id).first()

    @classmethod
    def crear_encargado(cls, nombres, apellidos, tel, correo):
        encargado = Encargado(n_nombres=nombres, n_apellidos=apellidos, telefono=tel, correo=correo)
        db.session.add(encargado)
        db.session.commit()
        return encargado

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
    __tablename__ = "parcelas"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(90), nullable=False)
    direccion = db.Column(db.String(120), nullable=False)
    area = db.Column(db.Float, nullable=False)
    n_puestos = db.Column(db.Integer, nullable=False)

    # clave foránea
    encargado_id = db.Column(db.Integer, db.ForeignKey('encargados.id'), nullable=True)

    cosechas = db.relationship("Cosecha", backref="parcela", lazy=True)

    def get_parcelas(self):
        p = Parcela().query.all()
        return p

    @classmethod
    def pos_encargado(cls, lista):

        ll = [parcela.encargado_id for parcela in lista]
        # retornamos la lista de posiciones
        return ll

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
    id = db.Column(db.Integer, primary_key=True)
    f_inicio = db.Column(db.DateTime, nullable=False)
    f_fin = db.Column(db.DateTime, nullable=False)
    n_cosecha = db.Column(db.Integer, nullable=False)
    n_bolsa = db.Column(db.Integer, nullable=False)
    # clave foranea
    parcela_id = db.Column(db.Integer, db.ForeignKey('parcelas.id'), nullable=True)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        print("Cosecha guardado")

    def get_cosechas(self):
        return Cosecha().query.all()

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

