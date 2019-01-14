class CustomValidationRequestHandler():
	def wrong_variable_rule(self, resource):
		return {
				"status" : 400,
				"error" : "The resource at a `/{}` does not seem to exist".format(resource)
				}, 400

	def custom_request_made(self, header, resource):
		return {
					"status" : header,
					"error" : resource
					}, header 

	def custom_request_made_max_min_missing(self, header, fld, max, min):
		return {
					"status" : header,
					"error" : "Error with the request field the {} field should not be longer than {} nor smaller than {} or does not exist".format(fld, max, min)
					}, header 

	def custom_request_missing_field(self, header, resource):
		return {
					"status" : header,
					"error" : "You did not provide any input for the *{}* field. Please fill it and try again".format(resource)
					}, header 

	def success_request_made(self, header, resource):
		return {"status":header,
			"data": resource
			}, header

	def success_create_meetup_admin(self, MeetupData):
		return {
			"topic": MeetupData['topic'],
			"location": MeetupData['location'],
			"happeningOn": MeetupData['happeningOn'],
			"tags" : MeetupData['Tags']
				}
	def user_post_questions_to_meetup(self, questionReceived):
		return {
				"user": questionReceived['createdBy'],
				"meetup": questionReceived['meetup'],
				"title": questionReceived['title'],
				"body": questionReceived['body']
				}