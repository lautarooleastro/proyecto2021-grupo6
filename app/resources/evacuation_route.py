from flask import render_template, redirect, request
from flask.helpers import flash, url_for
from flask_login.utils import login_required
from wtforms import form
from app.helpers.forms.evacuation_route import EditEvacuationRouteForm, EvacuationRouteForm
from app.models.evacuation_route import EvacuationRoute
from app.models.route_point import RoutePoint
from app.helpers.permission import permission_required


@login_required
@permission_required('recorrido_evacuacion_index')
def index():
    return render_template("evacuation_route/index.html", routes=EvacuationRoute.all())


@login_required
@permission_required('recorrido_evacuacion_show')
def detail(id):
    return render_template("evacuation_route/detail.html",
                           route=EvacuationRoute.with_id(id))


@login_required
@permission_required('recorrido_evacuacion_new')
def new():
    return render_template("evacuation_route/new.html")


@login_required
@permission_required('recorrido_evacuacion_new')
def create():
    data = request.form
    form = EvacuationRouteForm(request.form)
    if (form.validate()):
        data = dict((key, request.form.getlist(key))
                    for key in request.form.keys())

        if (len(data['latitude']) >= 3):
            route_points = []
            for pos in range(len(data['latitude'])):
                point = RoutePoint(data['latitude'][pos],
                                   data['longitude'][pos])
                route_points.append(point)

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


@login_required
@permission_required('recorrido_evacuacion_destroy')
def destroy(id):
    route = EvacuationRoute.with_id(id)
    if route:
        route.destroy()
        flash("Se elimino correctamente", "success")
    else:
        flash("No existe la ruta con id; "+id, "error")

    return redirect(url_for("evacuation_route_index"))


@login_required
@permission_required('recorrido_evacuacion_update')
def edit(id):
    return render_template("evacuation_route/update.html",
                           route=EvacuationRoute.with_id(id))


@login_required
@permission_required('recorrido_evacuacion_update')
def update(id):
    form = EditEvacuationRouteForm(request.form)
    if form.validate():
        route = EvacuationRoute.with_id(id)
        form.populate_obj(route)
        route.save()
        flash("Se actualizo correctamente la ruta: "+route.name, "success")
    else:
        for error in form.errors:
            flash(form.errors[error], "error")
        return redirect(url_for("evacuation_route_edit", id=id))

    return redirect(url_for("evacuation_route_detail", id=route.id))
