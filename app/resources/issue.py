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
def index(page='1', code='_all', status="None"):
    """shearch=request.form.get('shearch', False, type=bool)
    if (shearch):
        try:
            form = IssuesFilter(request.form, csrf_enabled=False)
        except:
            flash("Error en la búsqueda", "Error")
            return redirect(url_for("flood_zone_index"))
        issues = Issue.get_filter(page, Configuration.per_page(), form.code.data, form.status.data)
        public=form.status.data 
        code=form.code.data
        status=form.status.data
    
    if (status!="None"):
        if (code=='_all'):
            code=''
        if status=="False":
            status=False
        issues = Issue.get_filter(page, Configuration.per_page(), code, status)
        public=status
    else:
        issues = Issue.get_filter(page, Configuration.per_page()) 
        public=True      
    if (code==''):
        code='_all'"""
    issues=Issue.all_paginate();
    return render_template("issue/index.html", issues=issues)


def new():
    form=IssueNew()
    return render_template("issue/new.html", form=form)

def __newIssue(form):
    """Valida los datos ingresados y crea un nuevo issue"""
    if (form.validate()):
        """phone = str(form.phone.data['area_code'])+str(form.phone.data['number'])"""
        phone=str(form.phone.data)
        issue= Issue(email=form.email.data, tittle=form.tittle.data, description=form.description.data, status_id=1, category_id=int(form.category.data), first_name=form.first_name.data, last_name=form.last_name.data, latitude=form.latitude.data, longitude=form.longitude.data, phone=phone)        
        return issue
    else:
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
