from flask import Blueprint, request
from flask_restplus import Resource, Api
from app.api.v1.models.meetupscontroller import MeetUpController
from app.api.v1.models.questionscontroller import QuestionsController
from app.api.v1.models.rsvpcontroller import RsvController


from datetime import datetime


users = Blueprint('UserApi', __name__)
UserApi = Api(users)

meetupcntrl = MeetUpController()
qstnscntrl = QuestionsController()
rsvpCntr = RsvController()


@UserApi.route('/api/v1/meetups/upcoming')
class getall(Resource):
	def get(self):
		return meetupcntrl.getall_meetups()

@UserApi.route('/api/v1/meetups/<int:id>')
class getspecific(Resource):
	def get(self,id):
		return meetupcntrl.getone_meetup(id)
		

@UserApi.route('/api/v1/meetups/<string:id>')
@UserApi.route('/api/v1/meetups/<float:id>')
@UserApi.route('/api/v1/meetups/<path:id>')
@UserApi.route('/api/v1/meetups/<uuid:id>')
class getspecificerrors(Resource):
	def get(self,id):
		return {
				"status" : 400,
				"error" : "Sorry this route only supports Integers as part of its variable rules"
				}, 400

@UserApi.route('/api/v1/questions')
class postquestion(Resource):
	def post(self):
		questionReceived = request.get_json()
		if questionReceived:
			PostQuestionState = qstnscntrl.PostQuestion(questionReceived)
			if PostQuestionState == True:
				return {
						"status": 201,
						"data": [
							{
							"user": questionReceived['createdBy'],
							"meetup": questionReceived['meetup'],
							"title": questionReceived['title'],
							"body": questionReceived['body']
							}
						]
							},201
			else:
				return {
						"status": 400,
						"data": "The request made incomplete"

						}, 400
		else:
			return {
						"status": 400,
						"data": "The request made was empty"

						},400

@UserApi.route('/api/v1/questions/<int:questionid>/upvote')
class patchupvotequestion(Resource):
	def put(self, questionid):
		return qstnscntrl.upvoteQuestion(questionid)

@UserApi.route('/api/v1/questions/<string:questionid>/upvote')
@UserApi.route('/api/v1/questions/<float:questionid>/upvote')
@UserApi.route('/api/v1/questions/<path:questionid>/upvote')
@UserApi.route('/api/v1/questions/<uuid:questionid>/upvote')
class SpeficicErrorsForUpvoteFunctionality(Resource):
	def get(self,id):
		return {
				"status" : 400,
				"error" : "Sorry this route only supports Integers as part of its variable rules"
				}, 400

@UserApi.route('/api/v1/questions/<int:questionid>/downvote')
class patchdownvotequestion(Resource):
	def put(self, questionid):
		return qstnscntrl.downvoteQuestion(questionid)


@UserApi.route('/api/v1/questions/<string:questionid>/downvote')
@UserApi.route('/api/v1/questions/<float:questionid>/downvote')
@UserApi.route('/api/v1/questions/<path:questionid>/downvote')
@UserApi.route('/api/v1/questions/<uuid:questionid>/downvote')
class SpeficicErrorsForUpvoteFunctionality(Resource):
	def get(self,id):
		return {
				"status" : 400,
				"error" : "Sorry this route only supports Integers as part of its variable rules"
				}, 400

@UserApi.route('/api/v1/meetups/rsvps')
class ShowallRsvps(Resource):
	def get(self):
		return rsvpCntr.showall_rsvps()

@UserApi.route('/api/v1/meetups/<meetupid>/rsvps')
class createMeetupRsvp(Resource):
	def post(self, meetupid):
		reservationMaking = request.get_json()
		return rsvpCntr.add_rsvp(meetupid,reservationMaking)