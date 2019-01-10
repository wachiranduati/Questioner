from datetime import datetime

Questions = []

class QuestionsController():
	def __init__(self):
		self.required = ['meetup','title','body','votes']
		self.all_required_fields_present = True
		self.user = 2
		
	def PostQuestion(self, data):
		# Questions.append(data)
		# return Questions
		for self.requiredField in self.required:
			if self.requiredField not in data:
				self.all_required_fields_present = False
				break

		if self.all_required_fields_present == True:
			data['id'] = int(len(Questions) + 1)
			data['createdOn'] = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
			data['createdBy'] = self.user
			Questions.append(data)
			return True
		else:
			return False

	def upvoteQuestion(self, id):
		""" This method should update the question votes value to + 1"""
		self.questionfound = False
		for self.question in Questions:
			if self.question['id'] == id:
				self.questionfound = True
				self.question['votes'] = int(self.question['votes'] + 1)
				return {
						"status" : 202,
						"data" : [{
						"meetup" : self.question['meetup'],
						"title" : self.question['title'],
						"body" : self.question['body'],
						"votes": self.question['votes']
						}]
						}, 202

		if self.questionfound == False:
			return {
					"status" : 404,
					"error" : "sorry but a question with that id does not exist"
					}, 404 

	def downvoteQuestion(self, id):
		""" This method should update the question votes value to + 1"""
		self.questionfound = False
		for self.question in Questions:
			if self.question['id'] == id:
				self.questionfound = True
				self.question['votes'] = int(self.question['votes'] - 1)
				#decided to leave it as such now someone can have a negative vote too yes
				return {
						"status" : 202,
						"data" : [{
						"meetup" : self.question['meetup'],
						"title" : self.question['title'],
						"body" : self.question['body'],
						"votes": self.question['votes']
						}]
						}, 202

		if self.questionfound == False:
			return {
					"status" : 404,
					"error" : "sorry but a question with that id does not exist"
					}, 404 

