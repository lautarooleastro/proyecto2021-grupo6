from flask_login import current_user
from flask import abort


def check_permission(user, permission):
    """
        Recibe un usuario (User) y el nombre de un permiso (String). 
        Devuelve True si el usuario tiene ese permiso, False caso contrario.
    """
    user_permissions = []
    for role in user.roles:
        for perm in role.permissions:
            user_permissions.append(perm.name)
    return(permission in user_permissions)


def permission_required(permission):
    """
        Decorador para chequear los permisos antes de ejecutar una funcion.
        Recibe el nombre de un permiso (String).
        Si el usuario actual (current_user) tiene dicho permiso, ejecuta la funcion decorada.
        Caso contrario, lanza error 401.
    """
    def requires_permission_decorator(f):
        def check():
            if check_permission(current_user, permission):
                return f()
            else:
                abort(401)
        return check
    return requires_permission_decorator
