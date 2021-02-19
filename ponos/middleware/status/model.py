from ponos.global_init import ponosapi, GenericModel


class AllStatusAction(GenericModel):
    def __init__(self, args):
        self.__resource = 'status_action'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class Status(GenericModel):
    def __init__(self, args):
        self.__resource = 'status'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class StatusAction(GenericModel):
    def __init__(self, args):
        self.__resource = 'status.action'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)
