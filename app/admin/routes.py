from flask import render_template, request
from .forms import EmpleadosForm, ParcelasForm, CosechasForm
from .forms import cosechaJCM, cosechaBAT, cosechaKM6
from . import admin
from .models import CosechaJCM

@admin.route('/dashboard')
def get_dashboard():
    return render_template('dashboard.html', title = "Dashboard")

@admin.route('/dashboard/cosechas-jcm', methods=['GET', 'POST'])
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

@admin.route('/dashboard/cosechas-bat')
def cosechasbat():
    bat = cosechaBAT()
    return render_template('cosechas_bat.html', title = "Cosechas - Buenos Aires", bat = bat)

@admin.route('/dashboard/cosechas-km6')
def cosechaskm6():
    km6 = cosechaKM6()
    return render_template('cosechas_km6.html', title = "Cosechas - Buenos Aires", km6 = km6)

@admin.route('/dashboard/parcelas')
def get_parcelas():
    form = ParcelasForm()
    return render_template('parcela.html', title = "Parcelas", form=form)

@admin.route('/dashboard/empleados')
def get_empleados():
    form = EmpleadosForm()
    return render_template('empleados.html', title = "Empleado", form = form)



@admin.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', title= 404), 404