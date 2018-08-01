import unittest
import json
import os,sys
sys.path.insert(0, os.path.abspath(".."))
from app import flask_app as app

class Users_TestCase(unittest.TestCase):

	def test_get_user(self):
		tester= app.test_client(self)
		response= tester.get('/api/v2/get_user/', content_type='application/json')
		self.assertEqual(response.status_code, 403)


	def test_login(self):
		tester= app.test_client(self)
		response =tester.get('/api/v2/login/')
		self.assertEqual(tester.post('/api/v2/login',
			json={"username":"fifi","password":"2345"}).status_code, 301)
	def test_login(self):
		tester= app.test_client(self)
		response =tester.get('/api/v2/login/')
		self.assertEqual(tester.post('/api/v2/login/',
			json={"username":"fifi","password":""}).status_code, 401)	
	def test_login(self):
		tester= app.test_client(self)
		response =tester.get('/api/v2/login/')
		self.assertEqual(tester.post('/api/v2/login/',
			json={"username":"","password":"fifi23456"}).status_code, 401)	

	def test_register(self):
		with app.test_client(self) as f:
			response = f.get('/api/v2/register/')
			self.assertEqual(f.post('/api/v2/register',
				json={"name":"fiona","username":"fifi","password":"2345", "repeat_password": "2345", "email":"fko@gmail.com"}).status_code, 301)

	def test_register(self):
		with app.test_client(self) as f:
			response = f.post('/api/v2/register/')
			self.assertEqual(f.post('/api/v2/register/',
				json={"name":"","username":"fifi","password":"2345", "repeat_password": "2345","email":"fko@gmail.com"}).status_code, 406)		
    	def test_register(self):
		with app.test_client(self) as f:
			response = f.post('/api/v2/register/')
			self.assertEqual(f.post('/api/v2/register/',
				json={"name":"fiona","username":"fifi","password":"2345", "repeat_password": "25","email":"fko@gmail.com"}).status_code, 403)	

	def test_logout(self):
		res = app.test_client(self)
		response= res.get('/api/v2/logout/', content_type='application/json')
		self.assertEqual(response.status_code, 200)


		

if __name__ == '__main__':
	unittest.main()
				
