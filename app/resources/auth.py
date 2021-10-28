from flask import redirect, render_template, request, url_for, abort, session, flash
from flask_login import login_manager
from flask_login.utils import logout_user
from sqlalchemy.sql.functions import user
from app.models.user import User
from flask_login import login_user


def login():
    return render_template("auth/login.html")


def authenticate():
    # conn = connection()
    # params = request.form
    # user = User.find_by_email_and_pass(conn, params["email"], params["password"])

    # Me traigo los parametros del formulario
    params = request.form

    user = User.query.filter(
        User.email == params["email"] and User.password == params["password"]
    ).first()

    if (not user) or (user.password != params["password"]):
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))

    login_user(user)

    return redirect(url_for("home"))


def logout():
    logout_user()
    return redirect(url_for("auth_login"))
