from datetime import datetime

users=[]
class UserController():
    """ This will control all the crud operations that involve Questioner users"""
    def CreateUser(self, data):
        data['id'] = int(len(users)+ 1)
        data['isAdmin'] = False
        data['registered'] = str(
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        users.append(data)
        return users, 201

    def RetrieveUsers(self):
        pass
    
    def RetrieveSingleUser(self, id):
        pass

    def UpdateUser(self, id):
        pass
    
    def DeleteUser(self, id):
        pass