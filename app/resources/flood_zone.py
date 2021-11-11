from flask import render_template, redirect, request
from flask_login.utils import login_required
from flask.helpers import flash, url_for
from wtforms.validators import ValidationError
from app.helpers.permission import permission_required
from app.models.flood_zone import FloodZone

@login_required
#@permission_required('zona_inundable_index')
def index():
    flood_zones = FloodZone.get_all()
    return render_template("flood_zone/index.html", flood_zone=flood_zones)
