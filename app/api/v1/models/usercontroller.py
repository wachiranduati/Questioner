from datetime import datetime

users=[]
class UserController():
    """ This will control all the crud operations that involve Questioner users"""
    def throwUserErrorClash(self, status, Error):
        return {
                    "error": status,
                    "data": [Error]
                }, 409
    def CreateUser(self, data):
    # check whether username/phonenumber exists
        for self.user in users:
            if self.user['username'] == data['username']:
                return self.throwUserErrorClash(409, 'A user with the username already exists')
            elif self.user['phoneNumber'] == data['phoneNumber']:
                return self.throwUserErrorClash(409, 'A user with the phoneNumber already exists')
            elif self.user['email'] == data['email']:
                return self.throwUserErrorClash(409, 'A user with the email already exists')
            else:
                data['id'] = int(len(users)+ 1)
                data['isAdmin'] = False
                data['registered'] = str(
                            datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        users.append(data)
        # return data, 201
        return {
            "status": 201,
            "data": [{
                "username": data['username'],
                "message": "user successfully created"
            }]
        }, 201

    def RetrieveUsers(self):
        pass
    
    def RetrieveSingleUser(self, id):
        pass

    def UpdateUser(self, id):
        pass
    
    def DeleteUser(self, id):
        pass