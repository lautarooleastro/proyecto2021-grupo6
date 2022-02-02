from flask import Blueprint
from app.resources.api.issue import issue_api
from app.resources.api.evacuation_route import evacuation_route_api
from app.resources.api.flood_zones import flood_zones_api
from app.resources.api.meeting_point import meeting_point_api


def set_routes(app):
    # Rutas de API-REST (usando Blueprints)
    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(issue_api)
    api.register_blueprint(evacuation_route_api)
    api.register_blueprint(flood_zones_api)
    api.register_blueprint(meeting_point_api)

    app.register_blueprint(api)
