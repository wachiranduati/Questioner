import unittest
from app import create_app
from app.api.v1.utils.validator import TestValidator


class ValidatorTestSys(unittest.TestCase):
	def setUp(self):
		self.app = create_app("testing")
		self.client = self.app.test_client()
		self.validt = TestValidator()

		self.missing_meetup = {}
		self.meetup_present = {"meetup":1}

	def test_empty(self):
		resp = self.validt.emptyrequest('something')
		self.assertEqual(resp, False)
		resp = self.validt.emptyrequest('')
		self.assertEqual(resp, True)
		resp = self.validt.emptyrequest(None)
		self.assertEqual(resp, True)

	def test_meetup_present(self):
		resp = self.validt.meetup_id_provided(self.missing_meetup)
		self.assertEqual(resp, False)
		resp = self.validt.meetup_id_provided(self.meetup_present)
		self.assertEqual(resp, True)

	# def test_title_present(self):
	# 	resp = self.validt.


	def tearDown(self):
		self.app = None

#post question
#meetup, title, body, votes

