from flask import Blueprint, request
from flask_restplus import Resource, Api
from app.api.v1.models.meetupscontroller import MeetUpController
from app.api.v1.models.questionscontroller import QuestionsController


from datetime import datetime


users = Blueprint('UserApi', __name__)
UserApi = Api(users)

meetupcntrl = MeetUpController()
qstnscntrl = QuestionsController()


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