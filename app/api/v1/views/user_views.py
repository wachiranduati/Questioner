from flask import Blueprint, request
from flask_restplus import Resource, Api
from app.api.v1.models.meetupscontroller import MeetUpController
from app.api.v1.models.questionscontroller import QuestionsController
from app.api.v1.models.rsvpcontroller import RsvController
from app.api.v1.utils.customrequesthandler import CustomValidationRequestHandler
from app.api.v1.utils.validator import PostedDataValidator
from app.api.v1.models.usercontroller import UserController



from datetime import datetime


users = Blueprint('UserApi', __name__)
UserApi = Api(users)

meetupcntrl = MeetUpController()
qstnscntrl = QuestionsController()
rsvpCntr = RsvController()
customrqstHndlr = CustomValidationRequestHandler()
validatr = PostedDataValidator()
userCtnr = UserController()


@UserApi.route('/api/v1/meetups/upcoming')
class getall(Resource):
    def get(self):
        return meetupcntrl.getall_meetups()
    
    def post(self):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def put(self):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')

    def delete(self):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')

    def patch(self):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    

@UserApi.route('/api/v1/meetups/<int:id>')
class getspecific(Resource):
    def get(self, id):
        return meetupcntrl.getone_meetup(id)

    def post(self, id):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def put(self, id):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')

    def delete(self, id):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def patch(self, id):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')


@UserApi.route('/api/v1/meetups/<id>')
class getspecificerrors(Resource):
    def get(self, id):
        return customrqstHndlr.wrong_variable_rule(id)

    def post(self, id):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def put(self, id):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')

    def delete(self, id):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def patch(self, id):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')


@UserApi.route('/api/v1/questions')
class postquestion(Resource):
    def post(self):
        # title body
        questionReceived = request.get_json()
        if questionReceived:
            if validatr.x_in_data('title', questionReceived) and validatr.x_instance_of(questionReceived['title'], str) and not validatr.x_too_large(questionReceived['title'], 50) and not validatr.x_too_small(questionReceived['title'], 5):
                if validatr.x_in_data('body', questionReceived) and validatr.x_instance_of(questionReceived['body'], str) and not validatr.x_too_small(questionReceived['body'], 50):
                    if validatr.x_in_data('meetup', questionReceived) and validatr.x_instance_of(questionReceived['meetup'], int):
                        # code goes in here
                        return qstnscntrl.PostQuestion(questionReceived)
                        # code goes in here
                    else:
                        return customrqstHndlr.custom_request_made(400, 'Error the meetup is either missing or has been supplied not as an integer')
                else:
                    return customrqstHndlr.custom_request_made_max_min_missing(400, 'body', 3000, 50)
            else:
                return customrqstHndlr.custom_request_made_max_min_missing(400, 'title', 50, 5)
        else:
            return customrqstHndlr.custom_request_made(400, 'The request made was empty, Please provide all the necessary fields')

    
    def put(self):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')

    def delete(self):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def patch(self):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')


@UserApi.route('/api/v1/questions/<int:questionid>/upvote')
class patchupvotequestion(Resource):
    def put(self, questionid):
        return qstnscntrl.upvoteQuestion(questionid)

    def post(self, questionid):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def delete(self, questionid):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def patch(self, questionid):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')


@UserApi.route('/api/v1/questions/<questionid>/upvote')
class SpeficicErrorsForUpvoteFunctionality(Resource):
    def get(self, questionid):
        return customrqstHndlr.wrong_variable_rule('question ID')

    def post(self, questionid):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def put(self, questionid):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')

    def delete(self, questionid):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def patch(self, questionid):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')


@UserApi.route('/api/v1/questions/<int:questionid>/downvote')
class patchdownvotequestion(Resource):
    def put(self, questionid):
        return qstnscntrl.downvoteQuestion(questionid)

    def post(self, questionid):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def delete(self, questionid):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def patch(self):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')


@UserApi.route('/api/v1/questions/<questionid>/downvote')
class SpeficicErrorsFordownUpvoteFunctionality(Resource):
    def get(self, questionid):
        return customrqstHndlr.wrong_variable_rule('question ID')

    def post(self, questionid):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def put(self, questionid):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')

    def delete(self, questionid):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def patch(self, questionid):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')


@UserApi.route('/api/v1/meetups/rsvps')
class ShowallRsvps(Resource):
    def get(self):
        return rsvpCntr.showall_rsvps()
    
    def post(self):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def put(self):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')

    def delete(self):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def patch(self):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')


@UserApi.route('/api/v1/meetups/<int:meetupid>/rsvps')
class createMeetupRsvp(Resource):
    def post(self, meetupid):
        # response
        reservationMaking = request.get_json()
        if reservationMaking:
            if validatr.rsvp_response_correct(reservationMaking['response']):
                return rsvpCntr.add_rsvp(meetupid, reservationMaking)
            else:
                return customrqstHndlr.success_request_made(400, "Please check your response again, it can only be /no/ /yes/ or /maybe/")

        else:
            return customrqstHndlr.custom_request_made(400, 'You sent an empty request...Please post the relevant data and try again')

