maxminlength = {
    "maxtitle": 50,
    "maxbody": 1500,
    "mintitle": 5,
    "minbody": 500,
    "maxlocation": 100,
    "minlocation": 4,
    "maximages": 2,
    "maxtopic": 100,
    "mintopic": 3,
    "minhappeningOn": 8,
    "maxhappeningOn": 25,
    "maxtags": 9
}


class PostedDataValidator():

    def emptyrequest(self, data):
        if data == None or data == '':
            return True
        else:
            return False

    def x_in_data(self, x, data):
        if x in data:
            return True
        else:
            return False

    def x_instance_of(self, x, typ):
        self.state = isinstance(x, typ)
        if self.state == True:
            return True
        else:
            return False

    def x_too_large(self, data, max):
        if len(data) > max:
            return True
        else:
            return False

    def x_too_small(self, data, min):
        if len(data) < min:
            return True
        else:
            return False

    def rsvp_response_correct(self, data):
        if 'yes' in data.lower() or 'no' in data.lower() or 'maybe' in data.lower():
            return True
        else:
            return False

    def all_checks(self, x, data, max, min, typ):
        if self.x_in_data(x, data) == True:
            if self.x_instance_of(data[x], typ) == True:
                if self.x_too_large(data[x], max) == False:
                    if self.x_too_small(data[x], min) == False:
                        return True
                    else:
                        return [False, '{}'.format(x)]
                else:
                    return [False, '{}'.format(x)]
            else:
                return [False, '{}'.format(x)]
        else:
            return [False, '{}'.format(x)]

    # 'location','images','topic','happeningOn','Tags','details'
    # def validateLocation(self,)
