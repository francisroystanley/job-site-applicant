from requests import Request, Session
from requests.exceptions import Timeout, ReadTimeout


class LinkedInApi(object):
    def __init__(self, app):
        self.__app = app
        self.__init_resources()
        self.init_app(app)

    def init_app(self, app):
        self.__api_url = 'https://api.linkedin.com'
        self.__client_id = app.config['LINKEDIN_CLIENT_ID']
        self.__client_secret = app.config['LINKEDIN_CLIENT_SECRET']
        self.__headers = {}

    @property
    def client_id(self):
        return self.__client_id

    @property
    def client_secret(self):
        return self.__client_secret

    def __init_resources(self):
        self.__resources = {
            'profile': '/v2/me',
            'email': '/v2/clientAwareMemberHandles?q=members&projection=(elements*(primary,type,handle~))'
        }

    def __get_url(self, resource, data, endpoint=None):
        if endpoint is None:
            endpoint = self.__resources.get(resource, None)

        try:
            endpoint = endpoint.format(**data)
        except KeyError:
            endpoint = endpoint.replace('/{id}', '')

        return self.__api_url + endpoint

    def __request(self, method, url, data=None, params=None, auth=None):
        s = Session()
        self.__headers['Authorization'] = auth
        self.__app.logger.debug(self.__headers)
        req = Request(method, url, params=params, json=data, headers=self.__headers)
        prepped = req.prepare()

        try:
            res = s.send(prepped, timeout=30)
            retval = res.json()
        except (Timeout, ReadTimeout) as e:
            retval = {
                'status': 'error',
                'message': 'waited too long'
            }
            self.__app.logger.error(e)

        return retval

    def get(self, resource, data=None, auth=None):
        url = self.__get_url(resource, data)
        self.__app.logger.debug(data)
        return self.__request('GET', url, params=data, auth=auth)

    def save(self, resource, data=None, auth=None):
        url = self.__get_url(resource, data)
        self.__app.logger.debug(data)
        return self.__request('POST', url, data=data, auth=auth)
