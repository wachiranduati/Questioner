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

