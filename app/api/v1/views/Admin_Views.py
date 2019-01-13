from flask import Blueprint, request
from flask_restplus import Resource, Api
from app.api.v1.models.meetupscontroller import MeetUpController
from app.api.v1.utils.customrequesthandler import CustomValidationRequestHandler



admin = Blueprint('api', __name__)
api = Api(admin)

meetupcntrl = MeetUpController()
customrqstHndlr = CustomValidationRequestHandler()



@api.route('/api/v1/meetups')
class AdminCreateMeetup(Resource):
	def post(self):
		MeetupData = request.get_json()
		if MeetupData:
			PostMeetupState = meetupcntrl.create_meetup(MeetupData)
			if PostMeetupState == True:
				return customrqstHndlr.success_request_made(201, {
							"topic": MeetupData['topic'],
							"location": MeetupData['location'],
							"happeningOn": MeetupData['happeningOn'],
							"tags" : MeetupData['Tags']
								})

				
			else:
				return customrqstHndlr.custom_request_missing_field(400, PostMeetupState[-1])
				
		else:
			return customrqstHndlr.custom_request_made(400, "You didn't send any of the required fields in your request.")