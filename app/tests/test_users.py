import unittest
from diary import *
import json

class Users_TestCase(unittest.TestCase):

    #test login
	def test_login(self):
		tester= app.test_client(self)
		response = tester.get('/api/v1/login/')
		
		self.assertEqual(tester.post('/api/v1/login/', json={"username":"fifi","password":"2345"}).status_code, 200)

	if __name__ == '__main__':
		unittest.run()
				
