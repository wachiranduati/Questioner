from flask import Blueprint, request
from flask_restplus import Resource, Api
from app.api.v1.models.meetupscontroller import MeetUpController
from app.api.v1.models.questionscontroller import QuestionsController
from app.api.v1.models.rsvpcontroller import RsvController
from app.api.v1.utils.customrequesthandler import CustomValidationRequestHandler
from app.api.v1.utils.validator import PostedDataValidator


from datetime import datetime


users = Blueprint('UserApi', __name__)
UserApi = Api(users)

meetupcntrl = MeetUpController()
qstnscntrl = QuestionsController()
rsvpCntr = RsvController()
customrqstHndlr = CustomValidationRequestHandler()
validatr = PostedDataValidator()


@UserApi.route('/api/v1/meetups/upcoming')
class getall(Resource):
	def get(self):
		return meetupcntrl.getall_meetups()

@UserApi.route('/api/v1/meetups/<int:id>')
class getspecific(Resource):
	def get(self,id):
		return meetupcntrl.getone_meetup(id)
		

@UserApi.route('/api/v1/meetups/<id>')
class getspecificerrors(Resource):
	def get(self,id):
		return customrqstHndlr.wrong_variable_rule(id)

@UserApi.route('/api/v1/questions')
class postquestion(Resource):
	def post(self):
		# title body
		questionReceived = request.get_json()
		if questionReceived:
			if validatr.x_in_data('title', questionReceived) and validatr.x_instance_of(questionReceived['title'], str) and not validatr.x_too_large(questionReceived['title'], 50) and not validatr.x_too_small(questionReceived['title'], 5):
				if validatr.x_in_data('body', questionReceived) and validatr.x_instance_of(questionReceived['body'], str) and not validatr.x_too_small(questionReceived['body'], 50):
					# code goes in here
					PostQuestionState = qstnscntrl.PostQuestion(questionReceived)
					if PostQuestionState == True:
						return customrqstHndlr.success_request_made(201, customrqstHndlr.user_post_questions_to_meetup(questionReceived))
					elif PostQuestionState == 'notexist':
						return customrqstHndlr.custom_request_made(400, 'Could not post the question, The meetup does not exist')

					else:
						return customrqstHndlr.custom_request_made(400, 'Please ensure that you filled in all the required fields')
					# code goes in here
				else:
					return customrqstHndlr.custom_request_made_max_min_missing(400, 'body', 3000, 50)
			else:
				return customrqstHndlr.custom_request_made_max_min_missing(400, 'title', 50, 5)
		else:
			return customrqstHndlr.custom_request_made(400, 'The request made was empty, Please provide all the necessary fields')


			
				
		
@UserApi.route('/api/v1/questions/<int:questionid>/upvote')
class patchupvotequestion(Resource):
	def put(self, questionid):
		return qstnscntrl.upvoteQuestion(questionid)


@UserApi.route('/api/v1/questions/<questionid>/upvote')
class SpeficicErrorsForUpvoteFunctionality(Resource):
	def get(self,questionid):
		return customrqstHndlr.wrong_variable_rule('question ID')

@UserApi.route('/api/v1/questions/<int:questionid>/downvote')
class patchdownvotequestion(Resource):
	def put(self, questionid):
		return qstnscntrl.downvoteQuestion(questionid)


@UserApi.route('/api/v1/questions/<questionid>/downvote')
class SpeficicErrorsForUpvoteFunctionality(Resource):
	def get(self,questionid):
		return customrqstHndlr.wrong_variable_rule('question ID')

@UserApi.route('/api/v1/meetups/rsvps')
class ShowallRsvps(Resource):
	def get(self):
		return rsvpCntr.showall_rsvps()

@UserApi.route('/api/v1/meetups/<int:meetupid>/rsvps')
class createMeetupRsvp(Resource):
	def post(self, meetupid):
		# response
		reservationMaking = request.get_json()
		if reservationMaking:
			if validatr.rsvp_response_correct(reservationMaking['response']):
				return rsvpCntr.add_rsvp(meetupid,reservationMaking)
			else:
				return customrqstHndlr.success_request_made(400, "Please check your response again, it can only be /no/ /yes/ or /maybe/")

		else:
			return customrqstHndlr.custom_request_made(400, 'You sent an empty request...Please post the relevant data and try again')