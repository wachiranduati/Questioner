maxminlength = {
	"maxtitle":50,
	"maxbody":1500,
	"mintitle": 20,
	"minbody": 500,
	"maxlocation":100,
	"minlocation":4,
	"maximages":2,
	"maxtopic":100,
	"mintopic":3,
	"minhappeningOn": 8,
	"maxhappeningOn": 25,
	"maxtags": 9 
	}

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

	def title_provided(self, data):
		if 'title' in data:
			return True
		else:
			return False

	def body_provided(self, data):
		if 'body' in data:
			return True
		else:
			return False

	def votes_provided(self, data):
		if 'votes' in data:
			return True
		else:
			return False

	def meetup_instance_of_int(self, data):
		self.state = isinstance(data, int)
		if self.state == True:
			return True
		else:
			return False

	def title_instance_of_str(self, data):
		self.state = isinstance(data, str)
		if self.state == True:
			return True
		else:
			return False

	def body_instance_of_str(self, data):
		self.state = isinstance(data, str)
		if self.state == True:
			return True
		else:
			return False

	def votes_instance_of_str(self, data):
		self.state = isinstance(data, int)
		if self.state == True:
			return True
		else:
			return False

	def title_max_length_reached(self, data):
		if len(data) > maxminlength['maxtitle']:
			return True
		else:
			return False

	def body_max_length_reached(self, data):
		if len(data) > maxminlength['maxbody']:
			return True
		else:
			return False

	def title_min_length_reached(self, data):
		if len(data) < maxminlength['mintitle']:
			return True
		else:
			return False

	def body_min_length_reached(self, data):
		if len(data) < maxminlength['minbody']:
			return True
		else:
			return False



	def location_provided_meetup(self, data):
		if 'location' in data:
			return True
		else:
			return False

	def topic_provided_meetup(self, data):
		if 'topic' in data:
			return True
		else:
			return False

	def happeningOn_provided_meetup(self,data):
		if 'happeningOn' in data:
			return True
		else:
			return False

	def tags_provided_meetup(self,data):
		if 'tags' in data:
			return True
		else:
			return False

	def images_provided_meetup(self, data):
		if 'images' in data:
			return True
		else:
			return False

	def images_is_list(self, data):
		self.state = isinstance(data, list)
		if self.state == True:
			return True
		else:
			return False 

	def topic_is_str(self, data):
		self.state = isinstance(data, str)
		if self.state == True:
			return True
		else:
			return False 

	def happeningOn_is_str(self, data):
		self.state = isinstance(data, str)
		if self.state == True:
			return True
		else:
			return False

	def tags_is_list(self, data):
		self.state = isinstance(data, list)
		if self.state == True:
			return True
		else:
			return False

	def rsv_meetup_provided(self, data):
		if 'meetup' in data:
			return True
		else:
			return False
	def rsv_response_provided(self, data):
		if 'meetup' in data:
			return True
		else:
			return False

	def meetup_location_min_length_reached(self, data):
		if len(data) < maxminlength['minlocation']:
			return True
		else:
			return False

	def meetup_location_max_length_reached(self, data):
		if len(data) > maxminlength['maxlocation']:
			return True
		else:
			return False

	def meetup_images_max_length_reached(self, data):
		if len(data) > maxminlength['maximages']:
			return True
		else:
			return False

	def meetup_topics_min_length_reached(self, data):
		if len(data) < maxminlength['mintopic']:
			return True
		else:
			return False

	def meetup_topics_max_length_reached(self, data):
		if len(data) > maxminlength['maxtopic']:
			return True
		else:
			return False

	def meetup_happeningOn_max_length_reached(self, data):
		if len(data) > maxminlength['maxhappeningOn']:
			return True
		else:
			return False

	def meetup_happeningOn_min_length_reached(self, data):
		if len(data) < maxminlength['minhappeningOn']:
			return True
		else:
			return False

	def meetup_tags_max_length_reached(self, data):
		if len(data) > maxminlength['maxtags']:
			return True
		else:
			return False

	def rsv_response_is_str(self, data):
		rsv_state = isinstance(data, str)
		if rsv_state == True:
			return True
		else:
			return False

	def rsv_meetup_is_int(self, data):
		rsv_state = isinstance(data, int)
		if rsv_state == True:
			return True
		else:
			return False

	def rsvp_response_correct(self, data):
		if data.lower() == 'yes' or data.lower() == 'no' or data.lower() == 'maybe':
			return True
		else:
			return False

