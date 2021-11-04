from flask import render_template, redirect, request
from flask_login.utils import login_required
from flask.helpers import flash, url_for
from wtforms.validators import ValidationError
from app.helpers.permission import permission_required
from app.helpers.forms import NewPointForm
from app.models.meeting_point import MeetingPoint


@login_required
@permission_required('punto_encuentro_index')
def index():
    meeting_points = MeetingPoint.get_all()
    return render_template("meeting_point/index.html", meeting_points=meeting_points)


@login_required
@permission_required('punto_encuentro_new')
def new():
    return render_template("meeting_point/new.html")


@login_required
@permission_required('punto_encuentro_new')
def create():

    meeting_point = MeetingPoint()
    form = NewPointForm(request.form)
    try:
        if form.validate():
            form.populate_obj(meeting_point)
            meeting_point.save()
            flash("El punto de encuentro fue creado con exito", "success")
        else:
            raise Exception()
    except Exception as e:
        flash("No se pudo crear el punto de encuentro.", "error")
        if not form.validate():
            flash(form.errors, "error")

    return redirect(url_for('meeting_point_index'))
