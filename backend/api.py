from flask import Blueprint, jsonify, request
from random import *

api = Blueprint('api', __name__)

# ハローと返すapi
@api.route('/hello/<string:name>/')
def say_hello(name):
    response = { 'msg': "Hello {}".format(name) }
    return jsonify(response)

# 乱数を返すapi
@api.route('/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)