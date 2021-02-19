from ponos.global_init import hermes, GenericModel


class Email(GenericModel):
    def __init__(self, args):
        self.__resource = 'mail'
        self.__api = hermes
        self.__args = args
        super().__init__(self.__resource, self.__api, self.__args)

    def send(self):
        retval = self.__api.save(self.__resource, self.__args)

        return retval
