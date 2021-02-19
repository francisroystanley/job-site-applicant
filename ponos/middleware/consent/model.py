from ponos.global_init import ponosapi, GenericModel


class Consent(GenericModel):
    def __init__(self, args):
        self.__resource = 'consent'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)
