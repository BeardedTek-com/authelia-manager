from app import db

class host(db.Model):
    """
    id                                      : unique identifier
    host                                    : Host/Interface (0.0.0.0)
    port                                    : Port Number
    log_level                               : Log Level
    default_redirection_url                 : Default Redirection URL
    jwt_secret                              : JWT Secret
    authentication_backend                  : 'file' or 'ldap' authentication backend
    """
    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(1024))
    port = db.Column(db.Integer)
    log_level = db.Column(db.String(1024))
    default_redirection_url = db.Column(db.String(1024))
    jwt_secret = db.Column(db.String(64))
    authentication_backend = db.Column(db.String(4))
    default_policy = db.Column(db.String(5))
    notes = db.Column(db.Text)