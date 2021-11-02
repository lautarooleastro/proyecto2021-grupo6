from flask.templating import render_template
from flask_login.utils import login_required
from app.models.meeting_point import MeetingPoint


@login_required
def index():
    meeting_points = MeetingPoint.get_all()
    return render_template("meeting_point/index.html", meeting_points=meeting_points)
