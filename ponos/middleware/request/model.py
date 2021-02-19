from ponos.global_init import ponosapi, GenericModel


class Request(GenericModel):
    def __init__(self, args):
        self.__resource = 'request'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class RequestAction(GenericModel):
    def __init__(self, args):
        self.__resource = 'request.action'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)
