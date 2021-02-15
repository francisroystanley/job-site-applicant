from metis.global_init import metisapi, vprofile


class Activate(object):
    def __init__(self, args):
        self.__resource = 'person'
        self.__api = metisapi
        self.__api_vprofile = vprofile
        self.__args = args

    def activate_login(self):
        self.__activate = self.__api_vprofile.activate_login(self.__resource, self.__args)
        return self.__activate
