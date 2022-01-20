from flask import render_template, redirect, request, Flask, flash, url_for 
from flask_login.utils import login_required
from flask.helpers import flash, url_for
from sqlalchemy import false, null, true
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
import json

@login_required
@permission_required('zona_inundable_index')
def index(page='1', code='_all', status="None"):
    shearch=request.form.get('shearch', False, type=bool)
    if (shearch):
        try:
            form = NewFilter(request.form, csrf_enabled=False)
        except:
            flash("Error en la búsqueda", "Error")
            return redirect(url_for("flood_zone_index"))
        flood_zones = FloodZone.get_filter(page, Configuration.per_page(), form.code.data, form.status.data)
        public=form.status.data 
        code=form.code.data
        status=form.status.data
    
    if (status!="None"):
        if (code=='_all'):
            code=''
        if status=="False":
            status=False
        flood_zones = FloodZone.get_filter(page, Configuration.per_page(), code, status)
        public=status
    else:
        flood_zones = FloodZone.get_filter(page, Configuration.per_page()) 
        public=True      
    if (code==''):
        code='_all'
    return render_template("flood_zone/index.html", flood_zones=flood_zones, public=public, code=code, status=status)

@login_required
@permission_required('zona_inundable_index')
def re_index(zones, public=true):
    return render_template("flood_zone/index.html", flood_zones=zones, public=public)


@login_required
@permission_required('zona_inundable_show')
def show(id):
    zona= FloodZone.with_id(id)
    puntos = __points(zona)
    return render_template("flood_zone/show.html",
                           zone=zona, points=puntos)

@login_required
@permission_required('zona_inundable_destroy')
def destroy():
    zone = FloodZone.with_id(request.form['destroy_id'])
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
    flood_zone=__newZone(form)
    pair_list = json.loads(request.form.to_dict()['puntos'])
    flood_zone.flood_points = __pointsLoad(pair_list, flood_zone.id)
    if __verificar(flood_zone):
        flood_zone.save()
    if FloodZone.with_id(flood_zone.id)!= None:
        flash("Se creó la zona "+flood_zone.code+" correctamente", "success")
        return redirect(url_for("flood_zone_index", page=1))
    else:
        flash("No fue posible crear la zona", "error")
        return redirect(url_for('flood_zone_new'))

def __pointsLoad(pair_list,floodZone_id):
    flood_points = []
    if (len(pair_list) >= 3):
        for pair in pair_list:
            flood_points.append(FloodPoint(pair['latitude'], 
                pair['longitude'],floodZone_id))
    return flood_points

@login_required
@permission_required('zona_inundable_update')
def edit(id):
    zona= FloodZone.with_id(id)
    puntos = __points(zona)
    return render_template("flood_zone/edit.html",
                           zone=zona, points=puntos)

def __points(zona):
    puntos = []
    for point in zona.flood_points:
        puntos.append('{"lat":'+point.latitude+',"lng":'+point.longitude+'}')        
    points = ",".join(puntos)
    points = "["+points+"]"
    return points


@login_required
def __newZone(form):
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
    
    flood_zone=__newZone(form)
    setattr (oldZone,"name",flood_zone.name)
    setattr (oldZone,"code",flood_zone.code)
    setattr (oldZone,"color",flood_zone.color)
    setattr (oldZone,"status",flood_zone.status)
    pair_list = json.loads(request.form.to_dict()['puntos'])
    oldZone.flood_points = __pointsLoad(pair_list, oldZone.id)

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
            
            if __verificar(zone):
                try:
                    zone.save()
                except ValueError as e:
                    flash(e, 'error')   

    return redirect(url_for('flood_zone_index', page=1)) 


def __verificar(zone):
        #Verificar 
    """if len(zone.flood_points)<3:
        flash("Se requieren al menos tres puntos en el mapa", "error")
        return False"""

    if (FloodZone.with_code(zone.code) != None):
        flash("Código de zona "+zone.code+" ya existente", "error")
        return False
    
    if (FloodZone.with_name(zone.name) != None):
        flash("Nombre de zona "+zone.name+" ya existente", "error")
        return False
    return True

