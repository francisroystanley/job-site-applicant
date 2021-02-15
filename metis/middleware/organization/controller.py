from flask_restful import Resource, reqparse

from metis.global_init import app
from .model import Organization, OrganizationJobtitle


class OrganizationJobtitleHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__args = self.__reqparse.parse_args()

    def get(self, id=None):
        self.__args['group_code'] = app.config['GROUP_CODE']
        organization_id = 0
        if id is None:
            return {'status': 'FAILED'}

        self.__args['id'] = id
        organization = Organization({'group_code': app.config['GROUP_CODE']}).get()
        if organization['status'] != 'SUCCESS' or not organization['organization']:
            return {'status': 'FAILED'}

        organization_id = organization['organization'][0]['id']
        self.__args['organization_id'] = organization_id
        retval = OrganizationJobtitle(self.__args).get()

        return retval
