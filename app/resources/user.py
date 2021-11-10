from flask import redirect, render_template, request, url_for, session, abort
from flask.helpers import flash
from flask_login.utils import login_required
from flask_login import current_user
from app.helpers.forms.user import UserForm
from app.helpers.permission import permission_required
from app.models.role import Role
from app.models.user import User


# Protected resources


@login_required
@permission_required('usuario_index')
def index():
    users = User.all()
    users.remove(current_user)
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
        flash("Se actualizo al usuario: "+data['email'], 'success')
    except Exception as e:
        flash("No se pudo editar al usuario: "+data['email'], 'error')

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
    data = request.form
    user = User()
    form = UserForm(data)
    print(data)

    if User.already_exists(form.email.data):
        flash("Ya existe el usuario con mail: "+form.email.data, "error")
        return redirect(url_for("user_new"))

    if (data and form.validate()):
        try:
            form.populate_obj(user)
            roles = []
            for role_name in data.keys():
                if data[role_name] == 'role':
                    roles.append(Role.with_name(role_name))
            user.roles = roles
            user.save()
            flash("Se creo correctamente al usuario: "+user.email, "success")
        except:
            flash("Ocurrió un error. No se pudo crear al usuario.", "error")
    else:
        for field in form.errors:
            for error in form.errors[field]:
                flash(error, "error")
        return redirect(url_for("user_new"))

    return redirect(url_for("user_index"))


@login_required
@permission_required('usuario_destroy')
def destroy():
    try:
        user = User.with_id(request.form['destroy_id'])
        if user == current_user:
            raise ValueError("No se puede eliminar al usuario actual.")
        User.destroy(user)
        flash("Se elimino al usuario con mail: "+user.email, "success")
    except ValueError as e:
        flash(e, 'error')
    except:
        flash("No se pudo eliminar al usuario con mail: "+user.email, "error")

    return redirect(url_for("user_index"))


@login_required
def toggle(user_email):
    try:
        activado = User.toggle(User.with_email(user_email))
        if activado:
            flash("Usuario activado: "+user_email, 'success')
        else:
            flash("Usuario desactivado: "+user_email, 'success')
    except:
        flash("No se pudo activar/desctivar al usuario: "+user_email, 'error')
    return redirect(url_for("user_index"))


@login_required
def profile():
    return render_template("user/profile.html")


@login_required
@permission_required('usuario_update')
def profile_edit():
    return render_template("user/profile_edit.html")


@login_required
@permission_required('usuario_update')
def profile_update():
    try:
        # Pendiente agregar chequeo con wtforms y juntar ambos update en un mismo metodo
        User.update_profile(request.form)
        flash("Su perfil se actualizó correctamente.", "success")
    except:
        flash("Ocurrió un error. No se pudo actualizar su perfil.", "error")
    return redirect(url_for("user_profile"))
