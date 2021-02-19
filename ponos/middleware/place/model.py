from ponos.global_init import ponosapi, GenericModel


class Place(GenericModel):
    def __init__(self, args):
        self.__resource = 'place'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)
