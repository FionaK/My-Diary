import unittest
from d_structure import *
import json


class EndpointsTestCase (unittest.TestCase):
	#test home message
	def test_home(self):
		with app.test_client(self) as tester:
			response = tester.get('/api/v1/', content_type='application/json')
			self.assertEqual(response.status_code, 200)

	#test registration
	def test_register(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/register/', content_type='application/json')

		self.assertEqual(response.status_code, 400)

	#test create_entry
	def test_create_entry(self):
		with app.test_client(self) as tester:
			response =tester.get('/api/v1/create_entry/', content_type='application/json')
			self.assertEqual(response.status_code, 400)
			self.assertEqual(tester.get('api/vi/create_entry').status_code, 404)

	#test display_entry
	def test_display_entry(self):
		self.assertEqual(app.test_client(self).get('/api/v1/display_entry/').status_code, 200)


	#test delete entry
	def test_delete_entry(self):
		with app.test_client(self) as tester:
			self.assertEqual(tester.get('/api/v1/delete_entry/4').status_code, 405)

	#test modify entry
	def test_modify_entry(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/modify_entry/')
		self.assertEqual(response.status_code, 404)


	#test get user details
	def test_get_user(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/get_user/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(tester.get('/api/vi/get_user/').status_code, 404)

	# test login
	def test_login(self):
		tester= app.test_client(self)
		response = tester.get('/api/v1/login/')
		self.assertEqual(response.status_code, 500)	
		self.assertEqual(tester.post('/api/v1/login/', json={"username":"fifi","password":"2345"}).status_code, 200)

if __name__	== '__main__':
	app.run(debug=True)








             





