from bson.objectid import ObjectId
from base64 import urlsafe_b64encode, urlsafe_b64decode
from flask_login import UserMixin
from datetime import datetime, timedelta
from marshmallow_mongoengine import ModelSchema

from ponos.global_init import hermes, vprofile, ponosapi, app, GenericModel
from ..document import UserSessionSchema

import json
import hashlib
import requests
import random
import string


class Users(GenericModel):
    def __init__(self, args):
        self.__resource = 'users'
        self.__api = vprofile
        self.__args = args
        super().__init__(self.__resource, self.__api, self.__args)


class User(ModelSchema, UserMixin):
    class Meta:
        model = UserSessionSchema

    def __init__(self, accountcode=None, username=None, **kwargs):
        self.__session_token = None
        self.__user = None
        self.__accountcode = accountcode
        self.__username = username
        self.__args = kwargs
        super().__init__()

        if accountcode is not None and username is not None:
            user = vprofile.login_get({'acct_code': accountcode, 'login_name': username})
            if len(user['data']) >= 1:
                self.info = user['data'][0]

    def generate_reset_token(self):
        expiry = datetime.utcnow() + timedelta(days=1)
        data = {"expire_by": expiry}
        reset_token = self.__db.reset_token.insert_one({**self.__user, **data}).inserted_id
        encoded_token = "reset_token:{}".format(str(reset_token)).encode('utf-8')
        encoded_token = urlsafe_b64encode(encoded_token)
        encoded_token = urlsafe_b64encode(encoded_token)
        return encoded_token

    @property
    def info(self):
        return self.__user

    @info.setter
    def info(self, value):
        strip_keys = ('password', 'password_encoding')
        for key in strip_keys:
            value.pop(key)

        self.__user = value

    @classmethod
    def authenticate(cls, accountcode, username, password, ua, ip, device, **kwargs):
        self = cls()
        self.__args = {
            'acct_code': accountcode,
            'auth_provider': 'login',
            'auth_token': '',
            'login_name': username,
            'password': password,
            'user_agent': ua,
            'client_ipaddress': ip,
            'device': device,
            **kwargs
        }
        res = vprofile.authenticate(self.__args)
        if res is not None and res.get('status', None) == 'SUCCESS':
            self.__user = {**res, **self.__args}

            self.__user['expiry'] = datetime.utcnow() + timedelta(hours=1)

            self.__user.pop('password')
            self.__user['group_code'] = accountcode

            res_login = self.get_login()
            if len(res_login) > 0:
                person_uuid = res_login[0]['person_uuid']
                person_ponos = self.get_person_ponos({
                    'uuid': person_uuid,
                    'group_code': accountcode,
                    'person_type': 'WEB'
                })
                person = person_ponos['person']
                if len(person) > 0:
                    self.__user['person'] = person[0]
                else:
                    self.__user['person'] = {'fullname': username.upper()}
            else:
                self.__user['person'] = {'fullname': username.upper()}

            self.__user['last_login'] = datetime.strptime(self.__user['last_login'], '%Y-%m-%dT%H:%M:%S.%fZ')

            self.__session = UserSessionSchema(**self.__user)
            self.__session.save()
            self.__session_token = str(self.__session.id)
            self.__is_authenticated = True
        else:
            self.__is_authenticated = False
        return self

    @classmethod
    def autologin(cls, accountcode, username, ua, ip, device, **kwargs):
        self = cls()
        self.__args = {
            'acct_code': accountcode,
            'auth_provider': 'login',
            'auth_token': '',
            'login_name': username,
            'user_agent': ua,
            'client_ipaddress': ip,
            'device': device,
            **kwargs
        }

        self.__user = self.__args

        self.__user['expiry'] = datetime.utcnow() + timedelta(hours=1)
        self.__user['group_code'] = accountcode

        res_login = self.get_login()
        if len(res_login) > 0:
            person_uuid = res_login[0]['person_uuid']
            person_ponos = self.get_person_ponos({
                'uuid': person_uuid,
                'group_code': accountcode,
                'person_type': 'WEB'
            })
            person = person_ponos['person']
            if len(person) > 0:
                self.__user['person'] = person[0]
            else:
                self.__user['person'] = {'fullname': username.upper()}
        else:
            self.__user['person'] = {'fullname': username.upper()}

        self.__user['last_login'] = datetime.strptime(self.__user['last_login'], '%Y-%m-%dT%H:%M:%SZ')

        self.__session = UserSessionSchema(**self.__user)
        self.__session.save()
        self.__session_token = str(self.__session.id)
        self.__is_authenticated = True

        return self

    def delete_session(self):
        session_id = {'_id': {'$ne': ObjectId(self.__session_token)}}
        filters = [
            {'acct_code': self.__args['acct_code']},
            {'login_name': self.__args['login_name']},
            session_id
        ]
        params = {'$and': filters}
        retval = self.__db.sessions.delete_many(params).deleted_count
        return

    def extend_session(self):
        self.__session.expiry = datetime.utcnow() + timedelta(minutes=20)
        self.__session.save()
        # self.__db.sessions.update_one({'_id': session_id}, {'$set': data})
        return

    def get_id(self):
        return self.__session_token

    def get_branch(self, data):
        branch = Organization(data)
        retval = branch.get_branch()
        if retval['status'] == 'SUCCESS':
            return retval.get('branch')
        else:
            return []

    def get_org(self, data):
        organization = Organization(data)
        retval = organization.get()

        return retval.get('organization')

    def get_login(self):
        args = {
            'acct_code': self.__args['acct_code'],
            'id': self.__user['uuid']
        }
        login = Users(args)
        retval = login.get()
        return retval.get('data')

    def get_person(self, args):
        person = UserPerson(args)
        retval = person.get()
        return retval.get('person')

    def get_person_ponos(self, args):
        person = ponosapi.get('person', args)
        return person

    def get_policy(self):
        args = {
            'acct_code': self.__args['acct_code'],
            'login_uuid': self.__user['uuid']
        }
        policy = UserPolicy(args)
        retval = policy.get()

        return retval

    def get_request_token(self):
        encoded_token = self.__session_token.encode('utf-8')
        return urlsafe_b64encode(encoded_token).decode('utf-8')

    @property
    def is_authenticated(self):
        return self.__is_authenticated

    @property
    def is_exist(self):
        return self.__user is not None

    @classmethod
    def load_session(cls, session_id):
        self = cls()
        self.__session = UserSessionSchema.objects(id=ObjectId(session_id)).first()
        if self.__session is not None:
            self.__user = self.dump(self.__session).data
            self.__is_authenticated = True
            self.__session_token = session_id
        else:
            self = None
        return self

    @classmethod
    def load_session_token(cls, token):
        decoded_token = urlsafe_b64decode(token).decode('utf-8')
        self = cls.load_session(decoded_token)
        return self

    def remove(self):
        session_id = ObjectId(self.__session_token)
        self.__user = UserSessionSchema.objects(id=session_id).delete()

    def remove_token(self):
        self.__db.reset_token.delete_one({'_id': self.__reset_token})

    def update_password(self, password):
        self.__args = {'password': password, 'login_uuid': self.__user['login_uuid']}
        res = vprofile.password_update(self.__args)
        return res

    @classmethod
    def validate_token(cls, accountcode, username, reset_token, **kwargs):
        self = cls()
        token = urlsafe_b64decode(reset_token)
        token = urlsafe_b64decode(token).decode('utf-8')[12:]
        self.__reset_token = ObjectId(token)
        self.__user = self.__db.reset_token.find_one({'_id': self.__reset_token})

        return self


