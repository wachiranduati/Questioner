from .meetupscontroller import MeetUpController

meetupCntrl = MeetUpController()

rsrpReservations = []
class RsvController():
	def __init__(self):
		self.user = 2
		self.accepted_responses = ['yes','no','maybe'] 
		self.required_fields = ['meetup','response']
		self.all_required_fields = True
		self.response_found = False
		# self.required_fields = ['meetup','user','response']
		#we won't check for user since we dont have logins yet// well use a set value of 2

	def add_rsvp(self, id, data):
		#check whether id exists
		self.exists = False
		for rsvpMeetup in rsrpReservations:
			if rsvpMeetup['user'] == self.user and rsvpMeetup['meetup'] == id:
				self.exists = True
				break

		if self.exists == True:
			return {
					"status" : 409,
					"error" : "Reservation already exists on said Meetup"
					}, 409
		else:
			for rqField in self.required_fields:
				if rqField not in data:
					self.all_required_fields = False

		if self.all_required_fields == True:
			#check whether expected responses are found
			for self.response in self.accepted_responses:
				if self.response in data['response']:
					self.response_found = True

			if self.response_found == True:
				# data['id'] = int(rsrpReservations[-1]['id'] + 1)
				data['id'] = int(len(rsrpReservations) + 1)
				data['user'] = self.user
				meetup = meetupCntrl.getbyid_meetup(id)
				if meetup != False:
					data['topic'] = meetup['topic']
					data['meetup'] = id
					rsrpReservations.append(data)
					return {
							"status" : 201,
							"data" : [{
							"meetup" : id,
							"topic" : data['topic'],
							"status": data['response']
							}]}, 201
				else:
					return {
					"status" : 400,
					"error" : "Meetup with that id does not exist"
					}, 400

				

			else:
				return {
					"status" : 400,
					"error" : "Please use YES, NO OR MAYBE as a response"
					}, 400 

		else:
			return {
					"status" : 400,
					"error" : "Please provide all the required fields and try again"
					}, 400 



	def showall_rsvps(self):
		return {"status":200,
				"data": rsrpReservations
				}, 200