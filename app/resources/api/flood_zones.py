from flask import jsonify, Blueprint, request, abort
from app.models.configuration import Configuration
from app.models.flood_zone import FloodZone
from app.schemas.flood_zone import zone_pagination_schema, zone_schema, zones_schema

flood_zones_api = Blueprint(
    "zonas-inundables", __name__, url_prefix="/zonas-inundables")


@flood_zones_api.get('/')
def index():    
    page = str(request.args.get("page",1))
    if not page.isdigit():
        abort(404)
    page = int(page)
    zones_page = FloodZone.query.paginate(page=page, per_page=Configuration.per_page())
    if (page>zones_page.total):
        abort(404)
    zones = zone_pagination_schema.dump(zones_page)
    return jsonify(zones), 200

@flood_zones_api.get('/<int:id>')
def get_zone(id):
    zone = FloodZone.with_id(id)
    if zone != None:
        return jsonify(zone_schema.dump(zone)), 200    
    abort(404)
    
