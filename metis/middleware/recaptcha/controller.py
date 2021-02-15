from flask_restful import Resource, reqparse
from flask import request

from .model import Recaptcha
from metis.global_init import app


class RecaptchaHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('POST'):
            self.__reqparse.add_argument('response', type=str, required=True)
        self.__args = self.__reqparse.parse_args()
        self.__args['group_code'] = app.config['GROUP_CODE']

    def get(self):
        retval = {'client_key': app.config['GOOGLE_RECAPTCHA_CLIENT_KEY']}
        return retval

    def post(self):
        http_stat = 200
        self.__args['key'] = app.config['GOOGLE_RECAPTCHA_KEY']
        data = {
            'response': self.__args['response'],
            'secret': self.__args['key']
        }
        recaptcha = Recaptcha(data)
        res = recaptcha.post()

        if res is not None:
            retval = res
        else:
            retval = {
                'status': 'failed',
                'message': 'Internal Server Error.'
            }
            http_stat = 500

        return retval, http_stat
