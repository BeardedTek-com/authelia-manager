# External Imports
from flask import Blueprint, escape, redirect, jsonify, make_response, request
from sqlalchemy import desc, asc

# Internal Imports
from app.helpers.argon2 import argon2hash
from app import db

from app.models.config import config
from app.models.acc_networks import acc_networks
from app.models.acc_rules import acc_rules

api = Blueprint('api',__name__)

@api.route('/api')
def apiList():
    apilist = {
        "/api"                              : "API Information (THIS PAGE)",
        "/api/initdb"                       : "Init Database",
        "/api/config [GET]"                 : "Returns All Config Data"
        ""
    }
    return jsonify(apilist)
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