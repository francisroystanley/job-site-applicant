from ponos.global_init import ponosapi, GenericModel


class Skill(GenericModel):
    def __init__(self, args):
        self.__resource = 'skill'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)
