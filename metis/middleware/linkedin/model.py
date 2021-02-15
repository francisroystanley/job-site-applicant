from flask import url_for
from flask_login import UserMixin
from requests import Request, post
from datetime import datetime, timedelta
from marshmallow_mongoengine import ModelSchema

from metis.global_init import linkedin, vprofile, GenericModel
from ..user.model import User
from ..document import UserSessionSchema


class Auth(object):
    def __init__(self):
        self.host = 'https://www.linkedin.com'
        self.redirect_uri = url_for('linkedinauthcallbackhandler', _external=True, _scheme='https')

    def get(self):
        url = '/oauth/v2/authorization'
        data = {
            'response_type': 'code',
            'client_id': linkedin.client_id,
            'redirect_uri': self.redirect_uri,
            'state': 'foobar',
            'scope': 'r_liteprofile r_basicprofile r_emailaddress',
          }
        req = Request('GET', f'{self.host}{url}', params=data)
        prep = req.prepare()
        retval = f'{self.host}{prep.path_url}'
        return retval

    def authenticate(self, args):
        url = '/oauth/v2/accessToken'
        data = {
            'grant_type': 'authorization_code',
            'code': args['code'],
            'redirect_uri': self.redirect_uri,
            'client_id': linkedin.client_id,
            'client_secret': linkedin.client_secret
        }

        res = post(f'{self.host}{url}', data=data)

        return res.json()


class Profile(object):
    def __init__(self, auth):
        self.__resource = 'profile'
        self.__api = linkedin
        self.__auth = f'Bearer {auth}'

    @property
    def id(self):
        return self._id

    def get(self):
        profile = self.__api.get('profile', {}, auth=self.__auth)
        if profile.get('id') is not None:
            self._id = profile.get('id')
            email = self._get_email()
            retval = {
                'firstname': profile['localizedFirstName'],
                'lastname': profile['localizedLastName'],
                'email': email,
                'key': self._id
            }
        else:
            retval = None
        return retval

    def _get_email(self):
        retval = self.__api.get('email', {}, auth=self.__auth)
        email = None
        for e in retval.get('elements', []):
            if e['primary'] is True and e['type'] == 'EMAIL':
                email = e['handle~']['emailAddress']
        return email


class UserAuth(User):

    @classmethod
    def authenticate(cls, accountcode, id, ua, ip, device, **kwargs):
        self = cls()
        self.__args = {
            'acct_code': accountcode,
            'auth_provider': 'linkedin',
            'auth_token': id,
            'login_name': '',
            'user_agent': ua,
            'client_ipaddress': ip,
            'device': device,
            **kwargs
        }
        self._User__args = self.__args
        res = vprofile.authenticate_token(self.__args)
        if res is not None and res.get('status', None) == 'SUCCESS':
            self._User__user = {**res, **self.__args}

            self._User__user['expiry'] = datetime.utcnow() + timedelta(hours=1)

            self._User__user['group_code'] = accountcode
            res_login = self.get_login()
            if len(res_login) > 0:
                person_uuid = res_login[0]['person_uuid']
                person_metis = self.get_person_metis({'uuid': person_uuid, 'group_code': accountcode})
                person = person_metis['person']
                if len(person) > 0:
                    self._User__user['person'] = person[0]

            self._User__user['last_login'] = datetime.strptime(self._User__user['last_login'], '%Y-%m-%dT%H:%M:%S.%fZ')

            self._User__session = UserSessionSchema(**self._User__user)
            self._User__session.save()
            self._User__session_token = str(self._User__session.id)
            self._User__is_authenticated = True
        else:
            self._User__is_authenticated = False

        return self

    def check_is_registered(self, email):
        args = {
            'acct_code': self.__args['acct_code'],
            'login_name': email
        }

        res = vprofile.get('users', args)
        if res.get('total_count') > 0:
            retval = True
        else:
            retval = False

        return retval
