from flask import render_template, redirect, request
from flask_login.utils import login_required
from flask.helpers import flash, url_for
from wtforms.validators import ValidationError
from app.helpers.permission import permission_required
from app.models.flood_zone import FloodZone
from wtforms import form
from app.helpers.forms.flood_zone import NewFloodZoneForm

@login_required
@permission_required('zona_inundable_index')
def index():
    flood_zones = FloodZone.get_all()
    return render_template("flood_zone/index.html", flood_zones=flood_zones)

@login_required
@permission_required('zona_inundable_show')
def show(id):
    return render_template("flood_zone/show.html",
                           zone=FloodZone.with_id(id))

@login_required
@permission_required('zona_inundable_destroy')
def destroy():
    zone = FloodZone.with_id(request.form['destroy_id'])
    #if  confirm("¿Confirma la eliminación de la zona "+zone.code+"-"+zone.name+"?")
    try:
        FloodZone.destroy(zone)
    except ValueError as e:
        flash(e, 'error')
    if FloodZone.with_id(zone.id)!= None:
        flash("No fue posible eliminar la zona "+zone.code+"-"+zone.name, "error")
    else:
        flash("Se elimino la zona "+zone.code+"-"+zone.name, "success")

    return redirect(url_for("flood_zone_index"))


@login_required
@permission_required('zona_inundable_new')
def new():
    return render_template("flood_zone/new.html")


@login_required
@permission_required('zona_inundable_new')
def create():

    form = NewFloodZoneForm(request.form, csrf_enabled=False)
    
    #Verificar 
    if (FloodZone.with_code(form.data.get('code')) != None):
            flash("Código de zona ya existente", "error")
            return redirect(url_for("flood_zone_new"))
    
    if (FloodZone.with_name(form.data.get('name')) != None):
            flash("Nombre de zona ya existente", "error")
            return redirect(url_for("flood_zone_new"))

    data = request.form
    if (form.validate()):
        data.to_dict(flat=False)
        flood_zone= FloodZone()
        form.populate_obj(flood_zone)
        flood_zone.color=flood_zone.color.replace("#","").upper()  #revisar, el caracter # debe ser eliminado antes
        flood_zone.save()
        if FloodZone.with_id(flood_zone.id)!= None:
            flash("Se creó la zona "+flood_zone.code+" correctamente", "success")
            return redirect(url_for("flood_zone_index"))
        else:
            flash("No fue posible crear la zona", "error")
            return redirect(url_for("flood_zone_new"))
        
    else:
        for error in form.errors:
            flash(form.errors[error], "error")
    return redirect(url_for("flood_zone_new"))


@login_required
@permission_required('zona_inundable_edit')
def edit(id):
    return render_template("flood_zone/edit.html",
                           zone=FloodZone.with_id(id))

@login_required
@permission_required('zona_inundable_edit')
def modify():    
    form = NewFloodZoneForm(request.form, csrf_enabled=False)

    #Verificar 
    if (FloodZone.n_with_code(form.data.get('code')) > 0 ):
            flash("Código de zona ya existente", "error")
            return redirect(url_for('flood_zone_index')) 
    
    if (FloodZone.n_with_name(form.data.get('name')) > 0):
            flash("Nombre de zona ya existente", "error")
            return redirect(url_for('flood_zone_index')) 
    id = request.form['modify_id']

    data = request.form
    if (form.validate()):
        data.to_dict(flat=False)
        flood_zone= FloodZone()
        form.populate_obj(flood_zone)
        flood_zone.color=flood_zone.color.replace("#","").upper()  #revisar, el caracter # debe ser eliminado antes

        try:
            FloodZone.destroy(FloodZone.with_id(id))
        except ValueError as e:
            flash(e, 'error')
        if FloodZone.with_id(id)!= None:         
            flash("No fue posible modificar la zona", "error")
            return redirect(url_for("flood_zone_index"))
        else:
            flood_zone.save()
            if FloodZone.with_id(flood_zone.id)!= None:
                flash("Se modificó la zona "+flood_zone.code+" correctamente", "success")
                return redirect(url_for("flood_zone_index"))
            else:
                flash("No fue posible modificar la zona", "error")
                return redirect(url_for("flood_zone_index"))
        
    else:
        for error in form.errors:
            flash(form.errors[error], "error")

    return render_template("flood_zone/show.html",
                           zone=FloodZone.with_id(id))