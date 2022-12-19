# External Imports
from flask import Flask, session, redirect, send_from_directory, make_response, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import os

# Internal Imports
from app.helpers.argon2 import argon2hash

# Flask Setup
app = Flask(__name__)
try:
    app.config.update(
    SECRET_KEY                        = "SECRET_KEY",
    SESSION_COOKIE_NAME               = "authelia-manager_session",
    STATIC_FOLDER                     = "static",
    TEMPLATES_FOLDER                  = "templates",
    DEBUG                             = False,
    TESTING                           = False,
    SQLALCHEMY_DATABASE_URI           = "sqlite:///db.sqlite",
    SQLALCHEMY_TRACK_MODIFICATIONS    = False
    )
except:
    pass

# Session Setup
@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)

# Database Setup
db = SQLAlchemy(app)

# Import Blueprints
# API
from app.blueprints import api
app.register_blueprint(api.api)

#UI
from app.blueprints import ui
app.register_blueprint(ui.ui)
