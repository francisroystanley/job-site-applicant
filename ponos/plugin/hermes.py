from requests import Request, Session
from requests.auth import HTTPBasicAuth
from requests.exceptions import Timeout, ReadTimeout


class HermesApi(object):
    def __init__(self, app):
        self.__app = app
        self.__init_resources()
        if self.__app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.__api_url = app.config['HERMES_API']
        self.__headers = {'x-app-shortname': app.config['HERMES_APPNAME']}
        self.__headers['Content-Type'] = 'application/json'
        self.__auth = HTTPBasicAuth(app.config['HERMES_USER'], app.config['HERMES_PWD'])
        self.__key = app.config['SECRET_KEY']

    def __init_resources(self):
        self.__resources = {
            'mail': '/v1/mail',
            'sms': '/v1/sms/{provider}',
            'storage': '/v1/storage',
        }

    def __get_url(self, resource, data, endpoint=None):
        if endpoint is None:
            endpoint = self.__resources.get(resource, None)

        try:
            endpoint = endpoint.format(**data)
        except KeyError:
            endpoint = endpoint.replace('/{id}', '')
            if '{' in endpoint:
                endpoint = self.__get_url(resource, data, endpoint)
                endpoint = endpoint.replace(self.__api_url, '')

        return self.__api_url + endpoint

    def __strip(self, data, strip_keys=[], encoded=True):
        if isinstance(data, dict):
            items = data.items()
        elif isinstance(data, list):
            items = enumerate(data)

        for key, value in items:
            if isinstance(value, list):
                data[key] = self.__strip(value, encoded=encoded)
            elif isinstance(value, dict):
                data[key] = self.__strip(value, encoded=encoded)
            else:
                pass

        bad_keys = ['group_code', 'app_id']
        for key in bad_keys:
            if key in data:
                data.pop(key)

        for key in strip_keys:
            if key in data:
                data.pop(key)

        return data

    def __request(self, method, url, data=None, params=None):
        s = Session()
        req = Request(method, url, params=params, json=data, auth=self.__auth, headers=self.__headers)
        prepped = req.prepare()
        res = s.send(prepped, timeout=30)
        if res.status_code == 200:
            try:
                retval = self.__strip(res.json())
            except (Timeout, ReadTimeout) as e:
                retval = {
                    'status': 'error',
                    'message': 'waited too long'
                }
            except Exception as e:
                retval = {
                    'status': 'error',
                    'message': 'Unexpected error'
                }

        elif res.status_code == 403:
            retval = {
                'status': 'failed',
                'message': 'Already exists'
            }
        elif res.status_code >= 500:
            raise Exception('Internal Error')
        else:
            retval = {
                'status': 'error',
                'message': 'Internal error'
            }

        return retval

    def get(self, resource, data=None):
        url = self.__get_url(resource, data)
        self.__headers.pop('Content-Type', None)
        self.__app.logger.debug(data)

        return self.__request('GET', url, params=data)

    def save(self, resource, data=None):
        url = self.__get_url(resource, data)
        self.__app.logger.debug(data)

        return self.__request('POST', url, data=data)

    def update(self, resource, data=None):
        url = self.__get_url(resource, data)
        self.__app.logger.debug(data)

        return self.__request('PATCH', url, data)

    def delete(self, resource, data=None):
        url = self.__get_url(resource, data)
        self.__app.logger.debug(data)

        return self.__request('DELETE', url, data)
