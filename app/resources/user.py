from flask import redirect, render_template, request, url_for, session, abort
from flask.helpers import flash
from app.models.user import User
from app.helpers.auth import authenticated

from app.db import db

# Protected resources


def index():
    if not authenticated(session):
        abort(401)

    # Antes de usar ORM, se conectaba asi:
    # conn = connection()
    # users = User.all(conn)

    users = User.query.all()

    return render_template("user/index.html", users=users)


def new():
    if not authenticated(session):
        abort(401)

    return render_template("user/new.html")


def hasAllParams(params):
    """ Metodo para chequear que el issue tiene todos los params que necesita para ser creado. """
    lista = []
    for param in params.keys():
        lista.append(params.get(param) != '')
    return all(lista)


def alreadyExists(new_user):
    """ Devuelve True si ya existe un usuario con el mismo mail que new_user. False caso contrario. """
    query = User.query.filter(User.email == new_user.email).first()
    return (query != None)


def create():
    if not authenticated(session):
        abort(401)

    # conn = connection()
    # User.create(conn, request.form)

    if (hasAllParams(request.form)):
        # creamos el usuario con los parametros del diccionario request.form
        new_user = User(**request.form)

        if (alreadyExists(new_user)):
            flash("Ya existe un usuario con mail: '" + new_user.email + "'.")
        else:
            flash("Creado con éxito.")
            # agregamos el usuario
            db.session.add(new_user)
            # efectuamos los cambios
            db.session.commit()
            return redirect(url_for("user_index"))

    else:
        flash("Faltan parametros.")

    return redirect(url_for("user_new"))
