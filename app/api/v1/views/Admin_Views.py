from flask import Blueprint, request
from flask_restplus import Resource, Api
from app.api.v1.models.meetupscontroller import MeetUpController
from app.api.v1.utils.customrequesthandler import CustomValidationRequestHandler
from app.api.v1.utils.validator import PostedDataValidator


admin = Blueprint('api', __name__)
api = Api(admin)

meetupcntrl = MeetUpController()
customrqstHndlr = CustomValidationRequestHandler()
validatr = PostedDataValidator()


@api.route('/api/v1/meetups')
class AdminCreateMeetup(Resource):
    def post(self):
        MeetupData = request.get_json()
        if MeetupData:
            # location images topics happeningOn tags details

            if validatr.x_in_data('location', MeetupData) and validatr.x_instance_of(MeetupData['location'], str) and not validatr.x_too_large(MeetupData['location'], 100) and not validatr.x_too_small(MeetupData['location'], 4):
                if validatr.x_in_data('topic', MeetupData) and validatr.x_instance_of(MeetupData['topic'], str) and not validatr.x_too_large(MeetupData['topic'], 100) and not validatr.x_too_small(MeetupData['topic'], 5):
                    if validatr.x_in_data('happeningOn', MeetupData) and validatr.x_instance_of(MeetupData['happeningOn'], str) and not validatr.x_too_large(MeetupData['happeningOn'], 25) and not validatr.x_too_small(MeetupData['happeningOn'], 8):
                        if validatr.x_in_data('Tags', MeetupData) and validatr.x_instance_of(MeetupData['Tags'], list) and not validatr.x_too_large(MeetupData['Tags'], 9):
                            if validatr.x_in_data('details', MeetupData) and validatr.x_instance_of(MeetupData['details'], str) and not validatr.x_too_small(MeetupData['details'], 8):
                                # code goes in here
                                return meetupcntrl.create_meetup(MeetupData)
                                # code goes in here
                            else:
                                return customrqstHndlr.custom_request_made_max_min_missing(400, 'details', 3000, 8)
                        else:
                            return customrqstHndlr.custom_request_made_max_min_missing(400, 'Tags', 300, 9)
                    else:
                        return customrqstHndlr.custom_request_made_max_min_missing(400, 'happeningOn', 25, 8)
                else:
                    return customrqstHndlr.custom_request_made_max_min_missing(400, 'topic', 100, 5)
            else:
                return customrqstHndlr.custom_request_made_max_min_missing(400, 'location', 100, 4)

        else:
            return customrqstHndlr.custom_request_made(400, "You didn't send any of the required fields in your request.")
            # location images topic happeningOn tags details

    def get(self):
        return customrqstHndlr.custom_request_made(405, "The get method is not allowed on this route.")
    def put(self):
        return customrqstHndlr.custom_request_made(405, "The put method is not allowed on this route.")
    def patch(self):
        return customrqstHndlr.custom_request_made(405, "The patch method is not allowed on this route.")

@api.route('/api/v1/meetups')
class AdminDeleteMeetup(Resource):
    def delete(self):
        MeetupId = request.get_json()
        if MeetupId:
            if len(MeetupId) == 1:
                if validatr.x_in_data('meetup', MeetupId) and validatr.x_instance_of(MeetupId['meetup'], int):
                    return meetupcntrl.deleteMeetup(MeetupId)
                else:
                    return customrqstHndlr.custom_request_made(400, "Your request data did not pass our validation Please ensure that you have your id as an integer")
            else:
                return customrqstHndlr.custom_request_made(413, "Sorry you're request was aborted, Only the meetup id is expected in this request")
        else:
            return customrqstHndlr.custom_request_made(400, "You didn't send any of the required fields in your request.")
