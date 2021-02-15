from metis.global_init import metisapi, GenericModel


class License(GenericModel):
    def __init__(self, args):
        self.__resource = 'license'
        self.__api = metisapi
        super().__init__(self.__resource, self.__api, args)
