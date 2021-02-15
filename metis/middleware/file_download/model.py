from metis.global_init import hermes, GenericModel

import requests


class File(GenericModel):
    def __init__(self, args):
        self.__resource = 'storage'
        self.__api = hermes
        self.__args = args
        super().__init__(self.__resource, self.__api, self.__args)

    def download(self, path):
        retval = requests.get(path)
        return retval.content

    def upload(self):
        return


class Attachment(File):
    def __init__(self, args):
        self.__args = args
        key, file_name, ext = self.__args['file_name'].split('.')
        self._args = {
            'module_code': 'profile',
            'acct_code': self.__args['acct_code'].lower(),
            'file_type': 'ATTACHMENT',
            'file_class': 'ATTACHMENT',
            'path': f'attachment/{self.__args["file_type"]}/{file_name}.{ext}',
            'key': key
        }
        super().__init__(self._args)

    def get(self):
        retval = super().get()
        self.__url = retval['storage'][0]['request']['url']

        return retval

    def download(self):
        return super().download(self.__url)


class Image(File):
    def __init__(self, args):
        self.__args = args
        if len(self.__args['file_name'].split('.')) > 2:
            key, filename, ext = self.__args['file_name'].split('.')
        else:
            key = '--',
            filename = '--'
            ext = '--'

        self._args = {
            'module_code': 'businessunit',
            'acct_code': self.__args['acct_code'].lower(),
            'file_type': 'IMAGE',
            'file_class': 'IMAGE',
            'path': self.__args['image'] + f'/{filename}.{ext}',
            'key': key
        }
        super().__init__(self._args)

    def get(self):
        retval = super().get()
        if not retval['storage']:
            retval = {
                'status': 'FAILED'
            }
            return retval
        self.__url = retval['storage'][0]['request']['url']

        return retval

    def download(self):
        return super().download(self.__url)


class ProfilePhoto(File):
    def __init__(self, args):
        self.__args = args
        key, filename, ext = self.__args['file_name'].split('.')
        self._args = {
            'module_code': 'profile',
            'acct_code': self.__args['acct_code'].lower(),
            'file_type': 'IMAGE',
            'file_class': 'IMAGE',
            'path': f'photo/{filename}.{ext}',
            'key': key
        }
        super().__init__(self._args)

    def get(self):
        retval = super().get()
        self.__url = retval['storage'][0]['request']['url']

        return retval

    def download(self):
        return super().download(self.__url)


class Resume(File):
    def __init__(self, args):
        self.__args = args
        key, filename, ext = self.__args['file_name'].split('.')
        self._args = {
            'module_code': 'profile',
            'acct_code': self.__args['acct_code'].lower(),
            'file_type': 'RESUME',
            'file_class': 'RESUME',
            'path': f'resume/{filename}.{ext}',
            'key': key
        }
        super().__init__(self._args)

    def get(self):
        retval = super().get()
        self.__url = retval['storage'][0]['request']['url']

        return retval

    def download(self):
        return super().download(self.__url)
