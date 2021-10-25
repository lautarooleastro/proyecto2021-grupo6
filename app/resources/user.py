from flask import redirect, render_template, request, url_for, session, abort
from flask.helpers import flash
from flask_login.utils import login_required
from sqlalchemy.sql.functions import user
from app.models.role import Role
from app.models.user import User
from app.helpers.auth import authenticated

from app.db import db

# Protected resources


@login_required
def index():
    users = User.all()

    return render_template("user/index.html", users=users)


@login_required
def new():
    if not User.check_permission(User.with_email(session.get('user')), 'usuario_new'):
        abort(401)

    return render_template("user/new.html")


@login_required
def edit():
    if not User.check_permission(User.with_email(session.get('user')), 'usuario_update'):
        abort(401)

    user_to_update = User.with_id(request.form['edit_id'])
    all_roles = Role.get_all()

    return render_template("user/update.html", user=user_to_update, roles=all_roles)


@login_required
def update():
    if not User.check_permission(User.with_email(session.get('user')), 'usuario_update'):
        abort(401)

    data = request.form
    try:
        updated_user = User.update(data['edit_id'], data)
        flash("Se actualizo al usuario: "+data['email'])
    except Exception as e:
        print(e)
        flash("No se pudo editar al usuario: "+data['email'])

    all_roles = Role.get_all()

    return render_template("user/update.html", user=updated_user, roles=all_roles)


def hasAllParams(params):
    """ Metodo para chequear que el issue tiene todos los params que necesita para ser creado. """
    lista = []
    for param in params.keys():
        lista.append(params.get(param) != '')
    return all(lista)


@login_required
def create():
    if not User.check_permission(User.with_email(session.get('user')), 'usuario_new'):
        abort(401)

    if (hasAllParams(request.form)):
        # creamos el usuario con los parametros del diccionario request.form
        new_user = User(**request.form)

        if (User.already_exists(new_user.email)):
            flash("Ya existe un usuario con mail: '" + new_user.email + "'.")
        else:
            # agregamos el usuario
            db.session.add(new_user)

            # efectuamos los cambios
            db.session.commit()
            flash("Creado con éxito.")
            return redirect(url_for("user_index"))

    else:
        flash("Faltan parametros.")

    return redirect(url_for("user_new"))


@login_required
def destroy():
    if not User.check_permission(User.with_email(session.get('user')), 'usuario_destroy'):
        abort(401)

    try:
        user = User.with_id(request.form['destroy_id'])
        if user.email == authenticated(session):
            raise ValueError("No se puede eliminar al usuario actual.")
        User.destroy(user)
        flash("Se elimino al usuario con mail: "+user.email)
    except ValueError as e:
        flash(e)
    except:
        flash("No se pudo eliminar al usuario con mail: "+user.email)

    return redirect(url_for("user_index"))


@login_required
def toggle(user_email):
    if not User.check_permission(User.with_email(session.get('user')), 'usuario_update'):
        abort(401)

    print("paso el chequeo")
    User.toggle(User.with_email(user_email))
    return redirect(url_for("user_index"))
