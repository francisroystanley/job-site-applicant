from metis.global_init import metisapi, GenericModel


class Consent(GenericModel):
    def __init__(self, args):
        self.__resource = 'consent'
        self.__api = metisapi
        super().__init__(self.__resource, self.__api, args)
