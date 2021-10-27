from os import environ

from flask import Flask, render_template, Blueprint
from flask_session import Session

from config import config
from app import db
from app.resources.api.issue import issue_api

from app.helpers import handler
from app.helpers import auth as helper_auth
from app.helpers.login import set_login
from app.helpers.permission import check_permission

from app.routes import set_routes


def create_app(environment="production"):

    # Configuración inicial de la app
    app = Flask(__name__)
    app.secret_key = b'a7114859260f52e390e77ac5e319d15acacf527cc7c63b60c72d7e2c966ede14'

    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    # Configure db
    db.init_app(app)

    # Start Flask-Login manager
    set_login(app)

    # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)
    app.jinja_env.globals.update(current_user=helper_auth.current_user)
    app.jinja_env.globals.update(check_permission=check_permission)

    # Seteo de todas las rutas de la aplicacion
    set_routes(app)

    @app.route("/")
    def home():
        return render_template("home.html")

    # Rutas de API-REST (usando Blueprints)
    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(issue_api)

    app.register_blueprint(api)

    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    # Implementar lo mismo para el error 500

    # Retornar la instancia de app configurada
    return app
