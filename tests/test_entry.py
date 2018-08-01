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
		with app.test_client(self) as tester:
			response = tester.get('/api/v2/create_entry/')
			self.assertEqual(tester.post('api/v2/create_entry/',
				content_type='application/json', 
				headers={'x-access-token':"zsdxgfchgvh"},
			json = {"title":"Happiness thoughts", "entry":"Happiness is addictive"}).status_code, 408)
		with app.test_client(self) as tester:
			response =tester.get('/api/v2/create_entry/')
			self.assertEqual(tester.post('api/v2/create_entry/',
				content_type='application/json', 
				headers={'x-access-token':""},
			json = {"title":"Happiness thoughts", "entry":"Happiness is addictive"}).status_code, 403)							

	def test_display_entry(self):
		self.assertEqual(app.test_client(self).get('/api/v2/display_entry/').status_code, 403)

	def test_single_entry(self):
		tester= app.test_client(self)
		response= tester.get('api/v2/single_entry/4', 
			content_type='application/json', 
			headers={'x-access-token':"zsdxgfchgvh"})
		self.assertEqual(response.status_code, 408)

	def test_single_entry(self):
		tester= app.test_client(self)
		response= tester.get('api/v2/single_entry/4', 
			content_type='application/json', 
			headers={'x-access-token':""})
		self.assertEqual(response.status_code, 403)	
	

	def test_delete_entry(self):
		with app.test_client(self) as k:
			response = k.delete('/api/v2/delete_entry/6', content_type='application/json')
			self.assertEqual(response.status_code, 403)
		with app.test_client(self) as j:
			response = j.delete('/api/v2/delete_entry/5',
			 content_type='application/json',
			headers={'x-access-token':"zsdxgfchgvh"})
			self.assertEqual(response.status_code, 408)

	def test_modify_entry(self):
		with app.test_client(self) as tester:
			response =tester.get('/api/v2/modify_entry/')
			self.assertEqual(tester.put('api/v2/modify_entry/7',
				content_type='application/json', 
				headers={'x-access-token':"zsdxgfchgvh"},
			json = {"title":"Happiness thoughts", "entry":"Happiness is addictive"}).status_code, 408)

	def test_modify_entry(self):
		with app.test_client(self) as tester:
			response =tester.get('/api/v2/modify_entry/')
			self.assertEqual(tester.put('api/v2/modify_entry/7',
				content_type='application/json', 
				headers={'x-access-token':""},
			json = {"title":"Happiness thoughts", "entry":"Happiness is addictive"}).status_code, 403)		
		
			

if __name__ == '__main__':
	unittest.main()


		
		
