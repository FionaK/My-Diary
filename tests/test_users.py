import unittest
import os,sys
sys.path.insert(0, os.path.abspath(".."))
from app import flask_app as app

class Users_TestCase(unittest.TestCase):

	def get_user(self):
		tester= app.test_client(self)
		response= tester.get('/api/v2/get_user/', content_type='application/json')
		self.assertEqual(response.status_code, 200)


	def test_login(self):
		tester= app.test_client(self)
		response = tester.get('/api/v1/login/')
		
		self.assertEqual(tester.post('/api/v2/login/', 
			json={"username":"fifi","password":"2345"}).status_code, 401)

	def test_register(self):
		with app.test_client(self) as f:
			response = f.get('/api/v2/register/')
			self.assertEqual(f.post('/api/v2/register',
				json={"name":"fiona","username":"fifi","password":"2345","email":"fko@gmail.com"}).status_code, 301)
		

if __name__ == '__main__':
	unittest.main()
				
