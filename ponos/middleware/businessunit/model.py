from ponos.global_init import ponosapi, GenericModel


class BusinessUnit(GenericModel):
    def __init__(self, args):
        self.__resource = 'businessunit'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class BusinessUnitPhoto(GenericModel):
    def __init__(self, args):
        self.__resource = 'businessunit.photo'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)
