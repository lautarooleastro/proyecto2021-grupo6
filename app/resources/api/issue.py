from flask import jsonify, Blueprint, request, abort
from app.models.configuration import Configuration
from app.models.issue import Issue
from app.models.status import Status
from app.models.category import Category
from app.schemas.issue import issues_schema, issue_schema, issue_pagination_schema
import re

issue_api = Blueprint("consultas", __name__, url_prefix="/consultas")


@issue_api.get('/')
def index():    
    """Retorna el index de denuncias, paginado. Admite selección de página (atributo page)"""
    page = str(request.args.get("page",1))
    if not page.isdigit():
        abort(404)
    page = int(page)
    issues_page = Issue.query.paginate(page=page, per_page=Configuration.per_page())
    if (page>issues_page.total):
        abort(404)
    try:
        issues = issue_pagination_schema.dump(issues_page)
    except:
        abort(500)
    return jsonify(issues), 200


@issue_api.post('/')
def load():
    """Recibe una solicitud de creación de issue, responde con el mismo si la transacción es exitosa"""
    try:
        input = request.json
    except:
        abort(400)
    issue= __newIssue(input)
    try:
        issue_finished = __mask(input)
        issue.save()
    except:
        abort(500)    
    return jsonify(issue_finished), 201    


def __newIssue(input):
    """"Evalua el json recibido y crea un nuevo issue a partir del mismo"""
    try:
        cat = Category.with_id(int(input['categoria_id']))
    except:
        abort(500)
    if cat == None:
        abort(422)
    try:
        phone=re.sub("[^0-9]", "", input['telcel_denunciante'])
        coordinates=str(input['coordenadas']).split(', ')
        issue= Issue(email=input['email_denunciante'], tittle=input['titulo'], description=input['descripcion'], status_id=1, category_id=int(input['categoria_id']), first_name=input['nombre_denunciante'], last_name=input['apellido_denunciante'], latitude=coordinates[0], longitude=coordinates[1], phone=phone)        
    except:
        abort(500)
    return issue
    

def __mask(cls):
    """Enmascara el retorno"""
    return {
        'atributos':cls
    }