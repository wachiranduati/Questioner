class DataStructureDatabase():
    def __init__(self):
        self.payload = {
            "location": "Kangundo",
            "images": ["https://placeholder.io", "https://placeingine.io"],
            "topic": "Biking to MT longonot",
            "happeningOn": "12-23-2019",
            "Tags": ["bike", "bonding", "cheki maneno"],
            "details": "lorem ipsum and some other mumbo jumbo all foall in here"
        }

        self.incomplete_payload = {
            "location": "Kangundo",
            "images": ["https://placeholder.io", "https://placeingine.io"],
            "topic": "Biking to MT longonot"
        }

        self.longer_payload = {
            "location": "Kangundo",
            "images": ["https://placeholder.io", "https://placeingine.io"],
            "topic": "Biking to MT longonot",
            "geo": ["https://placeholder.io", "https://placeingine.io"],
            "weather": "Biking to MT longonot"
        }

        self.question_payload = {
            "meetup": 1,
            "title": "Can I carry bananas?",
            "body": "I just realized that with the formalities I probably wouldn' be able to carry any other food. Does a banana suffice?",
            "votes": 9
        }

        self.longer_question_payld = {
            "meetup": 1,
            "title": "Who is the next James Bond?",
            "body": "is it true that Idris Elba has been baiting people into believing he's the next James Bond?",
            "votes": 9,
            "name": "Jamusi Kantasai",
            "Age": 23
        }

        self.shorter_question_payld = {
            "meetup": 19,
            "title": "Who is the next James Bond?"
        }

        self.properrsvp_payload = {
            "meetup": 1,
            "response": "yes"
        }

        self.userpayload_success = {
                "firstname" : "Nicholas" 
                ,"lastname" : "Nduati" 
                ,"othername" : "Wachira" 
                ,"email" : "example @ example.com" 
                ,"phoneNumber" : "+254705780775",
                "username" : "toon",
                "password": "34k3kddsole32sld",
                "passwordconfirmation": "34k3kddsole32sld"
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
        return self.longer_question_payld

    def shorter_question_payload(self):
        return self.shorter_question_payld

    def rvsp_payload(self):
        return self.properrsvp_payload

    def good_user_payload(self):
        return self.userpayload_success
