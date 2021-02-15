

class GenericModel(object):
    def __init__(self, resource, api, args):
        self.__resource = resource
        self.__api = api
        self.__args = args

    def get(self):
        self.__data = self.__api.get(self.__resource, self.__args)
        return self.__data

    def save(self):
        self.__data = self.__api.save(self.__resource, self.__args)
        return self.__data

    def update(self):
        self.__data = self.__api.update(self.__resource, self.__args)
        return self.__data

    def delete(self):
        self.__data = self.__api.delete(self.__resource, self.__args)
        return self.__data
