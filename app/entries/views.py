from flask import Flask, Blueprint, jsonify, request
from models import *
from functools import wraps
import datetime
import psycopg2
import jwt
from __init__ import *


entries_blueprint = Blueprint('entries', __name__)

class Entries():
	

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



	@entries_blueprint.route('/api/v2/create_entry/', methods=['POST'])
	@require_auth
	def create_entry():
		title=request.get_json()['title']
		entry=request.get_json()['entry']
		username=request.get_json()['username']
		cur.execute("INSERT INTO entries(title,entry,username)VALUES(%s, %s, %s);",(title, entry, username))
		conn.commit()
		return jsonify({'message': 'New entry has been created'}), 200

	@entries_blueprint.route('/api/v2/display_entry/', methods= ['GET'])
	@require_auth
	def display_entry():
		cur.execute("SELECT * FROM entries")
		entries=cur.fetchall()

		return jsonify(entries), 200

	@entries_blueprint.route('/api/v2/single_entry/<int:entryid>', methods= ['GET'])
	@require_auth
	def single_entry(entryid):
		cur.execute("SELECT * FROM entries WHERE entryid="+str(entryid)+";")
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
		title=request.get_json()['title']
		entry=request.get_json()['entry']
		username=request.get_json()['username']

		cur.execute("UPDATE entries SET title= '"+title+"', entry='"+entry+"' WHERE entryid='"+str(entryid)+"'")
		conn.commit()
		return jsonify({'message': 'Your entry has been modified'}), 200


		
		






