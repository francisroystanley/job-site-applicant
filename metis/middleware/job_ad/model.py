from metis.global_init import metisapi, GenericModel


class JobAd(GenericModel):
    def __init__(self, args):
        self.__resource = 'job_ad'
        self.__api = metisapi
        super().__init__(self.__resource, self.__api, args)


class JobAdAdvSearch(GenericModel):
    def __init__(self, args):
        self.__resource = 'job_ad_advanced_search'
        self.__api = metisapi
        super().__init__(self.__resource, self.__api, args)


class JobAdApplication(GenericModel):
    def __init__(self, args):
        self.__resource = 'job_ad_application'
        self.__api = metisapi
        super().__init__(self.__resource, self.__api, args)


class JobAdApplicationEvent(GenericModel):
    def __init__(self, args):
        self.__resource = 'job_ad_application.event'
        self.__api = metisapi
        super().__init__(self.__resource, self.__api, args)


class JobAdApplicationQuick(GenericModel):
    def __init__(self, args):
        self.__resource = 'job_ad_application_quick_search'
        self.__api = metisapi
        super().__init__(self.__resource, self.__api, args)


class JobAdSearchTag(GenericModel):
    def __init__(self, args):
        self.__resource = 'job_ad_search_tag'
        self.__api = metisapi
        super().__init__(self.__resource, self.__api, args)


class JobAdTag(GenericModel):
    def __init__(self, args):
        self.__resource = 'job_ad.tag'
        self.__api = metisapi
        super().__init__(self.__resource, self.__api, args)
