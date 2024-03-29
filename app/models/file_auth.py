from app import db

class file_auth(db.Model):
    """
    id                                      : unique identifier
    name                                    : Network Name (no spaces) `internal`
    networks                                : Networks included in acc (comma separated) (CIDR Notation) `192.168.2.0/24,10.0.0.0/8,172.16.0.0/12`
    """
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(1024))
    password_algorithm = db.Column(db.String(50))
    password_iterations = db.Column(db.Integer)
    password_salt_length = db.Column(db.Integer)
    password_parallelism = db.Column(db.Integer)
    password_memory = db.Column(db.Integer)
    notes = db.Column(db.Text)