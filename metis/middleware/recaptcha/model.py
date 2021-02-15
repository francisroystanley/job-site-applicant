from metis.global_init import app
import requests


class Recaptcha():
    def __init__(self, args):
        self.__host = app.config['GOOGLE_RECAPTCHA_URL']
        self.__auth = ''
        self.__headers = {}
        self.__args = args

    def post(self):
        url = '{}/recaptcha/api/siteverify'.format(self.__host)

        self.__headers['Content-Type'] = 'application/json'

        try:
            res = requests.post(url, params=self.__args, auth=self.__auth, headers=self.__headers)
            res = res.json()
        except requests.packages.urllib3.exceptions.NewConnectionError:
            res = None
        except:
            res = None

        return res
