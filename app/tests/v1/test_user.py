import unittest
from app import create_app
from flask import jsonify, json

class TestUserEndpoints(unittest.TestCase):
	def setUp(self):
		self.app = create_app("testing")
		self.client = self.app.test_client()

	def test_getall(self):
		assertEqual(2,4)


	def tearDown(self):
		self.app = None