from flask import redirect, render_template, request, url_for
from app.models.issue import Issue

from app.db import db

# Public resources


def index():

    # Antes de usar el ORM, se conectaba asi:
    # conn = connection()
    # issues = Issue.all(conn)

    issues = Issue.query.all()

    return render_template("issue/index.html", issues=issues)


def new():
    return render_template("issue/new.html")


def create():
    # conn = connection()
    # Issue.create(conn, request.form)

    # los dos asteriscos son para descomponer el diccionario en los diferentes parametros (es una alternativa a usar params[])
    # request.form es un diccionario, pero anteponiendo ** lo separmos en los diferentes parametros
    # **diccionario -> parametros simples
    new_issue = Issue(**request.form)

    # agrego el nuevo issue
    db.session.add(new_issue)

    # efectuo los cambios (se pueden hacer muchos cambios y efectuarlos todos juntos)
    db.session.commit()

    return redirect(url_for("issue_index"))
