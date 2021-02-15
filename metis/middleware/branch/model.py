from metis.global_init import metisapi, GenericModel


class Branch(GenericModel):
    def __init__(self, args):
        self.__resource = 'branch'
        self.__api = metisapi
        super().__init__(self.__resource, self.__api, args)
