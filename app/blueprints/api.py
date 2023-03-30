# External Imports
from flask import Blueprint, escape, redirect, jsonify, make_response, request, render_template, send_from_directory
from sqlalchemy import desc, asc
import markdown
import yaml
import json
from os import path, access, R_OK, getcwd
import webbrowser

# Internal Imports
from app.helpers.argon2 import argon2hash
from app.helpers.rndpwd import randpwd
from app.helpers.apidocs import apidocs
from app import db

from app.models.config import config
from app.models.acc_networks import acc_networks
from app.models.acc_rules import acc_rules

api = Blueprint('api',__name__)

@api.route('/api')
def apiDoc():
    APIdocs = apidocs()
    Markdown = APIdocs.md()
    return make_response(render_template('apidocs.html',apidocs=Markdown))

@api.route('/api/initdb')
def apiInitDB():
    """
    Initialize the database
    """
    result = db.create_all()
    return jsonify(
            {
                "InitDB"                    : True,
                "Result"                    : result
            }
        )

@api.route('/api/config',methods=['GET'])
def apiConfigGET():
    try:
        config_Data = config.query.all()
        acc_networks_Data = acc_networks.query.all()
        acc_rules_Data = acc_rules.query.all()
        output = {
                    "CONFIG"                    : config_Data,
                    "Access Control Networks"   : acc_networks_Data,
                    "Access Control Rules"      : acc_rules_Data
            }
    except:
        output = {
                "Database Initialized"  : True,
                "Error"                 : "No Data in Database"
            }
    if not output :
        output = {"General Error": True}
    return jsonify(output)

@api.route('/api/<data>/current/<format>',methods=['GET'])
def apiUsersCurrentGet(format,data):
    if data == "user" or data == "users" or data == "users_database":
        data = "users_database"
    else:
        data = "configuration"
    config = f"{getcwd()}/app/data/{data}.yml"
    if path.isfile(config) and access(config, R_OK):
        with open(config) as configFile:
            Data = yaml.safe_load(configFile)
    else:
        Data = {"Error": f"Cannot read {config}"}
    if format == "yaml" or format == "yml":
        Data = yaml.dump(Data)
    else:
        Data = json.dumps(Data,indent=2)
    return render_template('config_file.html',data=data, Data=Data, format=format)

@api.route('/api/randpw/<format>/<type>',methods=['GET'])
def apiGenPassword(format,type):
    """
    Generates a random password hash
    """
    if format:
    # For now, we only do argon2 password generation.
    # We can expand here when we add more
        if type == "i" or type == "d" or type == "id":
        # Make sure it's a type that we support
            # Generate random password
            rndpwd = randpwd()
            Password = rndpwd.generate()
            print(Password)
            pwdhash = argon2hash(rndpwd.generate(),type=type)
            print(pwdhash)
            password = {
                Password    : pwdhash
            }
    else:
        password = {
            "Error"         : "Unsupported Format"
        }
    if not password:
        password = {
            "Error"         : "Unknown Error"
        }
    return jsonify(password)
