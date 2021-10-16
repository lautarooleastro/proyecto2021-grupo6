from sqlalchemy.sql.schema import Table
from app.db import db
from sqlalchemy import Column, Integer, String, ForeignKey

# LISTA DE PERMISOS (formato: modulo_accion)
#
# - usuario_index
# - usuario_new
# - usuario_update
# - usuario_destroy
# - usuario_show
#
# - configuracion_update
#
# - punto_encuentro_index
# - punto_encuentro_show
# - punto_encuentro_update
# - punto_encuentro_new
# - punto_encuentro_destroy


class Permission(db.Model):
    """ Define una entidad que se corresponde con la tabla permissions de la BD. """
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    description = Column(String(120))

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description
