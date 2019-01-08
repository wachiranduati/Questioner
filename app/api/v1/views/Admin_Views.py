from flask import Blueprint, request
from flask_restplus import Resource, Api
from app.api.v1.models.meetups_dbs import meetups


admin = Blueprint('api', __name__)
api = Api(admin)


@api.route('/api/v1/meetups')
class HelloWorld(Resource):
	def post(self):
		RequiredFields = ['id','createOn','location','images','topic','happeningOn', 'tags']
		FieldsProvided = True
		data = request.get_json()
		if len(data) < 7:
			return {
				"status" : 404,
				"error" : "Please ensure that you provide all the required fields"
				}, 400
		elif len(data) > 7:
			return {
				"status" : 404,
				"error" : "Your request contains more input that is required"
				}, 400
		elif len(data) == 7:
			meetups.append(data)
			return {
					"status": 201,
					"data": data

					}, 201		

