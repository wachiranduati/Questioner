from flask import Blueprint, request
from flask_restplus import Resource, Api
from app.api.v1.models.meetupscontroller import MeetUpController


admin = Blueprint('api', __name__)
api = Api(admin)

meetupcntrl = MeetUpController()


@api.route('/api/v1/meetups')
class AdminCreateMeetup(Resource):
	def post(self):
		MeetupData = request.get_json()
		if MeetupData:
			PostMeetupState = meetupcntrl.create_meetup(MeetupData)
			if PostMeetupState == True:
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
					"status" : 400,
					"error" : "Please ensure that you provide all the required fields"
					}, 400
		else:
			return {
					"status" : 400,
					"error" : "Please ensure that you provide all the required fields"
					}, 400