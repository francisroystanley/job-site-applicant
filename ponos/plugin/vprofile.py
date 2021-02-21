from requests import Request, Session, get, post
from requests.auth import HTTPBasicAuth
from requests.exceptions import Timeout, ReadTimeout

import copy


class VProfile(object):
    def __init__(self, app):
        self.__app = app
        self.__init_resources()
        if self.__app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.__api_url = app.config['VPROFILE_API']
        self.__headers = {'x-app-shortname': app.config['VPROFILE_APPNAME']}
        self.__headers['Content-Type'] = 'application/json'
        self.__auth = HTTPBasicAuth(app.config['VPROFILE_USER'], app.config['VPROFILE_PWD'])
        self.__key = app.config['SECRET_KEY']

    def __init_resources(self):
        self.__resources = {
            'activate_login': '/v1/auth/activate_login',
            'authenticate': '/v1/auth/login',
            'authenticate_auth_token': '/v1/auth/login_auth_token',
            'group': '/v1/group',
            'group.member': '/v1/group/{group_id}/user/{id}',
            'group.policy': '/v1/group/{group_id}/policy/{id}',
            'policy': '/v1/policy/{id}',
            'token': '/v1/login/{login_uuid}/token',
            'users': '/v1/login/{id}',
            'user.auth_token': '/v1/login/{login_uuid}/auth_token',
            'user.group': '/v1/login/{login_uuid}/group',
            'user.params': '/v1/login/{login_uuid}/parameters',
            'user.password': '/v1/login/{login_uuid}/password',
            'user.person': '/v1/person/{person_uuid}',
            'user.policy': '/v1/login/{login_uuid}/policy/{id}'
        }

    def authenticate(self, data):
        resource = 'authenticate'
        data = self.__decode(data)
        url = self.__get_url(resource, data)
        self.__app.logger.debug(data)

        return self.__request('POST', url, data)

    def authenticate_token(self, data):
        resource = 'authenticate_auth_token'
        url = self.__get_url(resource, data)
        self.__app.logger.debug(data)

        return self.__request('POST', url, data)

    def __decode(self, data):
        return data

    def __get_url(self, resource, data, endpoint=None):
        if endpoint is None:
            endpoint = self.__resources.get(resource, None)

        try:
            endpoint = endpoint.format(**data)
        except KeyError:
            endpoint = endpoint.replace('/{id}', '')
            endpoint = endpoint.replace('/{person_uuid}', '')
            if '{' in endpoint:
                endpoint = self.__get_url(resource, data, endpoint)
                endpoint = endpoint.replace(self.__api_url, '')

        return self.__api_url + endpoint

    def __strip(self, data, strip_keys=[]):
        if isinstance(data, dict):
            items = data.items()
        elif isinstance(data, list):
            items = enumerate(data)

        for key, value in items:
            if isinstance(value, list):
                data[key] = self.__strip(value)
            elif isinstance(value, dict):
                data[key] = self.__strip(value)
            else:
                pass
                # if ('app_id' in key):
                #     bad_keys.append(key)

        bad_keys = ['group_code', 'appid']
        for key in bad_keys:
            if key in data:
                data.pop(key)

        for key in strip_keys:
            if key in data:
                data.pop(key)

        return data

    def __request(self, method, url, data=None, params=None):
        s = Session()
        if method in ('GET'):
            headers = copy.copy(self.__headers)
            headers.pop('Content-Type')
        else:
            headers = self.__headers

        req = Request(method, url, params=params, json=data, auth=self.__auth, headers=headers)
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
                self.__app.logger.info(f'{url} Unexpected Error')
                self.__app.logger.info(f'{e}')
                retval = {
                    'status': 'error',
                    'message': 'Unexpected error'
                }

        elif res.status_code == 400:
            try:
                retval = self.__strip(res.json())
            except (Timeout, ReadTimeout) as e:
                retval = {
                    'status': 'error',
                    'message': 'waited too long'
                }
            except Exception as e:
                self.__app.logger.info(f'{url} Unexpected Error')
                self.__app.logger.info(f'{e}')
                retval = {
                    'status': 'error',
                    'message': 'Unexpected error'
                }

        elif res.status_code == 403:
            self.__app.logger.info(f'{res.status_code} {res.text}')
            retval = {
                'status': 'failed',
                'message': 'Already exists'
            }
        else:
            self.__app.logger.info(f'{res.status_code} {res.text}')
            retval = {
                'status': 'error',
                'message': 'Internal error'
            }

        self.__app.logger.info(f'{url} ({res.status_code})')

        return retval

    def activate_login(self, resource, data=None):
        endpoint = self.__resources['activate_login'].format(**data)
        url = '{}{}'.format(self.__api_url, endpoint)
        self.__app.logger.info('Request {}'.format(url))
        res = post(url, json=data, auth=self.__auth, headers=self.__headers, timeout=5)
        try:
            retval = res.json()
        except:
            retval = None

        self.__app.logger.info('Request {}: {}'.format(url, res.status_code))

        return retval

    def token(self, data):
        endpoint = self.__resources['token'].format(**data)
        url = '{}{}'.format(self.__api_url, endpoint)
        self.__app.logger.info('Request {}'.format(url))
        res = get(url, json=data, auth=self.__auth, headers=self.__headers, timeout=5)
        try:
            retval = res.json()
        except:
            retval = None

        self.__app.logger.info('Request {}: {}'.format(url, res.status_code))

        return retval

    def get(self, resource, data=None):
        data = self.__decode(data)
        url = self.__get_url(resource, data)
        self.__app.logger.debug(data)

        return self.__request('GET', url, params=data)

    def save(self, resource, data=None):
        data = self.__decode(data)
        url = self.__get_url(resource, data)

        return self.__request('POST', url, data=data)

    def update(self, resource, data=None):
        data = self.__decode(data)
        url = self.__get_url(resource, data)

        return self.__request('PATCH', url, data)

    def delete(self, resource, data=None):
        data = self.__decode(data)
        url = self.__get_url(resource, data)

        return self.__request('DELETE', url, data)
