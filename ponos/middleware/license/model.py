from ponos.global_init import ponosapi, GenericModel


class License(GenericModel):
    def __init__(self, args):
        self.__resource = 'license'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)
