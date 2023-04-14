"""_summary_"""
# External Imports
import yaml
import json
from flask import Blueprint, jsonify, make_response, render_template, request, redirect, flash, url_for
from flask_login import login_user, logout_user, login_required
from os import path, access, R_OK, getcwd

# Internal Imports
from app.helpers.argon2hash import argon2hash, argon2verify
from app.helpers.rndpwd import randpwd
from app.helpers.apidocs import apidocs
from app.helpers.iterateQuery import iterateQuery
from app import db

from app.models.config import config
from app.models.acc_networks import acc_networks
from app.models.acc_rules import acc_rules
from app.models.users import users
from app.models.group import group

api = Blueprint('api',__name__)

@api.route('/api')
@api.route('/api/account')
@api.route('/api/settings')
@api.route('/docs')
@login_required
def apiDoc():
    APIdocs = apidocs()
    Markdown = APIdocs.md()
    return make_response(render_template('apidocs.html',apidocs=Markdown))

@api.route('/api/initdb')
@login_required
def apiInitDB():
    """
    Initialize the database
    """
    try:
        db.create_all()
        result = True
    except Exception as e:
        result = e
    return jsonify(
            {
                "InitDB"                    : True,
                "Result"                    : result
            }
        )

@api.route('/api/<data>',methods=['GET'])
@login_required
def apiDataGET(data):
    if data == "config":
        config_Data = config.query.all()
        acc_networks_Data = acc_networks.query.all()
        acc_rules_Data = acc_rules.query.all()
        output = {
                    "CONFIG"                    : iterateQuery(config_Data),
                    "Access Control Networks"   : iterateQuery(acc_networks_Data),
                    "Access Control Rules"      : iterateQuery(acc_rules_Data)
            }
    elif data == "user":
        output = {}
        query = users.query.all()
        output = iterateQuery(query)

    elif data == "group":
        output = {}
        query = group.query.all()
        output = iterateQuery(query)
    else:
        output = {"Error":"Invalid Request"}
    print(output)
    return output

@api.route('/api/<config_type>/current/<config_format>',methods=['GET'])
@login_required
def apiUsersCurrentGet(config_format,config_type):
    if config_type == "user" or config_type == "users" or config_type == "users_database":
        config_type = "users_database"
    else:
        config_type = "configuration"
    config_path = f"{getcwd()}/app/data/{config_type}.yml"
    if path.isfile(config_path) and access(config_path, R_OK):
        with open(config_path) as config_file:
            config_data = yaml.safe_load(config_file)
    else:
        config_data = {"Error": f"Cannot read {config}"}
    if format == "yaml" or format == "yml":
        config_data = yaml.dump(config_data)
    else:
        config_data = json.dumps(config_data,indent=2)
    return render_template('config_file.html',data=config_type, Data=config_data, format=config_format)

@api.route('/api/randpw/<pw_format>/<type>',methods=['GET'])
@login_required
def api_gen_password(pw_format,pw_type):
    """
    Generates a random password hash
    """
    if pw_format:
    # For now, we only do argon2 password generation.
    # We can expand here when we add more
        if pw_type == "i" or pw_type == "d" or pw_type == "id":
        # Make sure it's a type that we support
            # Generate random password
            rndpwd = randpwd()
            rand_password = rndpwd.generate()
            print(rand_password)
            pwdhash = argon2hash(rand_password,type=pw_type)
            hashed_password = pwdhash.gen_hash()
            print(hashed_password)
            output = {
                "Password"    : hashed_password
            }
    else:
        output = {
            "Error"         : "Unsupported Format"
        }
    if not output:
        output = {
            "Error"         : "Unknown Error"
        }
    return jsonify(output)

@api.route('/api/login', methods=['POST'])
def api_login():
    # login code goes here
    username = request.form.get('user')
    password = request.form.get('password')
    try:
        user = users.query.filter_by(user=username).first()
        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if user and argon2verify(user.hash,password):
            flash(f"Welcome back, {user.display}")
            login_user(user)
        else:
            flash('Please check your login details and try again.')
            return redirect(url_for('ui.login')) # if the user doesn't exist or password is wrong, reload the page
        # if the above check passes, then we know the user has the right credentials
            
    except Exception as error_string:
        if "no such table" in str(error_string):
            flash("Database is missing. Please contact your administrator and inform them setup is not complete.")
        else:
            flash(f"{error_string}")
        return redirect(url_for('ui.ui_login'))

    return redirect(url_for('ui.ui_home'))

@api.route('/api/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('ui.ui_home'))
