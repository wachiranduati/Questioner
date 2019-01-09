class DataStructureDatabase():
	def __init__(self):
		self.payload = {
		"location" : "Kangundo",
		"images" : ["https://placeholder.io", "https://placeingine.io"],
		"topic" : "Biking to MT longonot",
		"happeningOn" : "12-23-2019",
		"Tags" : ["bike", "bonding", "cheki maneno"],
		"details": "lorem ipsum and some other mumbo jumbo all foall in here"
		}

		self.incomplete_payload = {
		"location" : "Kangundo",
		"images" : ["https://placeholder.io", "https://placeingine.io"],
		"topic" : "Biking to MT longonot"
		}

		self.longer_payload = {
		"location" : "Kangundo",
		"images" : ["https://placeholder.io", "https://placeingine.io"],
		"topic" : "Biking to MT longonot",
		"geo" : ["https://placeholder.io", "https://placeingine.io"],
		"weather" : "Biking to MT longonot"
		}

		self.questionsdbs = [
		{
		"id" : 1,
		"createdOn" : "12-27-2019",
		"createdBy" : 2,
		"meetup" : 19,
		"title" : "Can I carry bananas?",
		"body" : "I just realized that with the formalities I probably wouldn' be able to carry any other food. Does a banana suffice?",
		"votes" : 9
		},{
		"id" : 2,
		"createdOn" : "12-16-2010",
		"createdBy" : 203,
		"meetup" : 11,
		"title" : "How do we get there?",
		"body" : "I just realized that I am totally new in the region..so how do I even get there?",
		"votes" : 21
		}
		,{
		"id" : 3,
		"createdOn" : "13-27-2009",
		"createdBy" : 3,
		"meetup" : 19,
		"title" : "Who are you?",
		"body" : "Not trying to be rude but exactly who are you?",
		"votes" : 9
		}
		,{
		"id" : 4,
		"createdOn" : "12-27-2016",
		"createdBy" : 5,
		"meetup" : 19,
		"title" : "Do I have to come?",
		"body" : "I really don't want to join you guys, do I have to come this time?",
		"votes" : 9
		},
		{
		"id" : 5,
		"createdOn" : "12-27-2012",
		"createdBy" : 72,
		"meetup" : 19,
		"title" : "Who is the next James Bond?",
		"body" : "is it true that Idris Elba has been baiting people into believing he's the next James Bond?",
		"votes" : 9
		}
		]

		self.question_payload = {
		"meetup" : 19,
		"title" : "Who is the next James Bond?",
		"body" : "is it true that Idris Elba has been baiting people into believing he's the next James Bond?",
		"votes" : 9
		}

		self.longer_question_payload = {
		"meetup" : 19,
		"title" : "Who is the next James Bond?",
		"body" : "is it true that Idris Elba has been baiting people into believing he's the next James Bond?",
		"votes" : 9,
		"name": "Jamusi Kantasai",
		"Age": 23
		}

		self.shorter_question_payload = {
		"meetup" : 19,
		"title" : "Who is the next James Bond?"
		}

	def meetuppayload(self):
		return self.payload

	def meetup_incomplete_payload(self):
		return self.incomplete_payload

	def meetup_longer_payload(self):
		return self.longer_payload

	def questionsdb(self):
		return self.questionsdbs

	def questions_payload(self):
		return self.question_payload

	def longer_question_payload(self):
		return self.longer_question_payload

	def shorter_question_payload(self):
		return self.shorter_question_payload