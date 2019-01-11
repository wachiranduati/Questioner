import unittest
from app import create_app
from flask import jsonify, json
from app.api.v1.models.meetups_dbs import DataStructureDatabase


DataStrctPayloads = DataStructureDatabase()


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

	def test_userpostquestion_success(self):
		self.response_message = self.client.post('/api/v1/questions',
			data=json.dumps(DataStrctPayloads.questions_payload()), content_type="application/json")
		self.assertEqual(self.response_message.status_code, 400)

	def test_userpostquestion_nodata(self):
		self.response_message = self.client.post('/api/v1/questions',
			data=json.dumps(''), content_type="application/json")
		self.assertEqual(self.response_message.status_code, 400)

	def test_userpostquestion_incompletedata(self):
		self.response_message = self.client.post('/api/v1/questions',
			data=json.dumps(DataStrctPayloads.meetup_incomplete_payload()), content_type="application/json")
		self.assertEqual(self.response_message.status_code, 400)

	def test_userpostquestion_moredata(self):
		self.response_message = self.client.post('/api/v1/questions',
			data=json.dumps(DataStrctPayloads.longer_question_payload), content_type="application/json")
		self.assertEqual(self.response_message.status_code, 400)

	def test_upvotequestionError(self):
		"""  database is empty """
		self.response_message = self.client.put('/api/v1/questions/100000/upvote')
		self.assertEqual(self.response_message.status_code, 404)

	def test_upvotequestionSuccess(self):
		"""  run after successfully creating a question """
		self.response_message = self.client.post('/api/v1/questions',
			data=json.dumps(DataStrctPayloads.questions_payload()), content_type="application/json")
		self.response_message = self.client.put('/api/v1/questions/1/upvote')
		self.assertEqual(self.response_message.status_code, 202)

	def test_downvoteFunctionality(self):
		"""  run after successfully creating a question """
		self.response_message = self.client.post('/api/v1/questions',
			data=json.dumps(DataStrctPayloads.questions_payload()), content_type="application/json")
		self.response_message = self.client.put('/api/v1/questions/1/downvote')
		self.assertEqual(self.response_message.status_code, 202)

	def test_downvotequestionError(self):
		"""  database is empty """
		self.response_message = self.client.put('/api/v1/questions/100000/downvote')
		self.assertEqual(self.response_message.status_code, 404)


	def test_rsvpMeetupRetriveAll(self):
		self.response_message = self.client.get('/api/v1/meetups/rsvps')
		self.assertEqual(self.response_message.status_code, 200)

	def test_rsvpMeetupSendempty(self):
		self.response_message = self.client.post('/api/v1/meetups/1/rsvps',
			data=json.dumps(''), content_type="application/json")
		self.assertEqual(self.response_message.status_code, 400)

	def test_RsvpSuccessCreateEmpty(self):
		"""  run after successfully creating a meetup """
		self.response_message = self.client.post('/api/v1/meetups',
			data=json.dumps(DataStrctPayloads.meetuppayload()), content_type="application/json")
		self.response_message = self.client.post('/api/v1/meetups/1/rsvps',
			data=json.dumps(''), content_type="application/json")
		self.assertEqual(self.response_message.status_code, 400)

	def test_RsvpCreateGoodRequest(self):
		"""  run after successfully creating a meetup """
		self.response_message = self.client.post('/api/v1/meetups',
			data=json.dumps(DataStrctPayloads.meetuppayload()), content_type="application/json")
		self.response_message = self.client.post('/api/v1/meetups/1/rsvps',
			data=json.dumps(DataStrctPayloads.rvsp_payload()), content_type="application/json")
		self.assertEqual(self.response_message.status_code, 201)

	def test_RsvpMultipleCreate(self):
		"""  Try to create multiple reservations on the same meetup with the same user id """
		self.response_message = self.client.post('/api/v1/meetups/1/rsvps',
			data=json.dumps(DataStrctPayloads.rvsp_payload()), content_type="application/json")
		self.response_message = self.client.post('/api/v1/meetups/1/rsvps',
			data=json.dumps(DataStrctPayloads.rvsp_payload()), content_type="application/json")
		self.assertEqual(self.response_message.status_code, 409)


	def tearDown(self):
		self.app = None