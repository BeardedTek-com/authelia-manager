"""_summary_"""
# External Imports
import yaml
import json
from flask import Blueprint, jsonify, make_response, render_template, request, redirect, flash, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from os import path, access, R_OK, getcwd
import random

# Internal Imports
from app.helpers.argon2hash import argon2hash, argon2verify
from app.helpers.rndpwd import randpwd
from app.helpers.apidocs import apidocs
from app.helpers.iterateQuery import iterateQuery
from app import db

from app.models.file_auth import file_auth
from app.models.group import group
from app.models.host import host
from app.models.networks import networks
from app.models.rules import rules
from app.models.totp import totp
from app.models.users import users

api = Blueprint('api',__name__)

@api.route('/api',methods=['GET'])
@api.route('/api/account',methods=['GET'])
@api.route('/api/settings',methods=['GET'])
@api.route('/docs',methods=['GET'])
@login_required
def apiDoc():
    APIdocs = apidocs()
    Markdown = APIdocs.md()
    return make_response(render_template('apidocs.html',apidocs=Markdown))

@api.route('/api/initdb',methods=['GET'])
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
    elif data == "user" or data == "users":
        output = {}
        query = users.query.all()
        output = iterateQuery(query)
    elif data == "networks":
        output = {}
        query = networks.query.all()
        output = iterateQuery(query)
    elif data == "rules":
        output = {}
        query = rules.query.all()
        output = iterateQuery(query)
    elif data == "totp":
        output = {}
        query = totp.query.all()
        output = iterateQuery(query)
    elif data == "group":
        output = {}
        query = group.query.all()
        output = iterateQuery(query)
    else:
        output = {"Error":"Invalid Request"}
    return output

@api.route('/api/<data>',methods=['POST'])
def api_data_post(data):
    jsonData = request.get_json()
    print(jsonData)
    if data == "users":
        try:
            query = users.query.filter_by(id=jsonData['id']).first()
            changes = False
            if query.display != jsonData['display']:
                changes = True
                query.display = jsonData['display']
            if query.email != jsonData['email']:
                changes = True
                query.email = jsonData['email']
            if query.groups != jsonData['groups']:
                changes = True
                query.groups = jsonData['groups']
            if query.notes != jsonData['note']:
                changes = True
                query.notes = jsonData['note']
            if changes:
                print("changes")
                db.session.commit()
                output = {"return":0}
            else:
                print("no changes")
                output = {"return":1,"error":"No changes"}
        except Exception as error:
            print(f"ERROR: {error}")
            output = {"return":11,"error":str(error)}
    else:
        error_code = random.randint(0,2)
        output = {"return":error_code}
        if error_code != 0:
            output['error'] = "Test Error Code"
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
    if config_format == "yaml" or config_format == "yml":
        config_data = yaml.dump(config_data)
    else:
        config_data = json.dumps(config_data,indent=2)
    return render_template('config_file.html',data=config_type, Data=config_data, format=config_format)

@api.route('/api/randpw',methods=['GET'])
@login_required
def api_gen_password():
    """
    Generates a random password hash
    """
    pw_format="argon2"
    pw_type="id"
    if pw_format:
    # For now, we only do argon2 password generation.
    # We can expand here when we add more
        if pw_type == "i" or pw_type == "d" or pw_type == "id":
        # Make sure it's a type that we support
            # Generate random password
            rndpwd = randpwd()
            rand_password = rndpwd.generate()
            pwdhash = argon2hash(rand_password)
            hashed_password = pwdhash.gen_hash()
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
            return redirect(url_for('ui.ui_login')) # if the user doesn't exist or password is wrong, reload the page
        # if the above check passes, then we know the user has the right credentials
            
    except Exception as error_string:
        if "no such table" in str(error_string):
            flash("Database is missing. Please contact your administrator and inform them setup is not complete.")
        else:
            flash(f"{error_string}")
        return redirect(url_for('ui.ui_login'))

    return redirect(url_for('ui.ui_main'))

@api.route('/api/logout')
@login_required
def logout():
    display_name = current_user.display
    logout_user()
    flash(f"{display_name} successfully logged out.")
    return redirect(url_for('ui.ui_home'))
