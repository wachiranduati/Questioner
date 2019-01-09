from flask import Blueprint, request
from flask_restplus import Resource, Api
from app.api.v1.models.meetups_dbs import meetups

from datetime import datetime


users = Blueprint('apius', __name__)
apius = Api(users)


@apius.route('/api/v1/meetups/upcoming')
class getall(Resource):
	def get(self):
		return {"status":200,
				"data":meetups
				}, 200