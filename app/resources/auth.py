from flask import redirect, render_template, request, url_for, flash
from flask_login.utils import logout_user
from wtforms import form
from app.helpers.forms.auth import SignInForm
from app.models.user import User
from flask_login import login_user


def login():
    return render_template("auth/login.html")


def authenticate():
    data = request.form
    form = SignInForm(data)

    if form.validate():
        user = User.with_email(form.email.data)
        if user:
            if user.password == form.password.data:
                login_user(user)
                flash("Ha iniciado sesion con: "+user.email, "success")
                return redirect(url_for("home"))
        flash("Usuario o contraseña incorrectos", "error")
    else:
        for field in form.errors:
            for error in form.errors[field]:
                flash(field+": "+error, "error")

    return redirect(url_for("auth_login"))


def logout():
    logout_user()
    return redirect(url_for("auth_login"))
