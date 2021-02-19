from flask import request
from flask_restful import Resource, reqparse
from flask_login import login_required, current_user

from ..document import CitizenshipSchema, ReligionSchema

import re


class CitizenshipHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('citizenship_name', type=str, default='')
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        citizenship_name = self.__args['citizenship_name']
        regex = re.compile('.*{}.*'.format(citizenship_name), re.IGNORECASE)
        citizenship_collection = []
        citizenships = CitizenshipSchema.objects(name=regex)

        for citizenship in citizenships:
            citizenship_data = {
                'code': citizenship['code'],
                'name': citizenship['name']
            }

            citizenship_collection.append(citizenship_data)

        retval = {
            'status': 'SUCCESS',
            'citizenships': citizenship_collection
        }

        return retval


class ReligionHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('religion_name', type=str, default='')
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        religion_name = self.__args['religion_name']
        regex = re.compile('.*{}.*'.format(religion_name), re.IGNORECASE)
        religion_collection = []
        religions = ReligionSchema.objects(name=regex)

        for religion in religions:
            religion_data = {
                'code': religion['code'],
                'name': religion['name']
            }

            religion_collection.append(religion_data)

        retval = {
            'status': 'SUCCESS',
            'religions': religion_collection
        }

        return retval
