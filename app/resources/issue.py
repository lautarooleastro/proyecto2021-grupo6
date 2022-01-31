from flask import render_template, redirect, request, Flask, flash, url_for 
from flask_login.utils import login_required
from flask.helpers import flash, url_for
from app.helpers.permission import permission_required
from app.models.issue import Issue
from app.models.configuration import Configuration
from app.helpers.forms.issues_filter import IssuesFilter
from app.helpers.forms.issue_new import IssueNew
from app.helpers.forms.issue_edit import IssueEdit
from app.models.user import User
from app.models.status import Status
from app.models.category import Category

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
@permission_required('denuncia_show')
def show(id):
    issue = Issue.with_id(id)
    operator = User.with_id(issue.operator)
    status = Status.with_id(issue.status_id)
    category= Category.with_id(issue.category_id)
    return render_template("issue/show.html", issue=issue, operator=operator, status=status, category=category)


@login_required
@permission_required('denuncia_update')
def edit():
    pass


@login_required
@permission_required('denuncia_destroy')
def destroy():
    pass
    issue = Issue.with_id(request.form['destroy_id'])
    try:
        Issue.destroy(issue)
    except ValueError as e:
        flash(e, 'error')
    if Issue.with_id(issue.id)!= None:
        flash("No fue posible eliminar la denuncia "+issue.tittle, "error")
    else:
        flash("Se elimino la denuncia "+issue.tittle, "success")

    return redirect(url_for("issue_index", page=1))