import unittest
from endpoints import *
import json


class EndpointsTestCase (unittest.TestCase):
	#test home message
	def test_home(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/', content_type='application/json')
		self.assertEqual(response.status_code, 200)

	#test registration
	def test_register(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/register/', content_type='application/json'(
			details.update({username:{"name":fifi,"email":fko.com,"pass_wd":1234}})
			))

		self.assertEqual(response.status_code, 200)

	#test create_entry
	def test_create_entry(self):
		tester = app.test_client(self)
		response =tester.get('/api/v1/create_entry/', content_type='application/json'(
			entries.update({len(entries)+1:{title:entry}})
			))

		self.assertEqual(response.status_code, 403)

	#test display_entry
	def test_display_entry(self):
		tester = app.test_client(self)
		response = tester.get('/api/v1/display_entry/', content_type='application/json')
		self.assertEqual(response.status_code, 200)

	#test delete entry
	def test_delete_entry(self):
		tester = app.test_client(self)
		response =





