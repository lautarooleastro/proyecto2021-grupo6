from flask import render_template, request
from flask.helpers import flash, url_for
from werkzeug.utils import redirect
from app.helpers.forms.configuration import ConfigurationForm
from app.helpers.permission import permission_required
from app.models.configuration import Configuration
from flask_login.utils import login_required


@login_required
@permission_required('configuracion_index')
def index():
    configuration = Configuration().get()
    return render_template("configuration/index.html", configuration=configuration)


@login_required
@permission_required('configuracion_index')
def edit():
    configuration = Configuration().get()
    return render_template("configuration/edit.html", configuration=configuration)


def update():
    form = ConfigurationForm(request.form)
    if form.validate():
        configuration = Configuration.get()
        form.populate_obj(configuration)
        configuration.save()
        flash("Se actualizo correctamente", "success")
        return redirect(url_for("configuration_index"))
    else:
        for error in form.errors:
            flash(form.errors[error], "error")
        return redirect(url_for("configuration_edit"))
