class CustomValidationRequestHandler():
	def wrong_variable_rule(self, resource):
		return {
				"status" : 400,
				"error" : "Please provide the proper *{}*".format(resource)
				}, 400

	def custom_request_made(self, header, resource):
		return {
					"status" : header,
					"error" : resource
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
