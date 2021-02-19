from flask import request
from flask_restful import Resource, reqparse
from flask_login import login_required

from ponos.global_init import app
from .model import License


class LicenseHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('license_name', type=str)
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self, id=None):
        self.__args['group_code'] = app.config['GROUP_CODE']

        if id is not None:
            self.__args['id'] = id

        license = License(self.__args)
        retval = license.get()

        return retval
