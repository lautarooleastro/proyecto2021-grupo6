from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
    config_db(app)


def config_db(app):
    @app.before_first_request
    def init_database():
        """ Se ejecuta con el primer request (gracias al decorador). Es de SQLAlchemy que crea las tables a partir de los modelos que tenga. Requiere que la BD esta creada. """
        db.create_all()

    @app.teardown_request
    def close_session(exception=None):
        """ Se ejecuta cuando termina el request de Flask (gracias al decorador). Borra la sesion de la BD para no dejarla abierta. """
        db.session.remove()
