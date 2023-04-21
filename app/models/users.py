"""
_summary_
"""
from flask_login import UserMixin
from app import db

class users(db.Model, UserMixin):
    """
    id                                      : unique identifier
    user                                    : username (for login)
    display                                 : display name
    email                                   : email address
    hash                                    : password hash
    groups                                  : comma separated list of groups user belongs to
    """
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50),unique=True)
    display = db.Column(db.String(50))
    email = db.Column(db.String(150),unique=True)
    groups = db.Column(db.String(200))
    hash = db.Column(db.String(150))
    notes = db.Column(db.Text)
