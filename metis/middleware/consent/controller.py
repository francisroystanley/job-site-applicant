from flask import request
from flask_restful import Resource, reqparse
from flask_login import login_required, current_user

from metis.global_init import app
from .model import Consent


class ConsentHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('consent_code', type=str)
            self.__reqparse.add_argument('consent_name', type=str)
        self.__args = self.__reqparse.parse_args()

    def get(self):
        self.__args['group_code'] = app.config['GROUP_CODE']

        consent = Consent(self.__args)
        retval = consent.get()

        return retval
