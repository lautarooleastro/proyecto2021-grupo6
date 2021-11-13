from flask import render_template, redirect, request
from flask.helpers import flash, url_for
from wtforms import form
from app.helpers.forms.evacuation_route import EvacuationRouteForm
from app.models.evacuation_route import EvacuationRoute
from app.models.route_point import RoutePoint


def index():
    return render_template("evacuation_route/index.html", routes=EvacuationRoute.all())


def detail():
    pass


def new():
    return render_template("evacuation_route/new.html")


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


def destroy():
    pass


def edit():
    pass


def update():
    pass
