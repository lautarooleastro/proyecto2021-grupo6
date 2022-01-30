from flask import render_template, redirect, request, Flask, flash, url_for 
from flask_login.utils import login_required
from flask.helpers import flash, url_for
from app.helpers.permission import permission_required
from app.models.issue import Issue
from app.models.configuration import Configuration
from app.helpers.forms.issues_filter import IssuesFilter
from app.helpers.forms.issue_new import IssueNew

# Public resources

@login_required
@permission_required('denuncia_index')
def index():    
    page= request.args.get('page', 1, type=int)
    issues=Issue.all_paginate(page);
    filter=IssuesFilter()
    return render_template("issue/index.html", issues=issues, filter=filter)


@login_required
@permission_required('denuncia_create')
def new():
    form=IssueNew()
    return render_template("issue/new.html", form=form)


@login_required
def __newIssue(form):
    """Valida los datos ingresados y crea un nuevo issue"""
    if (form.validate()):
        """phone = str(form.phone.data['area_tittle'])+str(form.phone.data['number'])"""
        phone=str(form.phone.data)
        issue= Issue(email=form.email.data, tittle=form.tittle.data, description=form.description.data, status_id=1, category_id=int(form.category.data), first_name=form.first_name.data, last_name=form.last_name.data, latitude=form.latitude.data, longitude=form.longitude.data, phone=phone)        
        return issue
    else:
        """return render_template("issue/new.html", form=form)"""
        for error in form.errors:
            flash(form.errors[error], "error")


def __verificar(issue=None):
    """Verifica la consistencia de la denuncia"""
    if issue==None:
        return False
    if (Issue.with_id(issue.id) != None):
        return False
    return True


@login_required
@permission_required('denuncia_create')
def create():
    """ Crea el issue y lo agrega a la BD si es valido. """
    if request.method == 'POST':
        form = IssueNew(request.form, csrf_enabled=False)
        issue=__newIssue(form)
        if __verificar(issue):
            issue.save()
            if Issue.with_id(issue.id)!= None:
                flash("Se registró la denuncia correctamente", "success")
                return redirect(url_for("issue_index", page=1))
    flash("No fue posible registrar la denuncia", "error")
    return redirect(url_for('issue_new'))

@login_required
def show(arg):
    pass

    """if (hasAllParams(request.form)):
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

    return redirect(url_for("issue_index"))"""
