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
		tester= app.test_client(self)
		response= tester.get('/api/v2/get_user/', content_type='application/json',
			headers={'x-access-token':"zsdxgfchgvh"},)
		self.assertEqual(response.status_code, 408)


	"""def test_login(self):
		tester= app.test_client(self)
		response =tester.post('/api/v2/login/')
		self.assertEqual(tester.post('/api/v2/login/',content_type='application/json',
		 json={"username":"fifi","password":"2345"}).status_code, 500)"""

	def test_register(self):
		with app.test_client(self) as f:
			response = f.post('/api/v2/register/')
			self.assertEqual(f.post('/api/v2/register',content_type='application/json',
				json={"name":"fiona","username":"fii","password":"2345", "repeat_password": "2345", 
				"email":"fko@gmail.com"}).status_code, 401)

	def test_register(self):
		with app.test_client(self) as f:
			response = f.post('/api/v2/register/')
			self.assertEqual(f.post('/api/v2/register/',content_type='application/json',
				json={"name":"","username":"fifi","password":"2345", "repeat_password": "2345",
				"email":"fko@gmail.com"}).status_code, 406)	

	def test_register(self):
		with app.test_client(self) as f:
			response = f.post('/api/v2/register/')
			self.assertEqual(f.post('/api/v2/register/',content_type='application/json',
				json={"name":"fiona","username":"fifi","password":"2345", "repeat_password": "2345",
				"email":"fkomail.com"}).status_code, 417)
	def test_register(self):
		with app.test_client(self) as f:
			response = f.post('/api/v2/register/')
			self.assertEqual(f.post('/api/v2/register/',content_type='application/json',
				json={"name":"fiona","username":"fifi","password":"2345", "repeat_password": "2345",
				"email":""}).status_code, 406)
	def test_register(self):
		with app.test_client(self) as f:
			response = f.post('/api/v2/register/')
			self.assertEqual(f.post('/api/v2/register/',content_type='application/json',
				json={"name":"fiona","username":"fifi","password":"2345", "repeat_password": "2345",
				"email":"fi@gmail.com"}).status_code, 409)
	def test_register(self):
		with app.test_client(self) as f:
			response = f.post('/api/v2/register/')
			self.assertEqual(f.post('/api/v2/register/',content_type='application/json',
				json={"name":"fiona","username":"fifi","password":"2345", "repeat_password": "2345",
				"email":"fi@gmail.com"}).status_code, 409)				

	def test_register(self):
		with app.test_client(self) as f:
			response = f.post('/api/v2/register/')
			self.assertEqual(f.post('/api/v2/register/',content_type='application/json',
				json={"name":"fiona","username":"fifi","password":"2345", "repeat_password": "25",
				"email":"fko@gmail.com"}).status_code, 403)	

		

if __name__ == '__main__':
	unittest.main()
				
