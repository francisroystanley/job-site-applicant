from datetime import datetime, timedelta
from flask import request
from flask_restful import Resource, reqparse
from flask_login import login_required, current_user

from metis.global_init import app, metisapi
from .model import BusinessUnit, BusinessUnitPhoto
from ..organization import Organization
from ..document import BusinessUnitSchema

import re


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
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['organization_id'] = organization_id

        businessunit = BusinessUnit(self.__args)
        retval = businessunit.get()

        # if self.__args['businessunit_code'] is not None:
        #     code = self.__args['businessunit_code']
        # else:
        #     code = ''

        # today = str(datetime.utcnow()).split(' ')
        # regex = re.compile('.*{}.*'.format(code), re.IGNORECASE)
        # businessunit_collection = []
        # businessunit = BusinessUnitSchema.objects(businessunit_code=regex)
        # businessunits_all = BusinessUnitSchema.objects()

        # if len(businessunits_all) == 0:
        #     self.__args.pop('businessunit_code')
        #     retval = metisapi.get('businessunit', self.__args)

        #     if retval is not None and retval.get('status', None) == 'SUCCESS':
        #         for businessunit in retval['businessunit']:
        #             businessunit['bu_id'] = businessunit['id']
        #             businessunit['expiry'] = str(datetime.strptime(today[0] + 'T15:59:59Z', '%Y-%m-%dT%H:%M:%SZ'))
        #             businessunit.pop('id')

        #             business_unit = BusinessUnitSchema(**businessunit)
        #             business_unit.save()

        # if len(businessunit) > 0:
        #     for bu in businessunit:
        #         businessunit_data = {
        #             'id': bu['bu_id'],
        #             'businessunit_code': bu['businessunit_code'],
        #             'businessunit_name': bu['businessunit_name'],
        #             'organization_id': bu['organization_id'],
        #             'logo_image': bu['logo_image'],
        #             'banner_image': bu['banner_image'],
        #             'contact_email': bu['contact_email'],
        #             'contact_number': bu['contact_number'],
        #             'address': bu['address'],
        #             'description': bu['description'],
        #             'created_by': bu['created_by'],
        #             'date_created': bu['date_created'],
        #             'date_updated': bu['date_updated']
        #         }

        #         businessunit_collection.append(businessunit_data)

        #     retval = {
        #         'status': 'SUCCESS',
        #         'businessunit': businessunit_collection,
        #         'total_count': len(businessunit)
        #     }

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
            retval = {'status': 'FAILED'}

            return retval

        self.__args['businessunit_id'] = businessunit_id
        retval = BusinessUnitPhoto(self.__args).get()

        return retval
