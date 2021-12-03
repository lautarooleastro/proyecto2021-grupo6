from flask import jsonify, Blueprint

from app.models.evacuation_route import EvacuationRoute

evacuation_route_api = Blueprint(
    "recorridos-evacuacion", __name__, url_prefix="/recorridos-evacuacion")


@evacuation_route_api.get('/')
def index():
    routes_rows = EvacuationRoute.all()

    routes = [row.as_dict() for row in routes_rows]

    return jsonify(evacuation_routes=routes)
