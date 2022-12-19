from app import db

class acc_rules(db.Model):
    """
    id                                      : unique identifier
    domain                                  : `*.example.com`
    domain_regex                            : `empty string`
    policy                                  : one_factor or two_factor or pass `two_factor`
    networks                                : comma separated list of networks defined in acc_networks `internal`
    subject                                 : comma separated list of users, groups in format of ['user:username'] or ['group:groupname']
    NOTE: NEED TO ADD EVERYTHING ELSE BUT THIS GETS US STARTED FOR NOW.
    """
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(250))
    domain_regex = db.Column(db.String(250))
    policy = db.Column(db.String(15))
    networks = db.Column(db.String(1024))
    subject = db.Column(db.String(1024))