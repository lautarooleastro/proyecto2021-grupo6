from flask import jsonify, Blueprint, request

from app.models.meeting_point import MeetingPoint
from app.schemas.meeting_point import MeetingPointSchema

meeting_point_api = Blueprint(
    "puntos-encuentro", __name__, url_prefix="/puntos-encuentro")


@meeting_point_api.get('/')
def index():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 3))
    points_page = MeetingPoint.query.filter(MeetingPoint.status == True).paginate(
        page=page, per_page=per_page)

    routes = MeetingPointSchema.dump(points_page, many=True)

    return jsonify(routes)
