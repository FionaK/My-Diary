from flask import Flask, jsonify, request
from functools import wraps
from models import *
import datetime
import psycopg2
import jwt

app=Flask(__name__)

app.config['SECRET_KEY']='fifi'


@app.route('/api/v2/', methods= ['POST','GET'])
def home():
	return jsonify({'message': 'Welcome to my Diary'})

@app.route('/api/v2/register/', methods= ['POST', 'GET'])
def register():
	name=request.get_json()['name']
	username=request.get_json()['username']
	password=request.get_json()['password']
	email=request.get_json()['email']

	cur.execute("SELECT * FROM users WHERE username = '"+username+"'")
	if cur.fetchone() is None:
		cur.execute("INSERT INTO users(name,username,password,email)VALUES(%s, %s, %s, %s);",(name, username, password, email))
	else:
		return jsonify({'message': 'username already exists'}), 409
	conn.commit()

	return jsonify({'message': 'You are successfully registered'})

def token_needed(k):
	@wraps(k)
	def decorated(*args, **kwargs):
		token = request.args.get('access_token')
		if not token:
			return jsonify({'message' : 'Token is missing'})
			try:
				data = jwt.decode(token, app.config['SECRET_KEY'])
			except:
				return jsonify({'message' : 'Token is invalid'})
		return k(*args, **kwargs)
	return decorated

@app.route('/api/v2/login/', methods= ['POST', 'GET'])
def login():
	username=request.get_json()['username']
	password=request.get_json()['password']
	cur.execute("SELECT COUNT(1) FROM users WHERE username = '"+username+"'")
	if cur.fetchone() is not None:
		cur.execute("SELECT * FROM users WHERE username = '"+username+"'")
		for row in cur.fetchall():
			if password == row[3]:
				token= jwt.encode ({'user':username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=15)}, app.config['SECRET_KEY'])
				return jsonify({'message': 'Login successful', 'access_token': token.decode('UTF-8')}), 200
			else:
				return jsonify({'message':'wrong password'}), 401
	else:
		return jsonify({'message':'Invalid username'}), 401

	conn.commit()


@app.route('/api/v2/create_entry/', methods= ['POST', 'GET'])
@token_needed
def create_entry():
	title=request.get_json()['title']
	entry=request.get_json()['entry']
	username=request.get_json()['username']
	cur.execute("INSERT INTO entries(title,entry,username)VALUES(%s, %s, %s);",(title, entry, username))
	conn.commit()
	return jsonify({'message': 'New entry has been created'}), 200

@app.route('/api/v2/display_entry/', methods= ['GET'])
@token_needed
def display_entry():
	cur.execute("SELECT * FROM entries")
	entries=cur.fetchall() 

	return jsonify(entries), 200

@app.route('/api/v2/single_entry/<int:entryid>', methods= ['GET'])
@token_needed
def single_entry(entryid):
	cur.execute("SELECT * FROM entries WHERE entryid="+str(entryid)+";")
	entry=cur.fetchone()
	conn.commit()

	return jsonify(entry), 200

@app.route('/api/v2/delete_entry/<int:entryid>', methods= ['DELETE'])
@token_needed
def delete_entry(entryid):
	cur.execute("SELECT * FROM entries WHERE entryid = '"+str(entryid)+"'")
	user=cur.fetchone()
	if user is not None:
		cur.execute("DELETE FROM entries WHERE entryid='"+str(entryid)+"'")
	else:
		return jsonify({'message':'No user with such an entry exists'}), 401
	conn.commit()

	return jsonify({'message': 'Your entry has been successfully deleted'}), 200

@app.route('/api/v2/modify_entry/<int:entryid>', methods= ['PUT'])	
@token_needed
def modify_entry(entryid):
	title=request.get_json()['title']
	entry=request.get_json()['entry']
	username=request.get_json()['username']

	cur.execute("UPDATE entries SET title= '"+title+"', entry='"+entry+"' WHERE entryid='"+str(entryid)+"'")
	conn.commit()
	return jsonify({'message': 'Your entry has been modified'}), 200

@app.route('/api/v2/get_user/', methods=['GET'])
def get_user():
	cur.execute("SELECT * FROM users")
	users=cur.fetchall()
	return jsonify(users), 200

@app.route('/api/v2/logout/', methods=['GET'])
def logout():
	return jsonify({'message': 'Successfully logged out'})


if __name__	== '__main__':
	app.run(debug=True)












