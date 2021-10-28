from flask import redirect, render_template, request, url_for, session, abort
from flask.helpers import flash
from flask_login.utils import login_required
from app.helpers.permission import permission_required
from app.models.role import Role
from app.models.user import User
from app.helpers.auth import authenticated

from app.db import db

# Protected resources


@login_required
@permission_required('usuario_index')
def index():
    users = User.all()

    return render_template("user/index.html", users=users)


@login_required
@permission_required('usuario_new')
def new():
    return render_template("user/new.html", roles=Role.get_all())


@login_required
@permission_required('usuario_update')
def edit():
    user_to_update = User.with_id(request.form['edit_id'])
    all_roles = Role.get_all()

    return render_template("user/update.html", user=user_to_update, roles=all_roles)


@login_required
@permission_required('usuario_update')
def update():
    data = request.form
    try:
        updated_user = User.update(data['edit_id'], data)
        flash("Se actualizo al usuario: "+data['email'])
    except Exception as e:
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
@permission_required('usuario_new')
def create():
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
@permission_required('usuario_destroy')
def destroy():
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
@permission_required('usuario_update')
def toggle(user_email):
    User.toggle(User.with_email(user_email))
    return redirect(url_for("user_index"))


@login_required
def profile():
    return render_template("user/profile.html")


@login_required
@permission_required('usuario_update')
def profile_edit():
    return render_template("user/profile_edit.html")
