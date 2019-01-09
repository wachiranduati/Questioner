import unittest
from app import create_app
from flask import jsonify, json

class TestUserEndpoints(unittest.TestCase):
	def setUp(self):
		self.app = create_app("testing")
		self.client = self.app.test_client()

	def test_getallmeetups(self):
		self.response_message = self.client.get('/api/v1/meetups/upcoming')
		self.assertEqual(self.response_message.status_code, 200)

	def test_getspecificmeetup_success(self):
		self.response_message = self.client.get('/api/v1/meetups/1')
		self.assertEqual(self.response_message.status_code, 200)

	def test_getspecificmeetup_different_data_type(self):
		self.response_message = self.client.get('/api/v1/meetups/girl')
		self.assertEqual(self.response_message.status_code, 400)
		self.response_message = self.client.get('/api/v1/meetups/2.3')
		self.assertEqual(self.response_message.status_code, 400)
		self.response_message = self.client.get('/api/v1/meetups/girl/boy')
		self.assertEqual(self.response_message.status_code, 400)




	def tearDown(self):
		self.app = None