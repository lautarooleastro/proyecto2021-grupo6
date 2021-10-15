from flask import redirect, render_template, request, url_for, session, abort
from flask.helpers import flash
from sqlalchemy.sql.functions import user
from app.models.role import Role
from app.models.user import User
from app.helpers.auth import authenticated

from app.db import db

# Protected resources


def index():
    if not authenticated(session):
        abort(401)

    users = User.all()

    return render_template("user/index.html", users=users)


def new():
    if not authenticated(session):
        abort(401)

    if not User.check_permission(User.with_email(session.get('user')), 'usuario_new'):
        abort(401)

    return render_template("user/new.html")


def hasAllParams(params):
    """ Metodo para chequear que el issue tiene todos los params que necesita para ser creado. """
    lista = []
    for param in params.keys():
        lista.append(params.get(param) != '')
    return all(lista)


def create():
    if not authenticated(session):
        abort(401)

    if (hasAllParams(request.form)):
        # creamos el usuario con los parametros del diccionario request.form
        new_user = User(**request.form)

        if (User.already_exists(new_user.email)):
            flash("Ya existe un usuario con mail: '" + new_user.email + "'.")
        else:
            # por default, lo iniciamos como operador
            default_role = Role.query.filter(Role.name == "Operador").first()
            new_user.roles.append(default_role)

            # agregamos el usuario
            db.session.add(new_user)

            # efectuamos los cambios
            db.session.commit()
            flash("Creado con éxito.")
            return redirect(url_for("user_index"))

    else:
        flash("Faltan parametros.")

    return redirect(url_for("user_new"))


def destroy():
    if not authenticated(session):
        abort(401)

    if not User.check_permission(User.with_email(session.get('user')), 'usuario_destroy'):
        abort(401)

    try:
        user = User.with_id(request.form['destroy_id'])
        User.destroy(user)
        flash("Se elimino al usuario con mail: "+user.email)
    except:
        flash("No se pudo eliminar al usuario con mail: "+user.email)

    return redirect(url_for("user_index"))
