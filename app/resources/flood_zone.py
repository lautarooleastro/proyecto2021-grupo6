from flask import render_template, redirect, request
from flask_login.utils import login_required
from flask.helpers import flash, url_for
from wtforms.validators import ValidationError
from app.helpers.permission import permission_required
from app.models.flood_zone import FloodZone
from app.models.flood_point import FloodPoint

@login_required
@permission_required('zona_inundable_index')
def index():
    flood_zones = FloodZone.get_all()
    FloodPoint.get_all()
    return render_template("flood_zone/index.html", flood_zones=flood_zones)

@login_required
@permission_required('zona_inundable_destroy')
def destroy():
    try:
        zone = FloodZone.with_id(request.form['destroy_id'])
        for point in zone.flood_points:
            FloodPoint.destroy(point)  
        FloodZone.destroy(zone)
    except ValueError as e:
        flash(e, 'error')
    if FloodZone.with_id(zone.id)!= None:
        flash("Se elimino la zona "+zone.code+"-"+zone.name, "success")
    else:
        flash("Se elimino la zona "+zone.code+"-"+zone.name, "error")

    return redirect(url_for("flood_zone_index"))