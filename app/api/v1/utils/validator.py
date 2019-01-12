class TestValidator():

	def emptyrequest(self, data):
		if data == None or data == '':
			return True
		else:
			return False

	def meetup_id_provided(self, data):
		if 'meetup' in data:
			return True
		else:
			return False