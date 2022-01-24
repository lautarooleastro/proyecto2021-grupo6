from flask import render_template, redirect, request
import flask
from sqlalchemy.sql.expression import null
from flask_login.utils import login_required
from flask.helpers import flash, url_for
from app.helpers.permission import permission_required
from app.helpers.forms.meeting_point import PointForm
from app.models.meeting_point import MeetingPoint
from app.models.configuration import Configuration


@login_required
@permission_required('punto_encuentro_index')
def index():
    page = request.args.get('page', 1, type=int)
    name_query = request.args.get('name_query', type=str)
    meeting_points = MeetingPoint.all_paginated(
        page=page, name_query=name_query, config=Configuration.get())
    return render_template("meeting_point/index.html", name_query=name_query, meeting_points=meeting_points)


@login_required
@permission_required('punto_encuentro_new')
def new():
    return render_template("meeting_point/new.html")


@login_required
@permission_required('punto_encuentro_new')
def create():

    meeting_point = MeetingPoint()
    form = PointForm(request.form)

    if form.validate():
        form.populate_obj(meeting_point)
        meeting_point.save()
        flash("El punto de encuentro fue creado con exito", "success")
    else:
        for error in form.errors:
            flash(form.errors[error][0], "error")
        return redirect(url_for('meeting_point_new'))

    return redirect(url_for('meeting_point_index'))


@login_required
@permission_required('punto_encuentro_show')
def detail(id):
    meeting_point = MeetingPoint.with_id(id)
    return render_template("meeting_point/detail.html", meeting_point=meeting_point)


@login_required
@permission_required('punto_encuentro_destroy')
def delete(id):
    meeting_point = MeetingPoint.with_id(id)
    try:
        meeting_point.destroy()
        flash("Se elimino el punto de encuentro: " +
              meeting_point.name, "success")
    except:
        flash("No se pudo eliminar el punto de encuentro: " +
              meeting_point.name, "error")
    return redirect(url_for('meeting_point_index'))


@login_required
@permission_required('punto_encuentro_update')
def edit(id):
    meeting_point = MeetingPoint.with_id(id)
    return render_template("meeting_point/update.html", meeting_point=meeting_point)


@login_required
@permission_required('punto_encuentro_update')
def update(id):
    meeting_point = MeetingPoint.with_id(id)
    form = PointForm(request.form)
    try:
        if form.validate():
            form.populate_obj(meeting_point)
            meeting_point.save()
        flash("Se actualizo el punto de encuentro: " +
              meeting_point.name, "success")
    except:
        flash("No se pudo actualizar el punto de encuentro: " +
              meeting_point.name, "error")
    return redirect(url_for('meeting_point_detail', id=meeting_point.id))
