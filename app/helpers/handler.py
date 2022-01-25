from flask import render_template, request, jsonify

def not_found_error(e):
    kwargs = {
        "error_name": "404 Not Found Error",
        "error_description": "La url a la que quiere acceder no existe",
    }
    return selec_response(kwargs, 404)


def unauthorized_error(e):
    kwargs = {
        "error_name": "401 Unauthorized Error",
        "error_description": "No esta autorizado para acceder a la url",
    }
    return selec_response(kwargs, 401)


def internal_error(e):
    kwargs = {
        "error_name": "500 Internal Error",
        "error_description": "Se produjo un error interno en el servidor",
    }
    return selec_response(kwargs, 500)


def selec_response(kwargs, status):    
    if request.path.startswith("/api/"):
        return jsonify(kwargs), status
    return render_template("error.html", **kwargs), status