from ponos.global_init import ponosapi, vprofile


class Activate(object):
    def __init__(self, args):
        self.__resource = 'person'
        self.__api = ponosapi
        self.__api_vprofile = vprofile
        self.__args = args

    def activate_login(self):
        return self.__api_vprofile.activate_login(self.__resource, self.__args)
