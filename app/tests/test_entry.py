import unittest
from entries.views import *
import json

class Entries_TestCase (unittest.TestCase):
	def test_home(self):
		tester= app.test_client(self)
		response= tester.get('/api/v2/', content_type='application/json')
		self.assertEqual(response.status_code, 200)

	def test_create_entry(self):
		with app.test_client(self) as tester:
			response =tester.get('/api/v1/create_entry/', content_type='application/json')
			self.assertEqual(response.status_code, 400)
			self.assertEqual(tester.get('api/vi/create_entry').status_code, 404)

	def test_display_entry(self):
		self.assertEqual(app.test_client(self).get('/api/v1/display_entry/').status_code, 200)

	def test_single_entry(self):
		tester= app.test_client(self)
		response= tester.get('api/v2/single_entry/', content_type='application/json')
		self.assertEqual(response.status_code, 200)

	if __name__ == '__main__':
		unittest.run()
		
		
