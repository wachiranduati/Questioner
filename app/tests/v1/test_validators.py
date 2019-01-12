import unittest
from app import create_app
from app.api.v1.utils.validator import TestValidator


class ValidatorTestSys(unittest.TestCase):
	def setUp(self):
		self.app = create_app("testing")
		self.client = self.app.test_client()
		validt = TestValidator()

	def test_empty(self):
		pass

	def tearDown(self):
		self.app = None