from flask import redirect, render_template, request, url_for, session, abort
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


def create():
    if not authenticated(session):
        abort(401)

    # conn = connection()
    # User.create(conn, request.form)

    # creamos el usuario con los parametros del diccionario request.form
    new_user = User(**request.form)

    # agregamos el usuario
    db.session.add(new_user)

    # efectuamos los cambios
    db.session.commit()

    return redirect(url_for("user_index"))
