import unittest
from app import create_app
from flask import jsonify, json
from app.api.v1.models.meetups_dbs import DataStructureDatabase


DataStrctPayloads = DataStructureDatabase()

class TestAdminEndpoints(unittest.TestCase):

	def setUp(self):
		self.app = create_app("testing")
		self.client = self.app.test_client()

	def test_createmeetup_properdata(self):
		self.response_message = self.client.post('api/v1/meetups',
			data=json.dumps(DataStrctPayloads.meetuppayload()), content_type="application/json")
		self.assertEqual(self.response_message.status_code, 201)

	def test_createmeetup_nodata(self):
		self.response_message = self.client.post('api/v1/meetups',
			data=json.dumps(''), content_type="application/json")
		self.assertEqual(self.response_message.status_code, 400)

	def test_creatmeetup_incompletedata(self):
		self.response_message = self.client.post('api/v1/meetups',
			data=json.dumps(DataStrctPayloads.meetup_incomplete_payload()), content_type="application/json")
		self.assertEqual(self.response_message.status_code, 400)

	def test_creatmeetup_moredata(self):
		self.response_message = self.client.post('api/v1/meetups',
			data=json.dumps(DataStrctPayloads.meetup_longer_payload()), content_type="application/json")
		self.assertEqual(self.response_message.status_code, 400)


	def tearDown(self):
		self.app = None