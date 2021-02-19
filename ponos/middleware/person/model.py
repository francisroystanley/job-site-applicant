from ponos.global_init import hermes, GenericModel, ponosapi
from datetime import datetime

import hashlib
import requests
import random
import string


class Person(GenericModel):
    def __init__(self, args):
        self.__resource = 'person'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class PersonAffiliation(GenericModel):
    def __init__(self, args):
        self.__resource = 'person.affiliation'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class PersonAttachment(GenericModel):
    def __init__(self, args):
        self.__resource = 'person.attachment'
        self.__api = ponosapi
        self.__args = args
        super().__init__(self.__resource, self.__api, self.__args)

    def generate_filename(self, file, ext):
        date_now = datetime.now()
        file_random_string = file + ''.join(random.choice(string.digits) for _ in range(5))
        file_random_string = file_random_string + date_now.strftime('%m/%d/%Y, %H:%M:%S')
        key1 = self.generate_key(file_random_string)
        key2 = self.generate_key(key1)
        key3 = self.generate_key(f'{key1}_{key2}')
        filename = f'{key1}_{key2[:-10]}_{key3[:-10]}.{ext}'
        key = key1[-6:].upper()

        return filename, key

    def generate_key(self, file):
        m = hashlib.md5()
        m.update(file.encode('utf-8'))
        data = m.hexdigest()

        return data

    def request_file_upload(self, filetype, filename, key):
        data = {
            'module_code': 'profile',
            'acct_code': self.__args['acct_code'].lower(),
            'file_type': 'ATTACHMENT',
            'file_class': 'ATTACHMENT',
            'path': f'attachment/{filetype}/{filename}',
            'key': key
        }
        res = hermes.save('storage', data)
        storage = res.get('storage', None)
        if storage is not None:
            retval = storage[0].get('request')
        else:
            retval = {}

        return retval, data['path']

    def upload(self, url, fields, file):
        files = {
            'file': file
        }
        retval = requests.post(url, data=fields, files=files)

        return retval


class PersonCertificate(GenericModel):
    def __init__(self, args):
        self.__resource = 'person.certificate'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class PersonConsent(GenericModel):
    def __init__(self, args):
        self.__resource = 'person.consent'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class PersonDetail(GenericModel):
    def __init__(self, args):
        self.__resource = 'person.detail'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class PersonEducation(GenericModel):
    def __init__(self, args):
        self.__resource = 'person.education'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class PersonIdentification(GenericModel):
    def __init__(self, args):
        self.__resource = 'person.identification'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class PersonLicense(GenericModel):
    def __init__(self, args):
        self.__resource = 'person.license'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class PersonPortfolio(GenericModel):
    def __init__(self, args):
        self.__resource = 'person.portfolio'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class PersonPreference(GenericModel):
    def __init__(self, args):
        self.__resource = 'person.preference'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class PersonSkill(GenericModel):
    def __init__(self, args):
        self.__resource = 'person.skill'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class PersonSocialLink(GenericModel):
    def __init__(self, args):
        self.__resource = 'person.social'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class PersonTraining(GenericModel):
    def __init__(self, args):
        self.__resource = 'person.training'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)


class PersonWorkHistory(GenericModel):
    def __init__(self, args):
        self.__resource = 'person.work_history'
        self.__api = ponosapi
        super().__init__(self.__resource, self.__api, args)
