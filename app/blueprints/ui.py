# External Imports
from flask import Blueprint, escape, redirect, jsonify, make_response, render_template
from sqlalchemy import desc
import os

# Internal Imports

# API Blueprint Setup
ui = Blueprint('ui',__name__)
@ui.route('/')
@ui.route('/ui')
def uiHome():
    Text =  "This utility will allow you to manage your authelia configuration.  "
    Text += "It uses a sqlite backend to track changes to your config.  "
    Text += "Hopefully this will be found useful."
    output = render_template('textbody.html',textbody=Text,domain="jeandr.net")
    return make_response(output)
