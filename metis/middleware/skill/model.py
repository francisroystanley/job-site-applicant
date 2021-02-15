from metis.global_init import metisapi, GenericModel


class Skill(GenericModel):
    def __init__(self, args):
        self.__resource = 'skill'
        self.__api = metisapi
        super().__init__(self.__resource, self.__api, args)
