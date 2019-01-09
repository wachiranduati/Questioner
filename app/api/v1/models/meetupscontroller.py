class MeetUpController():
	""" This class will act as the controller directly working with the meetups"""
	def init(self):
		self.meetups = []

	def create_meetup(self, data):
		self.meetups.append(data)

	def getone_meetup(self, id):
		for self.meetup in self.meetups():
			if self.meetup['id'] = id:
				return self.meetup

	def getall_meetups(self):
		return self.meetups