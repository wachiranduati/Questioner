import unittest
from app import create_app
from flask import jsonify, json


class TestAdminEndpoints(unittest.TestCase):

	def setUp(self):
		self.app = create_app("testing")
		self.client = self.app.test_client()

	def test_createmeetup(self):
		self.response_message = self.client.post('api/v1/meetups',
			data=json.dumps(
				{
"id" : 2,
"createdOn" : "12-23-2019",
"location" : "Kangundo",
"images" : ["https://placeholder.io", "https://placeingine.io"],
"topic" : "Biking to MT longonot",
"happeningOn" : "12-23-2019",
"Tags" : ["bike", "bonding", "cheki maneno"]
}
), content_type="application/json")
		self.assertEqual(self.response_message.status_code, 200)

	def tearDown(self):
		self.app = None