class UserAuthToken(GenericModel):
    def __init__(self, args):
        self.__resource = 'user.auth_token'
        self.__api = vprofile
        self.__args = args
        super().__init__(self.__resource, self.__api, self.__args)


class UserGroup(GenericModel):
    def __init__(self, args):
        self.__resource = 'user.group'
        self.__api = vprofile
        self.__args = args
        super().__init__(self.__resource, self.__api, self.__args)


class UserPerson(GenericModel):
    def __init__(self, args):
        self.__resource = 'user.person'
        self.__api = vprofile
        self.__args = args
        super().__init__(self.__resource, self.__api, self.__args)


class UserParams(GenericModel):
    def __init__(self, args):
        self.__resource = 'user.params'
        self.__api = vprofile
        self.__args = args
        super().__init__(self.__resource, self.__api, self.__args)


class UserPassword(GenericModel):
    def __init__(self, args):
        self.__resource = 'user.password'
        self.__api = vprofile
        self.__args = args
        super().__init__(self.__resource, self.__api, self.__args)


class UserPolicy(GenericModel):
    def __init__(self, args):
        self.__resource = 'user.policy'
        self.__api = vprofile
        self.__args = args
        super().__init__(self.__resource, self.__api, self.__args)


class UserPhoto(GenericModel):
    def __init__(self, args):
        self.__resource = 'person.photo'
        self.__api = ponosapi
        self.__args = args
        super().__init__(self.__resource, self.__api, self.__args)

    def generate_filename(self, file):
        date_now = datetime.now()
        file_random_string = file + ''.join(random.choice(string.digits) for _ in range(5))
        file_random_string = file_random_string + date_now.strftime('%m/%d/%Y, %H:%M:%S')

        key1 = self.generate_key(file_random_string)
        key2 = self.generate_key(key1)
        key3 = self.generate_key(f'{key1}_{key2}')
        filename = f'{key1}_{key2[:-10]}_{key3[:-10]}.jpg'
        key = key1[-6:].upper()
        return filename, key

    def generate_key(self, file):
        m = hashlib.md5()
        m.update(file.encode('utf-8'))
        data = m.hexdigest()
        return data

    def request_file_upload(self, filename, key):
        data = {
            'module_code': 'profile',
            'acct_code': self.__args['acct_code'].lower(),
            'file_type': 'IMAGE',
            'file_class': 'IMAGE',
            'path': f'photo/{filename}',
            'key': key
        }
        res = hermes.save('storage', data)
        storage = res.get('storage', None)
        if storage is not None:
            retval = storage[0].get('request')
        else:
            retval = {}
        return retval

    def upload(self, url, fields, file):
        files = {
            'file': file
        }
        retval = requests.post(url, data=fields, files=files)
        return retval

    def save(self, file_name, key):
        self.__args['photo'] = f'{key}.{file_name}'
        retval = super().save()
        return retval


