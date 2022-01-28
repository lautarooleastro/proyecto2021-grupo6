from flask import jsonify, Blueprint, request

from app.models.evacuation_route import EvacuationRoute
from app.schemas.evacuation_route import EvacuationRouteSchema

evacuation_route_api = Blueprint(
    "recorridos-evacuacion", __name__, url_prefix="/recorridos-evacuacion")


@evacuation_route_api.get('/')
def index():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 3))
    routes_page = EvacuationRoute.query.filter(
        EvacuationRoute.status == True).paginate(page=page, per_page=per_page)

    routes = EvacuationRouteSchema.dump(routes_page, many=True)

    return jsonify(routes)
