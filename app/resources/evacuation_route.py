from flask import render_template, redirect, request
from flask.helpers import flash, url_for
from flask_login.utils import login_required
from sqlalchemy.sql.expression import null
from wtforms import form
from app.helpers.forms.evacuation_route import EvacuationRouteForm
from app.models.configuration import Configuration
from app.models.evacuation_route import EvacuationRoute
from app.models.route_point import RoutePoint
from app.helpers.permission import permission_required
import json


@login_required
@permission_required('recorrido_evacuacion_index')
def index():
    page = request.args.get('page', 1, type=int)
    name_query = request.args.get('name_query', type=str)
    status_query = request.args.get('status_query', type=str)
    routes = EvacuationRoute.all_paginated(
        page=page, name_query=name_query, status_query=status_query, config=Configuration.get())
    return render_template("evacuation_route/index.html", name_query=name_query, status_query=status_query, routes=routes)


@ login_required
@ permission_required('recorrido_evacuacion_show')
def detail(id):
    evacuation_route = EvacuationRoute.with_id(id)
    points_list = []
    for point in evacuation_route.points:
        points_list.append(point.toJSONstringify())
    points = ",".join(points_list)
    points = "["+points+"]"
    return render_template("evacuation_route/detail.html",
                           route=evacuation_route, points=points)


@ login_required
@ permission_required('recorrido_evacuacion_new')
def new():
    return render_template("evacuation_route/new.html")


@ login_required
@ permission_required('recorrido_evacuacion_new')
def create():
    form = EvacuationRouteForm(request.form)
    if (form.validate()):
        coordinates_list = json.loads(request.form.to_dict()['coordinates'])
        if (len(coordinates_list) >= 3):
            route_points = []

            for coordinates in coordinates_list:
                route_points.append(RoutePoint(
                    lat=coordinates['lat'], lng=coordinates['lng']))

            evacuation_route = EvacuationRoute()
            form.populate_obj(evacuation_route)
            evacuation_route.points = route_points
            evacuation_route.save()
            flash("Se creo el recorrido de evacuacion correctamente", "success")
            return redirect(url_for("evacuation_route_index"))
        else:
            flash("Especifique al menos 3 puntos del recorrido", "error")
    else:
        for error in form.errors:
            flash(form.errors[error], "error")
    return redirect(url_for("evacuation_route_new"))


@ login_required
@ permission_required('recorrido_evacuacion_destroy')
def destroy(id):
    route = EvacuationRoute.with_id(id)
    if route:
        route.destroy()
        flash("Se elimino correctamente", "success")
    else:
        flash("No existe la ruta con id; "+id, "error")

    return redirect(url_for("evacuation_route_index"))


@ login_required
@ permission_required('recorrido_evacuacion_update')
def edit(id):
    evacuation_route = EvacuationRoute.with_id(id)
    points_list = []
    for point in evacuation_route.points:
        points_list.append(point.toJSONstringify())
    points = ",".join(points_list)
    points = "["+points+"]"
    return render_template("evacuation_route/update.html",
                           route=evacuation_route, points=points)


@ login_required
@ permission_required('recorrido_evacuacion_update')
def update(id):
    form = EvacuationRouteForm(request.form)
    if form.validate():
        coordinates_list = json.loads(request.form.to_dict()['coordinates'])
        if (len(coordinates_list) >= 3):
            route_points = []

            for coordinates in coordinates_list:
                route_points.append(RoutePoint(
                    lat=coordinates['lat'], lng=coordinates['lng']))

            route = EvacuationRoute.with_id(id)
            form.populate_obj(route)
            route.points = route_points
            route.save()
            flash("Se actualizo correctamente la ruta: "+route.name, "success")
        else:
            flash("Debe seleccionar al menos 3 puntos del mapa", "error")
    else:
        for error in form.errors:
            flash(form.errors[error], "error")
        return redirect(url_for("evacuation_route_edit", id=id))

    return redirect(url_for("evacuation_route_detail", id=route.id))
