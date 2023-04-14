# External Imports
from flask import Flask, session, redirect, send_from_directory, make_response, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta
import os


# Flask Setup
app = Flask(__name__)
app.config.update(
SECRET_KEY                        = "SECRET_KEY",
SESSION_COOKIE_NAME               = "authelia-manager_session",
STATIC_FOLDER                     = "static",
TEMPLATES_FOLDER                  = "templates",
DEBUG                             = False,
TESTING                           = False,
SQLALCHEMY_DATABASE_URI           = "sqlite:///authelia-manager.sqlite",
SQLALCHEMY_TRACK_MODIFICATIONS    = False
)

# Session Setup
@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)

# Database Setup
db = SQLAlchemy(app)
app.SQLALCHEMY_TRACK_MODIFICATIONS=False

# Flask Login Setup
from app.models.users import users
login_manager = LoginManager()
login_manager.login_view = 'ui.ui_login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return users.query.get(int(userid))

# Import Blueprints

# API
from app.blueprints import api
app.register_blueprint(api.api)

#UI
from app.blueprints import ui
app.register_blueprint(ui.ui)