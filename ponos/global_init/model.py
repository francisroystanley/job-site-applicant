class GenericModel(object):
    def __init__(self, resource, api, args):
        self.__resource = resource
        self.__api = api
        self.__args = args

    def get(self):
        return self.__api.get(self.__resource, self.__args)

    def save(self):
        return self.__api.save(self.__resource, self.__args)

    def update(self):
        return self.__api.update(self.__resource, self.__args)

    def delete(self):
        return self.__api.delete(self.__resource, self.__args)
