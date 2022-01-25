from marshmallow import Schema, fields
from sqlalchemy import true


class FloodPointSchema(Schema):
    latitude = fields.Str()
    longitude = fields.Str()

class FloodZoneSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    code = fields.Str()
    status = fields.Bool()
    color = fields.Str()
    flood_points = fields.Nested(FloodPointSchema, many=true, data_key="points")
    """flood_points = fields.List(fields.List(fields.Str())) """
    """Un diccionario donde la key es la posición del punto, y cada punto es una lista de dos strings"""

class FloodZonePaginationSchema(Schema):
    page = fields.Int()
    total=fields.Int()
    items=fields.Nested(FloodZoneSchema, many=True, data_key="flood_zones")


zones_schema = FloodZoneSchema(many=True)
zone_schema = FloodZoneSchema()
zone_pagination_schema = FloodZonePaginationSchema()