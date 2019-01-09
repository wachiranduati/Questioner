from flask import Blueprint, request
from flask_restplus import Resource, Api
from app.api.v1.models.meetups_dbs import meetups

from datetime import datetime


users = Blueprint('UserApi', __name__)
UserApi = Api(users)


@UserApi.route('/api/v1/meetups/upcoming')
class getall(Resource):
	def get(self):
		return {"status":200,
				"data":meetups
				}, 200

@UserApi.route('/api/v1/meetups/<int:id>')
class getspecific(Resource):
	def get(self,id):
		for meet_up in meetups:
			if meet_up['id'] == id:
				return {"status":200,
					 "data": [
					 {
					 "id":meet_up['id'],
					 "topic":meet_up['topic'],
					 "location":meet_up['location'],
					 "happeningOn":meet_up['happeningOn'],
					 "tags": meet_up['Tags']
					 }
					 ]
					 }, 200

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
