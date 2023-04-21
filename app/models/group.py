from app import db

class group(db.Model):
    """
    id                                      : unique identifier
    group                                   : username (for login)
    display                                 : display name
    permissions                             : comma separated permissions
    """
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.String(50),unique=True)
    display = db.Column(db.String(50))
    permissions = db.Column(db.String(200))
    notes = db.Column(db.Text)
