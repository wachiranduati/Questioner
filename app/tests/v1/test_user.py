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

	def test_getspecificmeetup(self):
		self.response_message = self.client.get('/api/v1/meetups/upcoming')
		self.assertEqual(self.response_message.status_code, 200)


	def tearDown(self):
		self.app = None