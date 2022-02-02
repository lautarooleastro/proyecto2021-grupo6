from marshmallow import Schema, fields
from sqlalchemy import true


class IssueCommentsSchema(Schema):
    issue_id = fields.Int()
    author_id = fields.Int()
    date = fields.Date('%Y-%m-%d')
    description = fields.Str()

class IssueSchema(Schema):
    id = fields.Int()
    tittle = fields.Str()
    description = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    email = fields.Email()
    phone = fields.Str()
    latitude = fields.Str()
    longitude = fields.Str()
    date_open = fields.Date('%Y-%m-%d')
    date_closed = fields.Date('%Y-%m-%d')
    category_id = fields.Int()
    status_id = fields.Int()
    operator = fields.Int()
    comments = fields.Nested(IssueCommentsSchema, many=true, data_key="comments")
    

class IssuePaginationSchema(Schema):
    page = fields.Int()
    total=fields.Int()
    items=fields.Nested(IssueSchema, many=True, data_key="issues")


issues_schema = IssueSchema(many=True)
issue_schema = IssueSchema()
issue_pagination_schema = IssuePaginationSchema()