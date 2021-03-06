from datetime import datetime
from app.api.v1.utils.customrequesthandler import CustomValidationRequestHandler
from app.api.v1.utils.validator import PostedDataValidator


customrqstHndlr = CustomValidationRequestHandler()
validatr = PostedDataValidator()


meetups = []


class MeetUpController():
    """ This class will act as the controller directly working with the meetups"""

    def __init__(self):
        self.required = ['location', 'topic', 'happeningOn', 'Tags', 'details']
        self.all_required_fields_present = True
        self.allchecks = False
        

    def create_meetup(self, data):
        """ Method appends a new meetup to the meetups list"""
        # check whether all required fields are present
        self.topic_exist = False
        for self.requiredField in self.required:
            if self.requiredField not in data:
                self.all_required_fields_present = False
                self.missing_field = self.requiredField
                break

        if self.all_required_fields_present == True:
            for self.meetup in meetups:
                if self.meetup['topic'] in data['topic'] or data['topic'] in self.meetup['topic']:
                    self.topic_exist = True
                    break
        
        if self.topic_exist == False:
            if 'images' in data:
                data['images'] = data['images'][:2]
            data['id'] = int(len(meetups) + 1)
            data['createOn'] = str(
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            meetups.append(data)
            return customrqstHndlr.success_request_made(201, 'The meetup *{}* was created successfully'.format(data['topic']))
        else:
            return customrqstHndlr.custom_request_made(409, 'Sorry the meetup already exists')


    def getone_meetup(self, id):
        self.found = False
        for self.meetup in meetups:
            if self.meetup['id'] == id:
                self.found = True
                return customrqstHndlr.success_request_made(200, [
                    {
                        "id": self.meetup['id'],
                        "topic":self.meetup['topic'],
                        "location":self.meetup['location'],
                        "happeningOn":self.meetup['happeningOn'],
                        "tags": self.meetup['Tags']
                    }
                ])

    def getall_meetups(self):
        return customrqstHndlr.success_request_made(200, meetups)

    def getbyid_meetup(self, id):
        self.found = False
        for self.meetup in meetups:
            if self.meetup['id'] == id:
                self.found = True
                return self.meetup

        if self.found == False:
            return False

    def checkwhethermeetup_exists(self, id):
        self.found = False
        for self.meetup in meetups:
            if self.meetup['id'] == id:
                self.found = True

        if self.found == False:
            return False
        else:
            return True

    def deleteMeetup(self, data):
        self.meetup_located = False
        for self.meetup in meetups:
            if self.meetup['id'] == data['meetup']:
                meetups.remove(self.meetup)
                self.meetup_located = True
                return {
                    "status": 200,
                    "data": [{
                        "meetupid":self.meetup['id'],
                        "topic": self.meetup['topic']
                    }]
                }, 200
        
        if self.meetup_located == False:
            return {
                    "error": 404,
                    "data": ['Record does not exist']
                }, 404
            
