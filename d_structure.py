from flask import Flask, jsonify, request

app=Flask(__name__)


details={}
entries={}


@app.route('/api/v1/', methods= ['POST','GET'])
def home():
	return jsonify({'message': 'Welcome to my Diary'})

@app.route('/api/v1/register/', methods= ['POST', 'GET'])
def register():
	name=request.get_json()['name']
	username=request.get_json()['username']
	password=request.get_json()['password']
	email=request.get_json()['email']
	if username in details:
		return jsonify ({"message": "username exists"})
	else:
		details.update({username:{"name":name,"email":email,"pass_wd":password}})
		return jsonify({"message": "successfully registered"}), 200 

@app.route('/api/v1/login/', methods= ['POST', 'GET'])
def login():
	username=request.get_json()['username']
	password=request.get_json()['password']
	
	if username in details:
		if password==details[username]["pass_wd"]:
			
			return jsonify({"message":"Login successful"})
		else:
			return jsonify({'message': "Incorrect password"})
	else:
		return jsonify({'message':"Invalid Username"}), 200
		

@app.route('/api/v1/create_entry/', methods= ['POST', 'GET'])
def create_entry():
	title=request.get_json()['title']
	entry=request.get_json()['entry']
	entries.update({len(entries)+1:{title:entry}})
	return jsonify({'message':"New entry has been created successfully"})


@app.route('/api/v1/display_entry/', methods= ['GET'])
def display_entry():

	return jsonify(entries)


@app.route('/api/v1/single_entry/<int:entryid>', methods=['GET'])	
def single_entry(entryid):
		return jsonify (entries[entryid]), 200


@app.route('/api/v1/delete_entry/<int:entryid>', methods=['DELETE'])
def delete_entry(entryid):
	del entries[entryid]
	return jsonify ({"message": "your entry has been deleted"})

@app.route('/api/v1/modify_entry/<int:entryid>', methods= ['PUT'])
def modify_entry(entryid):
	title=request.get_json()['title']
	entry=request.get_json()['entry']
	del entries[entryid]
	entries.update({entryid:{title:entry}})

	return jsonify (entries), 200

@app.route('/api/v1/get_user/', methods=['GET'])
def get_user():
 
	return jsonify(details), 200



if __name__	== '__main__':
	app.run(debug=True)









