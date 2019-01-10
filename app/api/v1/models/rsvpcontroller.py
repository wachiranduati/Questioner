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
		#check whether such a rsvp exists - bug stories
		# we havent looked for the meetup via its id....hardcode it
		self.id = 1
		for rqField in self.required_fields:
			if rqField not in data:
				self.all_required_fields = False

		if self.all_required_fields == True:
			#check whether expected responses are found
			for self.response in self.accepted_responses:
				if self.response in data['response']:
					self.response_found = True

			if self.response_found == True:
				#another bug this is not a composite value
				data['id'] = (self.user, data['meetup'])
				data['user'] = self.user
				rsrpReservations.append(data)
				#another bug havent retrieved the topic from meetups
				return {
						"status" : 201,
						"data" : [{
						"meetup" : data['meetup'],
						"topic" : String,
						"status": data['response']
						}]}

				

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