from app import db

class totp(db.Model):
    """
    id                                      : unique identifier
    name                                    : Network Name (no spaces) `internal`
    networks                                : Networks included in acc (comma separated) (CIDR Notation) `192.168.2.0/24,10.0.0.0/8,172.16.0.0/12`
    """
    id = db.Column(db.Integer, primary_key=True)
    issuer = db.Column(db.String(1024))
    period = db.Column(db.Integer)
    skew = db.Column(db.Integer)
    notes = db.Column(db.Text)