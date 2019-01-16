from datetime import datetime

users=[]
class UserController():
    """ This will control all the crud operations that involve Questioner users"""
    def throwUserErrorClash(self, status, Error):
        return {
                    "error": status,
                    "data": [Error]
                }, status
    
    def throwSuccessMessg(self, status, Error):
        return {
                    "status": status,
                    "data": [Error]
                }, status

    def CreateUser(self, data):
    # check whether username/phonenumber exists
        self.user_exists = False
        for self.user in users:
            if self.user['username'] == data['username'] or self.user['phoneNumber'] == data['phoneNumber'] or self.user['email'] == data['email']:
                self.user_exists = True
            
        
        if self.user_exists == False:
            data['id'] = int(len(users)+ 1)
            data['isAdmin'] = False
            data['registered'] = str(
                        datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            users.append(data)
            return {
                "status": 201,
                "data": [{
                    "username": data['username'],
                    "message": "user successfully created"
                }]
            }, 201
        else:
            return self.throwUserErrorClash(409, 'A user with your credentials already exists')

    def RetrieveUsers(self, data):
        self.user_found = False
        for self.user in users:
            if self.user['email'] == data['email'] and self.user['password'] == data['password']:
                self.user_found = True
                break

        if self.user_found == True:
            return {
                        "status": 200,
                        "data": [{
                            "username": self.user['username'],
                            "message": "successfully logged in"
                        }]
                    }, 200
        else:
            return self.throwUserErrorClash(400, "Wrong username/email password combination")

    def RetrieveSingleUser(self, id):
        pass

    def UpdateUser(self, id):
        pass
    
    def DeleteUser(self, id):
        pass