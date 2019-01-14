from .meetupscontroller import MeetUpController
from app.api.v1.utils.customrequesthandler import CustomValidationRequestHandler


meetupCntrl = MeetUpController()
customrqstHndlr = CustomValidationRequestHandler()


rsrpReservations = []
class RsvController():
    def __init__(self):
        self.user = 2
        self.accepted_responses = ['yes', 'no', 'maybe']
        self.required_fields = ['response']
        self.all_required_fields = True
        self.response_found = False
        # self.required_fields = ['meetup','user','response']

    def add_rsvp(self, id, data):
        self.exists = False
        for rsvpMeetup in rsrpReservations:
            if rsvpMeetup['user'] == self.user:
                self.exists = True
                break

        if self.exists == True:
            return customrqstHndlr.custom_request_made(409, 'Reservation already exists on said meetup')

        else:
            for rqField in self.required_fields:
                if rqField not in data:
                    self.all_required_fields = False
                    self.missing_field = rqField

        if self.all_required_fields == True:
            for self.response in self.accepted_responses:
                if self.response in data['response'].lower():
                    self.response_found = True
                    self.responded_with = self.response

            if self.response_found == True:
                # data['id'] = int(rsrpReservations[-1]['id'] + 1)
                data['id'] = int(len(rsrpReservations) + 1)
                data['user'] = self.user
                meetup = meetupCntrl.getbyid_meetup(id)
                if meetup != False:
                    data['topic'] = meetup['topic']
                    data['meetup'] = id
                    rsrpReservations.append(data)
                    return customrqstHndlr.success_request_made(201, [{
                        "meetup": id,
                        "topic": data['topic'],
                        "status": self.responded_with
                    }])

                else:
                    return customrqstHndlr.custom_request_made(400, 'Meetup with that id does not exist')

            else:
                return customrqstHndlr.custom_request_made(400, 'Please use *yes*, *no* or *maybe* as a response')

        else:
            return customrqstHndlr.custom_request_missing_field(400, self.missing_field)

    def showall_rsvps(self):
        return customrqstHndlr.success_request_made(200, rsrpReservations)