from flask import Flask, Blueprint, jsonify, request
from app.models import *
from functools import wraps
import datetime
import psycopg2
import jwt
from __init__ import *

entries_blueprint = Blueprint('entries', __name__)
def require_auth(k):
	@wraps(k)
	def authorization(*args, **kwargs):
		token = request.headers.get('x-access-token')
		if not token:
			return jsonify({'message' : 'Missing Token'}), 403
		try:
			data = jwt.decode(token, 'fifi')
		except:
			return jsonify({'message' : 'Invalid Token'}), 408
		return k(*args, **kwargs)
		
	return authorization

@entries_blueprint.route('/api/v2/create_entry/', methods=['POST'])
@require_auth
def create_entry():
	try:
		title=request.get_json()['title'].strip()
		entry=request.get_json()['entry'].strip()
		data = jwt.decode(request.headers.get('x-access_token'), 'fifi')
		username = data['user']
		if len(title)==0 or len(entry)==0:
			return jsonify({'message':'provide a title and an entry'}), 406
		sql ="SELECT * FROM entries WHERE title = '"+title+"' and username = '"+username+"';"
		cur.execute(sql)
		result = cur.fetchone()
		if result is not None:
			return jsonify({'message':'Title already exists. Choose another title.'})
		else:
			cur.execute("INSERT INTO entries(title,entry,username)VALUES(%s, %s);",(title, entry))
		conn.commit()
		return jsonify({'message': 'New entry has been created'}), 200
	except KeyError:
		return jsonify({'message':'Field can not be blank or check on the field spelling'}), 406
		
@entries_blueprint.route('/api/v2/display_entry/', methods= ['GET'])
@require_auth
def display_entry():
	data = jwt.decode(request.headers.get('x-access_token'), 'fifi')
	username = data['user']
	cur.execute("SELECT * FROM entries WHERE username = '"+username+"'" )
	entries=cur.fetchall()
	return jsonify(entries), 200

@entries_blueprint.route('/api/v2/single_entry/<int:entryid>', methods= ['GET'])
@require_auth
def single_entry(entryid):
	data = jwt.decode(request.headers.get('x-access_token'), 'fifi')
	username = data['user']
	cur.execute("SELECT * FROM entries WHERE entryid='"+str(entryid)+"'")
	entry=cur.fetchone()
	conn.commit()
	return jsonify(entry), 200
	
@entries_blueprint.route('/api/v2/delete_entry/<int:entryid>', methods= ['DELETE'])
@require_auth
def delete_entry(entryid):
	cur.execute("SELECT * FROM entries WHERE entryid = '"+str(entryid)+"'")
	user=cur.fetchone()
	if user is not None:
		cur.execute("DELETE FROM entries WHERE entryid='"+str(entryid)+"'")
	else:
		return jsonify({'message':'No user with such an entry exists'}), 401
	conn.commit()
	return jsonify({'message': 'Your entry has been successfully deleted'}), 200

@entries_blueprint.route('/api/v2/modify_entry/<int:entryid>', methods= ['PUT'])
@require_auth
def modify_entry(entryid):
	title=request.get_json()['title'].strip()
	entry=request.get_json()['entry'].strip()
	data = jwt.decode(request.headers.get('x-access-token'), 'fifi')
	username= data['user']
	if len(title)==0 or len(entry)==0:
		return jsonify({'message':'Please provide a title and an entry!'}), 406
	else:
		cur.execute("SELECT * FROM entries WHERE username = '"+username+"' AND entryid = '"+str(entryid)+"'")
		result = cur.fetchone()
		if result is None:
			return jsonify({'message':'You are not authorized to modify this entry'})
			cur.execute("UPDATE entries SET title= '"+title+"', entry='"+entry+"' WHERE entryid='"+str(entryid)+"'")
	conn.commit()
	return jsonify({'message': 'Your entry has been modified'}), 200
