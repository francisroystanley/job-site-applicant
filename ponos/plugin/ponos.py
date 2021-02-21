from requests import Request, Session
from requests.auth import HTTPBasicAuth
from requests.exceptions import Timeout, ReadTimeout

import base64


class PonosApi(object):
    def __init__(self, app):
        self.__app = app
        self.__init_resources()
        if self.__app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.__api_url = app.config['PONOS_API']
        self.__headers = {'x-app-shortname': app.config['PONOS_APPNAME']}
        self.__headers['Content-Type'] = 'application/json'
        self.__auth = HTTPBasicAuth(app.config['PONOS_USER'], app.config['PONOS_PWD'])
        self.__key = app.config['SECRET_KEY']

    def __init_resources(self):
        self.__resources = {
            'branch': '/v1/branch/{id}',
            'businessunit': '/v1/businessunit/{id}',
            'businessunit.photo': '/v1/businessunit/{businessunit_id}/photo/{id}',
            'consent': '/v1/consent/{id}',
            'course': '/v1/course/{id}',
            'department': '/v1/department/{id}',
            'division': '/v1/division/{id}',
            'hiring_manager': '/v1/hiring_manager/{id}',
            'job_ad': '/v1/job_ad/{id}',
            'job_ad_advanced_search': '/v1/job_ad_advanced_search',
            'job_ad.tag': '/v1/job_ad/{id}/search_tag',
            'job_ad_application': '/v1/job_ad_application/{id}',
            'job_ad_application.event': '/v1/job_ad_application/{id}/event',
            'job_ad_application_quick_search': '/v1/job_ad_application_search',
            'job_ad_search_tag': '/v1/job_ad_search_tag',
            'license': '/v1/license/{id}',
            'organization': '/v1/organization/{id}',
            'organization.jobtitle': '/v1/organization/{organization_id}/jobtitle/{id}',
            'person': '/v1/person/{id}',
            'person.affiliation': '/v1/person/{person_id}/affiliation/{id}',
            'person.attachment': '/v1/person/{person_id}/attachment/{id}',
            'person.certificate': '/v1/person/{person_id}/certificate/{id}',
            'person.consent': '/v1/person/{person_id}/consent/{id}',
            'person.detail': '/v1/person/{person_id}/detail/{id}',
            'person.education': '/v1/person/{person_id}/education/{id}',
            'person.identification': '/v1/person/{person_id}/identification/{id}',
            'person.license': '/v1/person/{person_id}/license/{id}',
            'person.photo': '/v1/person/{person_id}/photo',
            'person.portfolio': '/v1/person/{person_id}/portfolio/{id}',
            'person.preference': '/v1/person/{person_id}/preference/{id}',
            'person.skill': '/v1/person/{person_id}/skill/{id}',
            'person.social': '/v1/person/{person_id}/social/{id}',
            'person.training': '/v1/person/{person_id}/training/{id}',
            'person.work_history': '/v1/person/{person_id}/work_history/{id}',
            'place': '/v1/place/{id}',
            'position': '/v1/position/{id}',
            'request': '/v1/request',
            'request.action': '/v1/request/{request_type}/action',
            'school': '/v1/school/{id}',
            'section': '/v1/section/{id}',
            'skill': '/v1/skill/{id}',
            'status': '/v1/status/{id}',
            'status.action': '/v1/status/{status_id}/action/{id}',
            'status_action': '/v1/status_action'
        }

    def encode_id(self, string, key=None):
        if key is None:
            key = self.__key

        encoded_chars = []
        for i in range(len(string)):
            key_c = key[i % len(key)]
            encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
            encoded_chars.append(encoded_c)

        encoded_string = ''.join(encoded_chars)
        encoded = base64.urlsafe_b64encode(encoded_string.encode('utf-8'))

        return encoded.decode('utf-8')

    def decode_id(self, string, key=None):
        if key is None:
            key = self.__key

        if string is None:
            return None

        data_string_array = string.split('+')
        data_string_output_array = []
        for data_string in data_string_array:
            decoded_chars = []
            decoded_string = ''
            try:
                data_string = base64.urlsafe_b64decode(data_string).decode('utf-8')
            except Exception as e:
                self.__app.logger.error('ERR encoding: {}, {}'.format(data_string, e))

                return data_string

            for i in range(len(data_string)):
                key_c = key[i % len(key)]
                encoded_c = chr(abs(ord(data_string[i]) - ord(key_c) % 256))
                decoded_chars.append(encoded_c)

            decoded_string = ''.join(decoded_chars)
            data_string_output_array.append(decoded_string)

        return '+'.join(data_string_output_array)

    def __decode(self, data):
        if isinstance(data, dict):
            items = data.items()
        elif isinstance(data, list):
            items = enumerate(data)
        elif data is None:
            return None

        for key, value in items:
            if isinstance(value, list):
                data[key] = self.__decode(value)
            elif isinstance(value, dict):
                data[key] = self.__decode(value)
            else:
                pass

        if 'id' in data:
            data['id'] = self.decode_id(str(data['id']), self.__key)

        for key in data:
            if isinstance(key, str) and key[-3:] == '_id':
                data[key] = self.decode_id(str(data[key]), self.__key)

        return data

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
                # if ('app_id' in key):
                #     bad_keys.append(key)

        bad_keys = ['group_code', 'app_id']
        for key in bad_keys:
            if key in data:
                data.pop(key)

        for key in strip_keys:
            if key in data:
                data.pop(key)

        if encoded:
            if 'id' in data:
                data['id'] = self.encode_id(str(data['id']), self.__key)

            for key in data:
                if isinstance(key, str) and key[-3:] == '_id':
                    data[key] = self.encode_id(str(data[key]), self.__key)

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
                print(f'{e}')
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
            # Hack for Specific endpoints
            # Need to improve resource responses and error handling
            if 'seat_hold' in url and res.status_code == 404:
                retval = res.json()
            else:
                retval = {
                    'status': 'error',
                    'message': 'Internal error'
                }

        return retval

    def get(self, resource, data=None):
        data = self.__decode(data)
        url = self.__get_url(resource, data)
        self.__headers.pop('Content-Type', None)
        self.__app.logger.debug(data)

        return self.__request('GET', url, params=data)

    def save(self, resource, data=None):
        data = self.__decode(data)
        url = self.__get_url(resource, data)
        self.__app.logger.debug(data)

        return self.__request('POST', url, data=data)

    def update(self, resource, data=None):
        data = self.__decode(data)
        url = self.__get_url(resource, data)
        self.__app.logger.debug(data)

        return self.__request('PATCH', url, data)

    def delete(self, resource, data=None):
        data = self.__decode(data)
        url = self.__get_url(resource, data)
        self.__app.logger.debug(data)

        return self.__request('DELETE', url, data)