@UserApi.route('/api/v1/users')
class CreateUserAccount(Resource):
    def post(self):
        UserRegDetails = request.get_json()
        if UserRegDetails:
            # insert validator here
            if validatr.x_in_data('firstname', UserRegDetails) and validatr.x_instance_of(UserRegDetails['firstname'], str) and not validatr.x_too_large(UserRegDetails['firstname'], 100) and not validatr.x_too_small(UserRegDetails['firstname'], 1):
                if validatr.x_in_data('lastname', UserRegDetails) and validatr.x_instance_of(UserRegDetails['lastname'], str) and not validatr.x_too_large(UserRegDetails['lastname'], 100) and not validatr.x_too_small(UserRegDetails['lastname'], 1):
                    if validatr.x_in_data('othername', UserRegDetails) and validatr.x_instance_of(UserRegDetails['othername'], str) and not validatr.x_too_large(UserRegDetails['othername'], 100) and not validatr.x_too_small(UserRegDetails['othername'], 1):
                        if validatr.x_in_data('email', UserRegDetails) and validatr.x_instance_of(UserRegDetails['email'], str) and validatr.check_whether_email(UserRegDetails['email']) and not validatr.x_too_large(UserRegDetails['email'], 100) and not validatr.x_too_small(UserRegDetails['email'], 1):
                            if validatr.x_in_data('phoneNumber', UserRegDetails) and validatr.x_instance_of(UserRegDetails['phoneNumber'], str) and not validatr.x_too_large(UserRegDetails['phoneNumber'], 20) and not validatr.x_too_small(UserRegDetails['phoneNumber'], 7):
                                if not validatr.check_space_username(UserRegDetails['username']) and validatr.x_in_data('username', UserRegDetails) and validatr.x_instance_of(UserRegDetails['username'], str) and not validatr.x_too_large(UserRegDetails['username'], 20) and not validatr.x_too_small(UserRegDetails['username'], 2):
                                    if validatr.x_in_data('password', UserRegDetails) and validatr.x_instance_of(UserRegDetails['password'], str) and not validatr.x_too_large(UserRegDetails['password'], 20) and not validatr.x_too_small(UserRegDetails['password'], 7) and validatr.x_in_data('passwordconfirmation', UserRegDetails) and UserRegDetails['password'] == UserRegDetails['passwordconfirmation']:
                                        return userCtnr.CreateUser(UserRegDetails)
                                    else:
                                        return customrqstHndlr.custom_request_made(400, "Please ensure that you're password and passord confirmation match")
                                else:
                                    return customrqstHndlr.custom_request_made_max_min_missing(400, 'username', 20, 2) 
                            else:
                               return customrqstHndlr.custom_request_made_max_min_missing(400, 'phonenumber', 20, 7) 
                        else:
                            return customrqstHndlr.custom_request_made(400, 'Your email did not pass the required checks please review it and try again')
                    else:
                        return customrqstHndlr.custom_request_made_max_min_missing(400, 'othername', 100, 1)
                else:
                    return customrqstHndlr.custom_request_made_max_min_missing(400, 'lastname', 100, 1)
            else:
                return customrqstHndlr.custom_request_made_max_min_missing(400, 'firstname', 100, 1)
            # insert validator here
            
        else:
            return customrqstHndlr.custom_request_made(400, 'You sent an empty request...Please post the relevant data and try again')

    
    def put(self):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')

    def delete(self):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def patch(self):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')

@UserApi.route('/api/v1/users/login')
class UserLogin(Resource):
    def post(self):
        LoginCredentials = request.get_json()
        if LoginCredentials:
            #check for username /email
            if validatr.x_in_data('password', LoginCredentials) and validatr.x_instance_of(LoginCredentials['password'], str) and not validatr.x_too_large(LoginCredentials['password'], 50) and not validatr.x_too_small(LoginCredentials['password'], 7):
                if validatr.x_in_data('email', LoginCredentials) and validatr.x_instance_of(LoginCredentials['email'], str) and validatr.check_whether_email(LoginCredentials['email']) and not validatr.x_too_large(LoginCredentials['email'], 100) and not validatr.x_too_small(LoginCredentials['email'], 7):
                    return userCtnr.RetrieveUsers(LoginCredentials)
                else:
                    return customrqstHndlr.custom_request_made(400, 'email did not pass our validation please review it and try again')
            else:
                return customrqstHndlr.custom_request_made(400, 'Your password looks ood, Please review it and try again')
        else:
            return customrqstHndlr.custom_request_made(400, 'You sent an empty request...Please post the relevant data and try again')
    
    def put(self, id):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')

    def delete(self, id):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')
    
    def patch(self):
        return customrqstHndlr.custom_request_made(405, 'Method not allowed on this endpoint')