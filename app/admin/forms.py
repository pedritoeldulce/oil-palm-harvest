from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, DateField, IntegerField, DateTimeLocalField, StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from wtforms.validators import (InputRequired, NumberRange)


class EncargadoForm(FlaskForm):
    n_nombres = StringField(validators=[DataRequired(message="Ingrese el nombre")])
    n_apellidos = StringField(validators=[DataRequired()])
    telefono = StringField(validators=[DataRequired()])
    correo = StringField()

class ParcelaForm(FlaskForm):
    nombre = StringField(validators=[DataRequired()])
    direccion = StringField(validators=[DataRequired()])
    area = DecimalField(validators=[DataRequired()])
    n_puestos = IntegerField(default=0)
    encargado = SelectField('encargado', choices=[], validators=[DataRequired()])

class CosechaForm(FlaskForm):
    parcela = SelectField('parcela', choices=[])
    f_inicio = DateField()
    f_fin = DateField()
    n_cosecha = IntegerField(validators=[DataRequired()],default=0)
    n_bolsa = IntegerField(validators=[DataRequired()], default=0)


"""
 class EmpleadosForm(FlaskForm):
    nombres = StringField(validators=[DataRequired()])
    apellidos = StringField()
    dni = StringField(validators=[DataRequired()])
    telefono = StringField(validators=[DataRequired()])
     f_inicio = DateField('Fecha de Inicio de labores')
    f_fin = DateField('Fecha Fin de labores') 
    # tipo datetime lo veremos depsues


class ParcelasForm(FlaskForm):
    nombre = StringField()
    ubicacion = StringField()
    area = DecimalField()
    total_puestos = IntegerField()
    

class CosechasForm(FlaskForm):
    parcela = SelectField('Parcela', choices=[('JCM', 'El Cajamarquino'), ('BA', 'Buenos Aires - Tomas'), ('KM6', 'KM6')])
    lado = StringField()
    puesto = IntegerField()
    cantidad = IntegerField()
    n_bolsas = IntegerField('Numero de bolsas')
    #fecha = DateTimeLocalField() 
    encargado = StringField()

class cosechaJCM(FlaskForm):
    encargado = SelectField('Encargado', choices=[('Pedro Perez', 'Pedro Perez'),('Paolo Perez', 'Paolo Perez'), ('Segundo Rojas', 'Rojas Rimarachin')])
    n_cosecha = IntegerField('N° cosecha', validators=[InputRequired(), NumberRange(1, 30)])
    bolsas = IntegerField('N° Bolsas', validators=[InputRequired(), NumberRange(1, 999)])
    puesto_1 = IntegerField('Puesto 1', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_2 = IntegerField('Puesto 2', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_3 = IntegerField('Puesto 3', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_4 = IntegerField('Puesto 4', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_5 = IntegerField('Puesto 5', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_6 = IntegerField('Puesto 6', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_7 = IntegerField('Puesto 7', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_8 = IntegerField('Puesto 8', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    
class cosechaBAT(FlaskForm):
    encargado = SelectField('Encargado', choices=[('Pedro Perez'),('Paolo Perez'), ('Rojas Rimarachin')])
    n_cosecha = IntegerField('N° cosecha',validators=[InputRequired(), NumberRange(1,30)])
    bolsas = IntegerField('N° Bolsas', validators=[InputRequired(), NumberRange(1, 999)])
    puesto_1 = IntegerField('Puesto 1', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_2 = IntegerField('Puesto 2', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_3 = IntegerField('Puesto 3', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_4 = IntegerField('Puesto 4', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_5 = IntegerField('Puesto 5', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_6 = IntegerField('Puesto 6', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_7 = IntegerField('Puesto 7', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_8 = IntegerField('Puesto 8', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_9 = IntegerField('Puesto 9', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_10 = IntegerField('Puesto 10', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_11 = IntegerField('Puesto 11', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
    puesto_12 = IntegerField('Puesto 12', validators=[InputRequired(message="Ingresar un valor válido"), NumberRange(0, 999, message="Ingresar un valor mayor a 0")], default=0)
   
class cosechaKM6(FlaskForm):
    encargado = SelectField('Encargado', choices=[('DP', 'Pedro Perez'),('PP', 'Paolo Perez'), ('RR', 'Rojas Rimarachin')])
    n_cosecha = IntegerField('N° cosecha')
    bolsas = IntegerField()
    puesto_1 = IntegerField()
    puesto_2 = IntegerField()
    puesto_3 = IntegerField()
    puesto_4 = IntegerField()
    puesto_5 = IntegerField()
    puesto_6 = IntegerField()
    puesto_7 = IntegerField()
    puesto_8 = IntegerField()
    puesto_9 = IntegerField()
    puesto_10 = IntegerField()
    puesto_11 = IntegerField()
    puesto_12 = IntegerField()
    puesto_13 = IntegerField()
    puesto_14 = IntegerField()
    puesto_15 = IntegerField()
    puesto_16 = IntegerField()
    puesto_17 = IntegerField()
    puesto_18 = IntegerField()
    puesto_19 = IntegerField()
    puesto_20 = IntegerField()
    puesto_21 = IntegerField()

class AsistenciaForm():
    pass 
    
"""