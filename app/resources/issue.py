from flask import redirect, render_template, request, url_for, flash
from app.models.issue import Issue

from app.db import db

# Public resources


def index():
    issues = Issue.query.all()
    return render_template("issue/index.html", issues=issues)


def new():
    return render_template("issue/new.html")


def hasAllParams(params):
    """ Metodo para chequear que el issue tiene todos los params que necesita para ser creado. """
    lista = []
    for param in params.keys():
        lista.append(params.get(param) != '')
    return all(lista)


def create():
    """ Crea el issue y lo agrega a la BD si es valido. """
    if (hasAllParams(request.form)):
        # los dos asteriscos son para descomponer el diccionario en los diferentes parametros (es una alternativa a usar params[])
        # request.form es un diccionario, pero anteponiendo ** lo separmos en los diferentes parametros
        # **diccionario -> parametros simples
        new_issue = Issue(**request.form)

        # agrego el nuevo issue
        db.session.add(new_issue)

        # efectuo los cambios (se pueden hacer muchos cambios y efectuarlos todos juntos)
        db.session.commit()
        flash("Consulta creada con éxito.")
    else:
        flash("Datos incompletos. Por favor, ingrese todos los datos.")
        return redirect(url_for("issue_new"))

    return redirect(url_for("issue_index"))
