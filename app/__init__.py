from os import environ

from flask import Flask
from flask_session import Session

from config import config
from app import db

from app.helpers.login import set_login

from app.routes import set_routes

from flask_cors import CORS, cross_origin


def create_app(environment="production"):

    # Configuración inicial de la app
    app = Flask(__name__)
    CORS(app)
    # app.config['CORS_ORIGINS'] = ['url de sitio permitido']
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

    # Seteo de todas las rutas de la aplicacion
    set_routes(app)

    # Retornar la instancia de app configurada
    return app
