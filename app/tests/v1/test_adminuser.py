import unittest
from app import create_app


class TestAdminEndpoints(unittest.TestCase):

	def setUp(self):
		self.app = create_app("testing")
		self.client = self.app.test_client()

	def test_createmeetup(self):
		assertEqual(4, 0)

	def tearDown(self):
		self.app = None