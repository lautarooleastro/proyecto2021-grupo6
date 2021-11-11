from flask import render_template, redirect
from flask.helpers import url_for
from app.models.evacuation_route import EvacuationRoute


def index():
    return render_template("evacuation_route/index.html", routes=EvacuationRoute.all())


def detail():
    pass


def new():
    pass


def create():
    pass


def destroy():
    pass


def edit():
    pass


def update():
    pass
