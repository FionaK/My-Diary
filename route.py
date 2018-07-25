from flask import Flask, Blueprint, jsonify, request

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/api/v2/', methods=['GET'])
def home_page():
	return jsonify({'message': 'Welcome to my diary'})
