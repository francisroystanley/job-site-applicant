from metis.global_init import vprofile


class Token(object):
    def __init__(self, args):
        self.__resource = 'token'
        self.__api = vprofile
        self.__args = args

    def get(self):
        self.__token = self.__api.token(self.__args)
        return self.__token
