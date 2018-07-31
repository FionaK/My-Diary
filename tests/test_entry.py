import unittest
import os,sys
sys.path.insert(0, os.path.abspath(".."))
from app import flask_app as app

class EntriesTestCase (unittest.TestCase):
	def test_home(self):
		tester= app.test_client(self)
		response= tester.get('/api/v2/', content_type='application/json')
		self.assertEqual(response.status_code, 200)

	def test_create_entry(self):
		with app.test_client(self) as tester:
			response =tester.get('/api/v2/create_entry/')
			self.assertEqual(tester.post('api/v2/create_entry',
				json = {"title":"Happiness thoughts", "entry":"Happiness is addictive"}).status_code, 301)

	def test_display_entry(self):
		self.assertEqual(app.test_client(self).get('/api/v2/display_entry/').status_code, 403)

	def test_single_entry(self):
		tester= app.test_client(self)
		response= tester.get('api/v2/single_entry/4', 
			content_type='application/json')
		self.assertEqual(response.status_code, 403)

	def test_delete_entry(self):
		with app.test_client(self) as k:
			response = k.get('/api/v2/delete_entry/', content_type='application/json')
			self.assertEqual(response.status_code, 404)

	def test_modify_entry(self):
		t = app.test_client(self)
		response = t.get(
			'api/v2/modify_entry/3'
			,content_type='application/json')
		self.assertEqual(response.status_code, 405)
					
		

if __name__ == '__main__':
	unittest.main()


		
		
