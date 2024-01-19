from flask import jsonify
from . import routes

@routes.route('/', methods=['GET'])
def index():
    return jsonify({'msg': 'helloWorld'})
