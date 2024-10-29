from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from bson.objectid import objectId

from flask import jsonify,request

from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)

