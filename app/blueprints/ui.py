# External Imports
from flask import Blueprint, escape, redirect, jsonify, make_response, render_template
from flask_login import login_required
from sqlalchemy import desc
import os

# Internal Imports

# API Blueprint Setup
ui = Blueprint('ui',__name__)
@ui.route('/')
def ui_home():
    """
    Home Page for Site

    Returns:
        make_response: outputs render template for text
    """
    intro =  {
                "header": "Easily Integrate On-Prem Authelia 2FA",
                "body": {
                    "1":"Authelia-Manager provides an easy to use interface to quickly deploy\
                        Authelia and its many options without having to manually edit yaml files.\
                        Save time and frustration digging through the docs with an easy way to\
                        explore and set configuration options.",
                    "2":"Join the revolution and be your own 2FA provider!",
                    "button":{
                                "text":"Get Started",
                                "link":{
                                    "url":"https://github.com/beardedtek-com/authelia-manager",
                                    "target":"target='_blank'"
                                },
                                "focus":"true"
                            }
                        },
                "image":{
                        "1":{
                            "src":"/static/img/google-auth.png",
                            "alt":"Google Authenticator",
                            "link":""
                            }
                        }

            }
    intro2 =  {
                "header": "Lock Down Unsecured Web Apps",
                "body": {
                    "1":"If you're using apps with no built-in authentication, you're attack\
                         surface is wide open.  Authelia-Manager can help you protect your\
                         services with one factor, two factor, or even open access with ease!",
                    "2":"Find out just how easy it can be to protect yourself!",
                    "button":{
                                "text":"Learn More",
                                "link":{
                                    "url":"https://github.com/beardedtek-com/authelia-manager",
                                    "target":"target='_blank'"
                                },
                                "focus":"true"
                            }
                        },
                "image":{
                        "1":{
                            "src":"/static/img/lockdown.png",
                            "alt":"App Lockdown",
                            "link":""
                            }
                        }

            }
    output = render_template('ui-home.html',intro=intro,intro2=intro2)
    return make_response(output)


@ui.route('/ui/login')
def ui_login():
    output = render_template('login-form.html')
    return make_response(output)


@ui.route('/ui')
@login_required
def ui_main():
    output = render_template('ui-main.html')
    return make_response(output)

@ui.route('/config')
@login_required
def ui_config():
    output = render_template('ui_config.html')
    return make_response(output)