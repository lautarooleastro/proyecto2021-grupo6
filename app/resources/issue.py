from flask import render_template, redirect, request, Flask, flash, url_for 
from flask_login.utils import login_required
from flask.helpers import flash, url_for
from app.helpers.permission import permission_required
from app.models.issue import Issue
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
    """Prepara y lanza la vista del listado de denuncias, incluyendo paginación y un formulario de filtro"""  
    page= request.args.get('page', 1, type=int)
    issues=Issue.all_paginate(page);
    filter=IssuesFilter()
    return render_template("issue/index.html", issues=issues, filter=filter)


@login_required
@permission_required('denuncia_create')
def new():
    """Prepara y lanza el formulario de carga de una nueva denuncia (IssueNew)"""
    form=IssueNew()        
    form.category.choices= __categories()
    return render_template("issue/new.html", form=form)


@login_required
def __newIssue(form):
    """Valida los datos del formulario ingresado y crea un issue a partir de un formulario de IssueNew"""        
    form.category.choices= __categories()
    if (form.validate()):
        phone=str(form.phone.data)
        issue= Issue(email=form.email.data, tittle=form.tittle.data, description=form.description.data, status_id=1, category_id=int(form.category.data), first_name=form.first_name.data, last_name=form.last_name.data, latitude=form.latitude.data, longitude=form.longitude.data, phone=phone)        
        return issue
    

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
    return render_template("issue/new.html", form=form)

@login_required
@permission_required('denuncia_show')
def show(id):
    """Prepara y lanza la vista de una denuncia pasa por ID"""
    issue = Issue.with_id(id)
    operator = User.with_id(issue.operator)
    status = Status.with_id(issue.status_id)
    category= Category.with_id(issue.category_id)
    return render_template("issue/show.html", issue=issue, operator=operator, status=status, category=category)

@login_required
def __statuses():
    statuses = Status.get_all()
    estados=[]
    for aux in statuses:
        estados.append((int(aux.id),str(aux.name)))
    return estados

@login_required
def __categories():
    categories = Category.get_all()
    categorias=[]
    for aux in categories:
        categorias.append((int(aux.id),str(aux.name)))
    return categorias

@login_required
def __users():
    users=User.get_all()
    usuarios=[]
    for aux in users:
        usuarios.append((str(aux.id),str(aux.username)))
    return usuarios

@login_required
@permission_required('denuncia_update')
def edit(id):
    """Prepara y lanza el formulario de edición de denuncias (IssueEdit) para la denuncia pasara por ID"""
    issue=Issue.with_id(id)
    editForm=IssueEdit()
    editForm.date_open.default=issue.date_open
    editForm.description.default=issue.description
    editForm.email.default=issue.email
    editForm.first_name.default=issue.first_name
    editForm.last_name.default=issue.last_name
    editForm.latitude.default=issue.latitude
    editForm.longitude.default=issue.longitude
    editForm.phone.default=issue.phone
    editForm.tittle.default=issue.tittle
    editForm.operator.choices= __users()
    editForm.operator.default=issue.operator
    editForm.category.choices= __categories()
    editForm.category.default=issue.category_id        
    editForm.status.choices= __statuses()
    editForm.status.default=issue.status_id    
    editForm.date_closed.default=issue.date_closed
    editForm.process()
    return render_template("issue/edit.html", editForm=editForm, id=issue.id)

@login_required
@permission_required('denuncia_update')
def modify(id):
    """Recibe, valida y aplica los cambios a un issue pasaro por ID"""
    issue_old=Issue.with_id(id)
    if request.method == 'POST':
        form = IssueEdit(request.form, csrf_enabled=False)
        form.operator.choices = __users()
        form.category.choices = __categories()
        form.status.choices = __statuses()
        issue=__editIssue(form,issue_old)
        if issue!=None:
            issue.id=id
            issue.issue_comment = issue_old.issue_comment
            issue.modify()
            if Issue.with_id(issue.id)!= None:
                flash("Se modificó la denuncia correctamente", "success")
                return redirect(url_for("issue_index", page=1))
    flash("No fue posible modificar la denuncia", "error")
    return render_template("issue/edit.html", editForm=form, id=id)

@login_required
def __editIssue(form,issue):
    """Valida los datos ingresados y modifica un issue a partir de un formulario de IssueEdit"""
    if (form.validate()):
        issue.phone=str(form.phone.data)
        issue.email=form.email.data
        issue.tittle=form.tittle.data
        issue.description=form.description.data
        issue.category_id=int(form.category.data)
        issue.first_name=form.first_name.data
        issue.last_name=form.last_name.data
        issue.latitude=form.latitude.data
        issue.longitude=form.longitude.data        
        issue.date_open = form.date_open.data       
        issue.date_closed = form.date_closed.data
        issue.operator = int(form.operator.data)
        issue.status_id = int(form.status.data)
        return issue

@login_required
@permission_required('denuncia_destroy')
def destroy():
    """Elimina un issue de la DB"""
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