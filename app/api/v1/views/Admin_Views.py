from flask import Blueprint, request
from flask_restplus import Resource, Api
from app.api.v1.models.meetups_dbs import meetups


admin = Blueprint('api', __name__)
api = Api(admin)


@api.route('/api/v1/meetups')
class HelloWorld(Resource):
	def post(self):
		data = request.get_json()
		meetups.append(data)
		return meetups

