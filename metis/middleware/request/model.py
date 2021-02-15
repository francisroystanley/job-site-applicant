from metis.global_init import metisapi, GenericModel


class Request(GenericModel):
    def __init__(self, args):
        self.__resource = 'request'
        self.__api = metisapi
        super().__init__(self.__resource, self.__api, args)


class RequestAction(GenericModel):
    def __init__(self, args):
        self.__resource = 'request.action'
        self.__api = metisapi
        super().__init__(self.__resource, self.__api, args)
