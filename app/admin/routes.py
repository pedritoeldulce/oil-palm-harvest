from flask import render_template, request
#from .forms import EmpleadosForm, ParcelasForm, CosechasForm
from .forms import EncargadoForm, ParcelaForm
from . import admin
from .models import Encargado, Parcela
import datetime

@admin.route('/dashboard')
def dashboard():

    #jcm = CosechaJCM.get_cosechas()
    #bat = CosechaBAT.get_cosechas()

    return render_template('dashboard.html', title = "Dashboard")

@admin.route('/dashboard/encargado-form', methods=['GET', 'POST'])
def encargado_form():
    form = EncargadoForm(request.form)

    nombres, apellidos, telefono, correo = form.n_nombres.data, form.n_apellidos.data, form.telefono.data, form.correo.data
    
    if form.validate_on_submit():
        encargado = Encargado(n_nombres=nombres, n_apellidos=apellidos, telefono = telefono, correo = correo)
        encargado.save()


    return render_template('encargado_form.html', title="Encargado", form=form)

@admin.route('/dashboard/encargado', methods=['GET'])
def encargado():
    encargados = Encargado().query.all()
    
    return render_template('encargado.html', title="Encargados", encargados = encargados)


@admin.route('/dashboard/parcelas')
def get_parcelas():
    form = ParcelaForm()
    return render_template('parcela.html', title = "Parcelas", form=form)

@admin.route('/dashboard/parcela-form')
def parcela_form():
    return render_template('parcela_form.html', title="Parcelas")

""" @admin.route('/dashboard/cosechas-jcm', methods=['GET', 'POST'])
def cosechasjcm():
    jcm = cosechaJCM(request.form)

    encargado,n_cosecha, n_bolsas = jcm.encargado.data, jcm.n_cosecha.data, jcm.bolsas.data
    p1, p2, p3, p4, p5, p6, p7, p8 = jcm.puesto_1.data, jcm.puesto_2.data, jcm.puesto_3.data, jcm.puesto_4.data, jcm.puesto_5.data, jcm.puesto_6.data, jcm.puesto_7.data, jcm.puesto_8.data

    total = p1+p2+p3+p4+p5+p6+p7+p8

    if jcm.validate_on_submit():
        # utilizado para guardar los valores en la bd, ya pasaron validate y submit
        # se procede a guardar los datos capturados
        cosecha_jcm = CosechaJCM(encargado = encargado, n_cosecha = n_cosecha, n_bolsas=n_bolsas, p_1 = p1, 
                                 p_2=p2, p_3=p3, p_4=p4, p_5=p5, p_6=p6, p_7=p7, p_8=p8, total = total )

        cosecha_jcm.save()

    return render_template('cosechas_jcm.html', title = "Cosechas - JCM", jcm = jcm, total = total)

@admin.route('/dashboard/cosechas-bat', methods=['GET', 'POST'])
def cosechasbat():
    bat = cosechaBAT(request.form)

    encargado,n_cosecha, n_bolsas = bat.encargado.data, bat.n_cosecha.data, bat.bolsas.data
    p1, p2, p3, p4, p5, p6, p7, p8 = bat.puesto_1.data, bat.puesto_2.data, bat.puesto_3.data, bat.puesto_4.data, bat.puesto_5.data, bat.puesto_6.data, bat.puesto_7.data, bat.puesto_8.data
    p9, p10, p11, p12 = bat.puesto_9.data, bat.puesto_10.data, bat.puesto_11.data, bat.puesto_12.data

    total = p1+p2+p3+p4+p5+p6+p7+p8+p9+p10+p11+p12

    if bat.validate_on_submit():
        cosecha_bat = CosechaBAT(encargado=encargado, n_cosecha = n_cosecha, n_bolsas=n_bolsas, p_1=p1, p_2=p2, p_3=p3, p_4=p4, p_5=p5,
                                 p_6=p6, p_7=p7, p_8=p8, p_9=p9, p_10=p10, p_11=p11, p_12=p12, total =total)

        cosecha_bat.save()
        
    return render_template('cosechas_bat.html', title = "Cosechas - Buenos Aires", bat = bat, total = total)

@admin.route('/dashboard/cosechas-km6')
def cosechaskm6():
    km6 = cosechaKM6()
    return render_template('cosechas_km6.html', title = "Cosechas - Buenos Aires", km6 = km6) """


""" @admin.route('/dashboard/empleados', methods=['GET','POST'])
def empleados():
    form = EmpleadosForm(request.form)
    nombres, apellidos,dni, telefono=form.nombres.data, form.apellidos.data, form.dni.data, form.telefono.data
    
    if form.validate_on_submit():

        empleado = Empleados(nombres = nombres, apellidos=apellidos, dni = dni, telefono = telefono)
        empleado.save()
    return render_template('empleados.html', title = "Empleado", form=form)
 """


@admin.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', title= 404), 404