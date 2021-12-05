from flask import render_template, redirect, request, Flask, flash, url_for 
from flask_login.utils import login_required
from flask.helpers import flash, url_for
from wtforms.validators import ValidationError
from app.helpers.permission import permission_required
from app.models.flood_zone import FloodZone
from app.models.flood_point import FloodPoint
from wtforms import form
from app.helpers.forms.flood_zone import NewFloodZoneForm
from app.helpers.flood_zone_csv import getZones
import os
from werkzeug.utils import secure_filename

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

    
    flood_zone=_newZone(form)
    flood_zone.save()
    if FloodZone.with_id(flood_zone.id)!= None:
        flash("Se creó la zona "+flood_zone.code+" correctamente", "success")
        return redirect(url_for("flood_zone_index"))
    else:
        flash("No fue posible crear la zona", "error")
        return redirect(url_for("flood_zone_new"))


@login_required
@permission_required('zona_inundable_update')
def edit(id):
    return render_template("flood_zone/edit.html",
                           zone=FloodZone.with_id(id))

@login_required
def _newZone(form):
    data = request.form
    if (form.validate()):
        data.to_dict(flat=False)
        zone= FloodZone()
        form.populate_obj(zone)
        zone.color=zone.color.replace("#","").upper()  #revisar, el caracter # debe ser eliminado antes
        return zone
    else:
        for error in form.errors:
            flash(form.errors[error], "error")
        redirect(url_for("flood_zone_index"))


@login_required
@permission_required('zona_inundable_update')
def modify():    
    form = NewFloodZoneForm(request.form, csrf_enabled=False)
    oldZone=FloodZone.with_id(request.form['modify_id']);
    
    if FloodZone.n_with_code(form.data.get('code')):
        if (FloodZone.with_code(form.data.get('code')).id != oldZone.id):
            flash("Código de zona ya existente", "error")
            return redirect(url_for('flood_zone_show', id=oldZone.id)) 
    
    if FloodZone.n_with_name(form.data.get('name')):
        if (FloodZone.with_name(form.data.get('name')).id != oldZone.id):
            flash("Nombre de zona ya existente", "error")
            return redirect(url_for('flood_zone_show', id=oldZone.id))    

    flood_zone=_newZone(form)
    """
    for aux in flood_zone.__dict__:
        setattr (oldZone,aux,flood_zone.__dict__[aux])"""
    

    setattr (oldZone,"name",flood_zone.name)
    setattr (oldZone,"code",flood_zone.code)
    setattr (oldZone,"color",flood_zone.color)
    setattr (oldZone,"status",flood_zone.status)

    """for fpoint in oldZone.flood_points :
        flood_zone.addPoint(fpoint)"""
    try:
        oldZone.modify()
    except ValueError as e:
        flash(e, 'error')   
    if FloodZone.with_id(oldZone.id)!= None:
        flash("Se modificó la zona "+oldZone.code+" correctamente", "success")
    else:
        flash("No fue posible modificar la zona", "error") 
    

    return redirect(url_for('flood_zone_index')) 


@login_required
@permission_required('zona_inundable_import')
def importZones():
    zones=FloodZone.get_all()
    num=len(zones)-1;
    return render_template("flood_zone/import.html",
                           zone=zones[num])

@login_required
@permission_required('zona_inundable_import')
def importedZones():
    #flash("Llegamos", "success")
    #flash(request.form, "success")
    

    #import pdb; pdb.set_trace()

    #form = NewFloodZoneForm(request.form, csrf_enabled=False)

    #file=request.file['zones_import']

    return redirect(url_for('flood_zone_index')) 
    #getZones(request.form)