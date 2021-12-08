from flask import render_template, redirect, request, Flask, flash, url_for 
from flask_login.utils import login_required
from flask.helpers import flash, url_for
from wtforms.validators import ValidationError
from app.helpers.permission import permission_required
from app.models.flood_zone import FloodZone
from app.models.flood_point import FloodPoint
from app.models.configuration import Configuration
from wtforms import form
from app.helpers.forms.flood_zone import NewFloodZoneForm
from app.helpers.forms.flood_zone_import import FloodZoneFile
from app.helpers.forms.flood_zone_filter import NewFilter
import csv
import io


@login_required
@permission_required('zona_inundable_index')
def index(page):
    flood_zones = FloodZone.get_all()
    return render_template("flood_zone/index.html", flood_zones=flood_zones, pos=page, cant=Configuration.per_page())

@login_required
@permission_required('zona_inundable_show')
def show(id):
    zona= FloodZone.with_id(id)
    puntos = []
    for point in zona.flood_points:
        puntos.append('{"lat":'+point.latitude+',"lng":'+point.longitude+'}')        
    points = ",".join(puntos)
    points = "["+points+"]"
    return render_template("flood_zone/show.html",
                           zone=zona, points=points)

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

    return redirect(url_for("flood_zone_index", page=1))


@login_required
@permission_required('zona_inundable_new')
def new():
    return render_template("flood_zone/new.html")


@login_required
@permission_required('zona_inundable_new')
def create():
    form = NewFloodZoneForm(request.form, csrf_enabled=False)    
    flood_zone=_newZone(form)
    if _verificar(flood_zone):
        flood_zone.save()
    if FloodZone.with_id(flood_zone.id)!= None:
        flash("Se creó la zona "+flood_zone.code+" correctamente", "success")
        return redirect(url_for("flood_zone_index", page=1))
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
        redirect(url_for("flood_zone_index", page =1))



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
    setattr (oldZone,"name",flood_zone.name)
    setattr (oldZone,"code",flood_zone.code)
    setattr (oldZone,"color",flood_zone.color)
    setattr (oldZone,"status",flood_zone.status)

    try:
        oldZone.modify()
    except ValueError as e:
        flash(e, 'error')   
    if FloodZone.with_id(oldZone.id)!= None:
        flash("Se modificó la zona "+oldZone.code+" correctamente", "success")
    else:
        flash("No fue posible modificar la zona", "error") 
    
    return redirect(url_for('flood_zone_index', page=1)) 




@login_required
@permission_required('zona_inundable_import')
def importZones():
    return render_template("flood_zone/import.html")



@login_required
@permission_required('zona_inundable_import')
def importedZones():    
    form = FloodZoneFile(request.form, csrf_enabled=False)
    file = request.files[form.zones_import.name]
    stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
    fieldnames = ("name","area")
    csv_input = csv.reader(stream,fieldnames)
    
    jsonFAKE = {}
    for row in csv_input:       
        key = row[0]
        jsonFAKE[key] = row[1].split('],[')
    for key in jsonFAKE:
        if len(jsonFAKE[key]) > 2:
            zone=FloodZone()
            form.populate_obj(zone)
            zone.color=zone.color.replace("#","").upper()  #revisar, el caracter # debe ser eliminado antes
            zone.code=key
            zone.name=key
            for pair in jsonFAKE[key]:
                coord=pair.replace("[","").replace("]","").split(',')
                point=FloodPoint(coord[0],coord[1],zone.id)
                zone.flood_points.append(point)
            
            if _verificar(zone):
                try:
                    zone.save()
                except ValueError as e:
                    flash(e, 'error')   

    return redirect(url_for('flood_zone_index', page=1)) 


def _verificar(zone):
        #Verificar 
    if (FloodZone.with_code(zone.code) != None):
        flash("Código de zona "+zone.code+" ya existente", "error")
        return False
    
    if (FloodZone.with_name(zone.name) != None):
        flash("Nombre de zona "+zone.name+" ya existente", "error")
        return False
    return True

@login_required
@permission_required('zona_inundable_index')
def filtrar():
    form = NewFilter(request.form, csrf_enabled=False)
    flood_zones = FloodZone.get_filter(form.status.data, form.code.data)
    return render_template("flood_zone/index.html", flood_zones=flood_zones, pos=1, cant=Configuration.per_page())

@login_required
@permission_required('zona_inundable_index')
def re_index(page,zones):
    return render_template("flood_zone/index.html", flood_zones=zones, pos=page, cant=Configuration.per_page())