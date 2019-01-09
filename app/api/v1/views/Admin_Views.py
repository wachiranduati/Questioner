from flask import Blueprint, request
from flask_restplus import Resource, Api
from app.api.v1.models.meetups_dbs import meetups
from datetime import datetime


admin = Blueprint('api', __name__)
api = Api(admin)


@api.route('/api/v1/meetups')
class HelloWorld(Resource):
	def post(self):
		MeetupData = request.get_json()
		if MeetupData != None:
			if len(MeetupData) < 6:
				return {
					"status" : 400,
					"error" : "Please ensure that you provide all the required fields"
					}, 400
			elif len(MeetupData) > 6:
				return {
					"status" : 400,
					"error" : "Your request contains more input that is required"
					}, 400
			else:
				MeetupData['createOn'] = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
				MeetupData['id'] = int(meetups[-1]['id'] + 1)
				meetups.append(MeetupData)
				return {
						"status": 201,
						"data": {
							"topic": MeetupData['topic'],
							"location": MeetupData['location'],
							"happeningOn": MeetupData['happeningOn'],
							"tags" : MeetupData['Tags']
								}

						}, 201	
		else:
			return {
						"status": 400,
						"data": "The request made was empty"

						}, 400	
