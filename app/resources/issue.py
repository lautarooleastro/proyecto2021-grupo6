from flask import redirect, render_template, request, url_for
from app.models.issue import Issue

# Public resources


def index():

    # Antes de usar el ORM, se conectaba asi:
    # conn = connection()
    # issues = Issue.all(conn)

    issues = Issue.query.all()

    return render_template("issue/index.html", issues=issues)


def new():
    return render_template("issue/new.html")


def create():
    # conn = connection()
    # Issue.create(conn, request.form)

    return redirect(url_for("issue_index"))
