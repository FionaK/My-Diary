from flask import Flask, Blueprint, jsonify, request
from models import *
from functools import wraps
import datetime
import psycopg2
import jwt
from __init__ import *


users_blueprint=Blueprint('users', __name__)

class Users():
	


	def require_auth(k):
		@wraps(k)
		def authorization(*args, **kwargs):
			token = request.args.get('access_token')
			if not token:
				return jsonify({'message' : 'Missing Token'}), 403
				try:
					data = jwt.decode(token, 'fifi')
				except:
					return jsonify({'message' : 'Invalid Token'}), 408
			return k(*args, **kwargs)
			
		return authorization



	@users_blueprint.route('/api/v2/register/', methods= ['POST', 'GET'])
	def register():
		try:
			name=request.get_json()['name']
			username=request.get_json()['username']
			password=request.get_json()['password']
			email=request.get_json()['email']
			if len(password)<3:
				return jsonify("password should be 4 characters or more")
			if len(name)<3:
				return jsonify({'message': 'name should not be less than 4 characters'})

			cur.execute("SELECT * FROM users WHERE username = '"+username+"' OR email = '"+email+"'")
			if cur.fetchone() is None:
				cur.execute("INSERT INTO users(name,username,password,email)VALUES(%s, %s, %s, %s);",(name, username, password, email))
			else:
				return jsonify({'message': 'username or email already taken'}), 409
				

			conn.commit()

			return jsonify({'message': 'You are successfully registered'})
		except KeyError:
			return jsonify({'message':'Field can not be blank'}), 406

	@users_blueprint.route('/api/v2/login/', methods= ['POST', 'GET'])
	def login():
		username=request.get_json()['username']
		password=request.get_json()['password']

		cur.execute("SELECT COUNT(1) FROM users WHERE username = '"+username+"'")
		if cur.fetchone() is not None:
			cur.execute("SELECT * FROM users WHERE username = '"+username+"'")
			for row in cur.fetchall():
				if password == row[3]:
					token= jwt.encode ({'user':username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=15)}, 'fifi')
					return jsonify({'message': 'Login successful', 'access_token': token.decode('UTF-8')}), 200
				else:
					return jsonify({'message':'wrong password'}), 401
		else:
			return jsonify({'message':'Invalid username'}), 401

	@users_blueprint.route('/api/v2/get_user/', methods=['GET'])
	@require_auth
	def get_user():
		cur.execute("SELECT * FROM users")
		users=cur.fetchall()
		return jsonify(users), 200

	@users_blueprint.route('/api/v2/logout/', methods=['GET'])
	def logout():
		return jsonify({'message': 'Successfully logged out'})



					
					








