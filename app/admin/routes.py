
from flask import render_template, request, redirect, url_for, flash, abort

from .forms import EncargadoForm, ParcelaForm, CosechaForm, PuestoForm
from . import admin
from .models import Encargado, Parcela, Cosecha
import datetime
from flask_login import login_required, current_user


@admin.route('/dashboard')
@login_required
def dashboard():

    #jcm = CosechaJCM.get_cosechas()
    #bat = CosechaBAT.get_cosechas()

    return render_template('dashboard.html', title="Dashboard")


@admin.route('/encargado/new', methods=['GET', 'POST'])
@login_required
def encargado_form():
    form = EncargadoForm(request.form)

    if form.validate_on_submit():
        encargado_n = Encargado.crear_encargado(form.n_nombres.data, form.n_apellidos.data, form.telefono.data,
                                                form.correo.data)
        print(encargado_n)
        if encargado_n:
            flash("Encargado Guardado Exitosamente", "success")

        return redirect(url_for('admin.encargado'))

    return render_template('encargado/encargado_form.html', title="Encargado", form=form)


@admin.route('/encargado', methods=['GET'])
@login_required
def encargado():
    encargados = Encargado().get_encargados()

    return render_template('encargado/encargado.html', title="Encargados", encargados=encargados)


@admin.route('/encargado/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def encargado_edit(id):
    encargado = Encargado.query.get_or_404(id)
    form = EncargadoForm(request.form, obj=encargado)

    if form.validate_on_submit():
        encargado_up = Encargado.updated_encargado(encargado.id, form.n_nombres.data, form.n_apellidos.data,
                                                   form.telefono.data, form.correo.data)

        if encargado_up:
            flash("Encargado editado satisfactoriamente", "success")
            return redirect(url_for('admin.encargado'))
        else:
            flash("Error al editar", "danger")
            return redirect(url_for('admin.encargado'))

    return render_template('encargado/encargado_edit.html', title="Editar Encargado", form=form)


@admin.route('/encargado/delete/<int:id>')
@login_required
def encargado_delete(id):
    e = Encargado.delete_encargado(id)
    if e:
        flash("Encargado eliminado satisfacotiramente","success")
    return redirect(url_for('admin.encargado'))


@admin.route('/parcela')
@login_required
def parcelas():
    list_parcelas = Parcela().get_parcelas()

    a = Parcela.pos_encargado(list_parcelas)  # lista de posiciones
    nombres = Encargado.name_encargado(a)  # lista de nombres

    par_nom = list(zip(list_parcelas, nombres))
    return render_template('parcela.html', title="Parcelas", parcela_encargado=par_nom)


@admin.route('/parcela/edit/<int:parcela_id>', methods=['GET', 'POST'])
@login_required
def parcela_edit(parcela_id):

    parcela = Parcela.query.get_or_404(parcela_id)  # get_or_404 devuelve error 404 en caso no haya encontrado

    form = ParcelaForm(request.form, obj=parcela)  # cargamos el objeto en el formulario

    # cargamos todos los nombre de encargados en el campo encargado del formulario Parcela
    form.encargado.choices = [(encargado.id, encargado.n_nombres) for encargado in Encargado.query.all()]

    if form.validate_on_submit():
        parcela_updated = Parcela.updated_parcela(parcela.id, form.nombre.data, form.direccion.data, form.area.data
                                                  , form.n_puestos.data, form.encargado.data)
        if parcela_updated:
            flash("Parcela actualidad Exitosamente", "success")
            return redirect(url_for('admin.parcelas'))
    return render_template('parcela_edit.html', title="Editar Parcela", form=form)


@admin.route('/parcela/delete/<int:parcela_id>')
@login_required
def parcela_delete(parcela_id):
    p_delete = Parcela.delete_parcela(parcela_id)
    if p_delete:
        flash("Parcela eliminado exitosamente", "success")

    return redirect(url_for('admin.parcelas'))


@admin.route('/parcela/new', methods=['GET', 'POST'])
@login_required
def parcela_form():
    parcelas = ParcelaForm(request.form)
    form = ParcelaForm()
    form.encargado.choices = [(encargado.id, encargado.n_nombres) for encargado in Encargado.query.all()]

    if form.validate_on_submit():        
        parcela = Parcela.crear_parcela(parcelas.nombre.data, parcelas.direccion.data, parcelas.area.data,
                                        parcelas.n_puestos.data, parcelas.encargado.data)
        if parcela:
            flash("Parcela Registrada Exitosamente", "success")
        return redirect(url_for('admin.parcelas'))

    return render_template('parcela_form.html', title="Parcelas", parcelas=parcelas, form=form)


@admin.route('/dashboard/cosecha/new', methods=['POST', 'GET'])
@login_required
def cosecha_new():
    cosechas = CosechaForm(request.form)

    cosechas.parcela.choices = [(parcela.id, parcela.nombre) for parcela in Parcela.query.all()]

    if cosechas.validate_on_submit():
        c_new = Cosecha.crea_cosecha(cosechas.f_inicio.data, cosechas.f_fin.data, cosechas.n_cosecha.data,
                                     cosechas.n_bolsa.data, cosechas.parcela.data)
        if c_new:
            flash("Cosecha guardado exitosamente", "success")
        return redirect(url_for('admin.cosecha'))

    return render_template('cosecha_form.html', title="Cosechas", cosechas=cosechas)


@admin.route('/cosecha/edit/<int:cosecha_id>', methods=['GET', 'POST'])
@login_required
def cosecha_edit(cosecha_id):
    cosecha = Cosecha.query.get_or_404(cosecha_id)
    form = CosechaForm(request.form, obj=cosecha)
    form.parcela.choices = [(parcela.id, parcela.nombre) for parcela in Parcela.query.all()]
    if form.validate_on_submit():
        cos_updated = Cosecha.update_cosecha(cosecha.id, form.f_inicio.data, form.f_fin.data,
                                             form.n_cosecha.data, form.n_bolsa.data, form.parcela.data)

        if cos_updated:
            flash("Cosecha Actualizada exitosamente", "success")
            return redirect(url_for('admin.cosecha'))

    return render_template('cosecha_edit.html', title="Editar Cosecha", form=form)


@admin.route('/cosecha/delete/<int:cosecha_id>')
@login_required
def cosecha_delete(cosecha_id):
    c_delete = Cosecha.delete_cosecha(cosecha_id)
    if c_delete:
        flash("Cosecha eliminado exitosamente", "success")

    return redirect(url_for('admin.cosecha'))


@admin.route('/dashboard/cosecha')
@login_required
def cosecha():
    list_cosecha = Cosecha().get_cosechas()
    parcelas = Parcela().get_parcelas()

    cosecha_parcela = list(zip(parcelas, list_cosecha))

    for cp in cosecha_parcela:
        print(cp[1].id, cp[0].nombre, cp[1].f_inicio)
    # l_parcelas = Parcela().get_parcelas()
    # encargados = Encargado().get_encargados()
    #
    # parcela_encargado = list(zip(l_parcelas, encargados))
    return render_template('cosecha.html', title="Lista de Cosechas", cosecha_parcela=cosecha_parcela)


@admin.route('/dashboard/puesto-form/<int:id>', methods=['GET', 'POST'])
@admin.route('/dashboard/puesto-form')
@login_required
def puesto_form(id:None):
    form = PuestoForm(request.form)
    puesto = form.n_puesto.data
    cantidad = form.cantidad.data
    lado = form.lado.data
    print(puesto, cantidad, lado)
    return render_template('puesto_form.html', title="Puesto", form=form)


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