class UserResume(GenericModel):
    def __init__(self, args):
        self.__resource = 'person.detail'
        self.__api = ponosapi
        self.__args = args
        super().__init__(self.__resource, self.__api, self.__args)

    def generate_filename(self, file):
        date_now = datetime.now()
        file_random_string = file + ''.join(random.choice(string.digits) for _ in range(5))
        file_random_string = file_random_string + date_now.strftime('%m/%d/%Y, %H:%M:%S')

        key1 = self.generate_key(file_random_string)
        key2 = self.generate_key(key1)
        key3 = self.generate_key(f'{key1}_{key2}')
        filename = f'{key1}_{key2[:-10]}_{key3[:-10]}.pdf'
        key = key1[-6:].upper()
        return filename, key

    def generate_key(self, file):
        m = hashlib.md5()
        m.update(file.encode('utf-8'))
        data = m.hexdigest()
        return data

    def request_file_upload(self, filename, key):
        data = {
            'module_code': 'profile',
            'acct_code': self.__args['acct_code'].lower(),
            'file_type': 'RESUME',
            'file_class': 'RESUME',
            'path': f'resume/{filename}',
            'key': key
        }
        res = hermes.save('storage', data)
        storage = res.get('storage', None)
        if storage is not None:
            retval = storage[0].get('request')
        else:
            retval = {}
        return retval

    def upload(self, url, fields, file):
        files = {
            'file': file
        }
        retval = requests.post(url, data=fields, files=files)
        return retval

    def save(self, file_name, key):
        self.__args['field_value'] = f'{key}.{file_name}'
        retval = super().save()
        return retval
