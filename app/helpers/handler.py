from flask import render_template, request, jsonify

def bad_request_error(e):
    kwargs = {
        "error_name": "400 Bad Request",
        "error_description": "Error de sintaxis o contenido incorrecto",
    }
    return selec_response(kwargs, 400)


def unauthorized_error(e):
    kwargs = {
        "error_name": "401 Unauthorized Error",
        "error_description": "No esta autorizado para acceder a la url",
    }
    return selec_response(kwargs, 401)


def not_found_error(e):
    kwargs = {
        "error_name": "404 Not Found Error",
        "error_description": "La url a la que quiere acceder no existe",
    }
    return selec_response(kwargs, 404)


def unprocessable_error(e):
    kwargs = {
        "error_name": "422 Unprocessable Entity",
        "error_description": "No fue posible procesar el pedido, revisar validez de los datos enviados",
    }
    return selec_response(kwargs, 422)


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