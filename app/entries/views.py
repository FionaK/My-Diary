from flask import Flask, Blueprint, jsonify, request

entries_blueprint = Blueprint('entries', __name__)

#class Entries():

entries_blueprint.route('/api/v2/create_entry/', methods=['POST'])	
def create_entry():
	title=request.get_json()['title']
	entry=request.get_json()['entry']
	username=request.get_json()['username']
	cur.execute("INSERT INTO entries(title,entry,username)VALUES(%s, %s, %s);",(title, entry, username))
	conn.commit()
	return jsonify({'message': 'New entry has been created'}), 200

entries_blueprint.route('/api/v2/display_entry/', methods= ['GET'])
def display_entry():
	cur.execute("SELECT * FROM entries")
	entries=cur.fetchall()

	return jsonify(entries), 200

entries_blueprint.route('/api/v2/single_entry/<int:entryid>', methods= ['GET'])
def single_entry(entryid):
	cur.execute("SELECT * FROM entries WHERE entryid="+str(entryid)+";")
	entry=cur.fetchone()
	conn.commit()
	return jsonify(entry), 200

entries_blueprint.route('/api/v2/delete_entry/<int:entryid>', methods= ['DELETE'])
def delete_entry(entryid):
	cur.execute("SELECT * FROM entries WHERE entryid = '"+str(entryid)+"'")
	user=cur.fetchone()
	if user is not None:
		cur.execute("DELETE FROM entries WHERE entryid='"+str(entryid)+"'")
	else:
		return jsonify({'message':'No user with such an entry exists'}), 401

	conn.commit()
	return jsonify({'message': 'Your entry has been successfully deleted'}), 200

entries_blueprint.route('/api/v2/modify_entry/<int:entryid>', methods= ['PUT'])
def modify_entry(entryid):
	title=request.get_json()['title']
	entry=request.get_json()['entry']
	username=request.get_json()['username']

	cur.execute("UPDATE entries SET title= '"+title+"', entry='"+entry+"' WHERE entryid='"+str(entryid)+"'")
	conn.commit()
	return jsonify({'message': 'Your entry has been modified'}), 200


		
		






