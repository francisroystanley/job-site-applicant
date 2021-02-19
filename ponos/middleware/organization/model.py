from ponos.global_init import ponosapi, GenericModel


class Organization(GenericModel):
    def __init__(self, args):
        self.__resource = 'organization'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class OrganizationJobtitle(GenericModel):
    def __init__(self, args):
        self.__resource = 'organization.jobtitle'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)
