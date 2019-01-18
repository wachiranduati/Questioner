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

    def test_createmeetup_recursively_data(self):
        self.response_message = self.client.post('api/v1/meetups',
                                                 data=json.dumps(DataStrctPayloads.meetuppayload()), content_type="application/json")
        self.response_message = self.client.post('api/v1/meetups',
                                                 data=json.dumps(DataStrctPayloads.meetuppayload()), content_type="application/json")
        self.assertEqual(self.response_message.status_code, 409)

    def test_createmeetup_topic_switched(self):
        self.response_message = self.client.post('api/v1/meetups',
                                                 data=json.dumps(DataStrctPayloads.meetuppayload()), content_type="application/json")
        DataStrctPayloads.meetuppayload()['title'] = 'Biking to Machakos tomorrow'
        self.response_message = self.client.post('api/v1/meetups',
                                                 data=json.dumps(DataStrctPayloads.meetuppayload()), content_type="application/json")
        self.assertEqual(self.response_message.status_code, 409)
    
    def test_createmeetup_properdata_wrong_method(self):
        self.response_message = self.client.put('api/v1/meetups',
                                                 data=json.dumps(DataStrctPayloads.meetuppayload()), content_type="application/json")
        self.assertEqual(self.response_message.status_code, 405)
        self.response_message = self.client.patch('api/v1/meetups',
                                                 data=json.dumps(DataStrctPayloads.meetuppayload()), content_type="application/json")
        self.assertEqual(self.response_message.status_code, 405)

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
    
    def test_creatmeetup_wrong_instance_location(self):
        self.response_message = self.client.post('api/v1/meetups',
                                                 data=json.dumps(DataStrctPayloads.meetup_wrong_instance()), content_type="application/json")
        self.assertEqual(self.response_message.status_code, 400)
    def test_single_userfield_empty(self):
        self.response_message = self.client.post('api/v1/meetups',
                                                 data=json.dumps(DataStrctPayloads.meetup_wrong_instance()), content_type="application/json")
        self.assertEqual(self.response_message.status_code, 400)

    def test_single_userfield_empty_meetup(self):
        self.response_message = self.client.post('api/v1/meetups',
                                                 data=json.dumps(DataStrctPayloads.meetup_with_empty_field()), content_type="application/json")
        self.assertEqual(self.response_message.status_code, 400)

    def test_single_userfield_delete_meetup(self):
        self.response_message = self.client.delete('api/v1/meetups',
                                                 data=json.dumps(''), content_type="application/json")
        self.assertEqual(self.response_message.status_code, 400)
    
    def test_single_userfield_delete_meetup_string_sent(self):
        self.response_message = self.client.delete('api/v1/meetups',
                                                 data=json.dumps({"meetup":'one'}), content_type="application/json")
        self.assertEqual(self.response_message.status_code, 400)

    def test_single_userfield_delete_meetup_moredata_than_expected(self):
        self.response_message = self.client.delete('api/v1/meetups',
                                                 data=json.dumps({"meetup":1, "user":34}), content_type="application/json")
        self.assertEqual(self.response_message.status_code, 413)
    
    def test_single_userfield_delete_meetup_doest_exist(self):
        self.response_message = self.client.delete('api/v1/meetups',
                                                 data=json.dumps({"meetup":10000000}), content_type="application/json")
        self.assertEqual(self.response_message.status_code, 404)

    

    def tearDown(self):
        self.app = None
