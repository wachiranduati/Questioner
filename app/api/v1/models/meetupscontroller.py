from datetime import datetime

meetups = []

class MeetUpController():
	""" This class will act as the controller directly working with the meetups"""
	def __init__(self):
		self.required = ['location','images','topic','happeningOn','Tags','details']
		self.all_required_fields_present = True
	

	def create_meetup(self, data):
		""" Method appends a new meetup to the meetups list"""
		#check whether all required fields are present
		for self.requiredField in self.required:
			if self.requiredField not in data:
				self.all_required_fields_present = False
				break

		if self.all_required_fields_present == True:
			data['id'] = int(len(meetups) + 1)
			data['createOn'] = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
			meetups.append(data)
			return True

	def getone_meetup(self, id):
		self.found = False
		for self.meetup in meetups:
			if self.meetup['id'] == id:
				self.found = True
				return {"status":200,
					 "data": [
					 {
					 "id":self.meetup['id'],
					 "topic":self.meetup['topic'],
					 "location":self.meetup['location'],
					 "happeningOn":self.meetup['happeningOn'],
					 "tags": self.meetup['Tags']
					 }
					 ]
					 }, 200

	def getall_meetups(self):
		if len(meetups) >= 1:
			return {"status":200,
				"data": meetups
				}, 200
		