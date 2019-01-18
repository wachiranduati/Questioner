from datetime import datetime
from app.api.v1.utils.validator import PostedDataValidator
from app.api.v1.utils.customrequesthandler import CustomValidationRequestHandler
from .meetupscontroller import MeetUpController


validtr = PostedDataValidator()
customrqstHndlr = CustomValidationRequestHandler()
meetupCntrl = MeetUpController()


Questions = []


class QuestionsController():
    def __init__(self):
        self.required = ['meetup', 'title', 'body']
        self.all_required_fields_present = True
        self.user = 2
        self.user_posted_same = False

    def PostQuestion(self, data):
        # return Questions
        if meetupCntrl.checkwhethermeetup_exists(data['meetup']) == True:
            for self.requiredField in self.required:
                if self.requiredField not in data:
                    self.all_required_fields_present = False
                    break
            # check whether exact question exists from the same user
            if self.all_required_fields_present == True:
                for self.question in Questions:
                    if self.question['body'] == data['body'] and self.question['createdBy'] == self.user:
                        self.user_posted_same = True
                        break

            if self.user_posted_same == True:
                return customrqstHndlr.custom_request_made(409, 'Sorry you already asked the same question before') 
            else:
                data['id'] = int(len(Questions) + 1)
                data['createdOn'] = str(
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                data['createdBy'] = self.user
                data['votes'] = 0
                Questions.append(data)
                return customrqstHndlr.success_request_made(201, customrqstHndlr.user_post_questions_to_meetup(data))

        else:
            return customrqstHndlr.custom_request_made(400,'Error, meetup does not exist')


    def upvoteQuestion(self, id):
        """ This method should update the question votes value to + 1"""
        self.questionfound = False
        for self.question in Questions:
            if self.question['id'] == id:
                self.questionfound = True
                self.question['votes'] = int(self.question['votes'] + 1)
                return {
                    "status": 202,
                    "data": [{
                        "meetup": self.question['meetup'],
                        "title": self.question['title'],
                        "body": self.question['body'],
                        "votes": self.question['votes']
                    }]
                }, 202

        if self.questionfound == False:
            return customrqstHndlr.custom_request_made(404, 'Sorry, the question does not exist')

    def downvoteQuestion(self, id):
        """ This method should update the question votes value to + 1"""
        self.questionfound = False
        for self.question in Questions:
            if self.question['id'] == id:
                self.questionfound = True
                self.question['votes'] = int(self.question['votes'] - 1)
                # decided to leave it as such now someone can have a negative vote too yes
                return {
                    "status": 202,
                    "data": [{
                        "meetup": self.question['meetup'],
                        "title": self.question['title'],
                        "body": self.question['body'],
                        "votes": self.question['votes']
                    }]
                }, 202

        if self.questionfound == False:
            return customrqstHndlr.custom_request_made(404, 'Sorry, the question does not exist')
