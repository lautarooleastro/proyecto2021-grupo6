
class EvacuationRouteSchema(object):

    @classmethod
    def dump(cls, obj, many=False):
        if many:
            return cls._serialize_collection(obj)
        else:
            return cls._serialize(obj)

    @classmethod
    def _serialize_collection(cls, pagination):
        return {
            "recorridos": [cls._serialize(item) for item in pagination.items],
            "page": pagination.page,
            "per_page": pagination.per_page,
            "total": pagination.total,
        }

    @classmethod
    def _serialize(cls, obj):
        route = {attr.name: getattr(obj, attr.name)
                 for attr in obj.__table__.columns}
        route["coordinates"] = [
            {"lat": point.lat, "lng": point.lng} for point in obj.points]
        return route
