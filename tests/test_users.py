import unittest
import os,sys
sys.path.insert(0, os.path.abspath(".."))
from app import flask_app as app

class Users_TestCase(unittest.TestCase):

	def test_get_user(self):
		tester= app.test_client(self)
		response= tester.get('/api/v2/get_user/', content_type='application/json')
		self.assertEqual(response.status_code, 403)


	def test_login(self):
		test_data = json.dump({
			"username": "fifi",
			"password":"fifi2345"})
		response = self.app.post('api/v2/login/', Content-type='application/json')
		self.assertEqual(response.status_code, 200)

	def test_login_with_wrong_password(self):
		test_data = json.dump({
			"username": "fifi",
			"password":""})
		response = self.app.post('api/v2/login/', Content-type='application/json')
		self.assertEqual(response.status_code, 401)
	
	def test_login_with_wrong_username(self):
		test_data = json.dump({
			"username": "",
			"password":"fifi2345"})
		response = self.app.post('api/v2/login/', Content-type='application/json')
		self.assertEqual(response.status_code, 401)
		

	def test_register(self):
		with app.test_client(self) as f:
			response = f.get('/api/v2/register/')
			self.assertEqual(f.post('/api/v2/register',
				json={"name":"fiona","username":"fifi","password":"2345","email":"fko@gmail.com"}).status_code, 301)

	def test_logout(self):
		res = app.test_client(self)
		response= res.get('/api/v2/logout/', content_type='application/json')
		self.assertEqual(response.status_code, 200)

		
		
	def test_register_with_valid_email(self):
		test_data = json.dump(
			{"name":"fiona", 
			"username":"fifi", 
			"password":"fifi2345", 
			"repeat_password":"fifi2345", 
			"email":"fifi@gmail.com"})
		response = self.app.post('api/v2/register/', Content-type='application/json')
		self.assertEqual(response.status_code, 200)

	def test_register_with_invalid_email(self):
			test_data = json.dump(
			{"name":"fiona", 
			"username":"fifi", 
			"password":"fifi2345", 
			"repeat_password":"fifi2345", 
			"email":"fi.com"})
		response = self.app.post('api/v2/register/', Content-type='application/json')
		self.assertEqual(response.status_code, 406)
		
	def test_register_with_empty_username(self):
		test_data = json.dump(
			{"name":"fiona", 
			"username":"", 
			"password":"fifi2345", 
			"repeat_pasword":"fifi2345", 
			"email":"i.com"})
		response = self.app.post('api/v2/register/', Content-type='application/json')
		self.assertEqual(response.status_code, 406)

	def test_register_with_empty_name(self):
		test_data = json.dump(
			{"name":"", 
			"username":"", 
			"password":"fifi2345", 
			"repeat_password":"fifi2345", 
			"email":"fi.com"})
		response = self.app.post('api/v2/register/', Content-type='application/json')
		self.assertEqual(response.status_code, 406)	
		

if __name__ == '__main__':
	unittest.main()
				
