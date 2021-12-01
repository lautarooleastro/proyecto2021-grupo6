from flask import Blueprint
from app.resources.api.issue import issue_api
from app.resources.api.evacuation_route import evacuation_route_api


def set_routes(app):
    # Rutas de API-REST (usando Blueprints)
    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(issue_api)
    api.register_blueprint(evacuation_route_api)

    app.register_blueprint(api)
