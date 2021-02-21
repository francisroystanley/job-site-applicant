from datetime import datetime, timedelta
from flask import request
from flask_restful import Resource, reqparse

from ponos.global_init import app, ponosapi
from .model import BusinessUnit, BusinessUnitPhoto
from ..organization import Organization


class BusinessUnitHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('businessunit_code', type=str)

        self.__args = self.__reqparse.parse_args()

    def get(self):
        self.__args['group_code'] = app.config['GROUP_CODE']
        organization_id = 0
        organization = Organization(self.__args).get()
        if organization['status'] == 'SUCCESS' and len(organization['organization']) > 0:
            organization_id = organization['organization'][0]['id']
        else:
            return {'status': 'FAILED'}

        self.__args['organization_id'] = organization_id
        businessunit = BusinessUnit(self.__args)
        retval = businessunit.get()

        return retval


class BusinessUnitPhotoHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('display_ui_code', type=str)

        self.__args = self.__reqparse.parse_args()

    def get(self, businessunit_id=None):
        self.__args['group_code'] = app.config['GROUP_CODE']
        if businessunit_id is None:
            return {'status': 'FAILED'}

        self.__args['businessunit_id'] = businessunit_id
        retval = BusinessUnitPhoto(self.__args).get()

        return retval
