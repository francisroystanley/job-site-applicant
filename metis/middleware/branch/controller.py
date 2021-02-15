from flask import request
from flask_restful import Resource, reqparse

from metis.global_init import app
from .model import Branch
from ..organization import Organization


class BranchHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('branch_name', type=str)

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
        branch = Branch(self.__args)
        retval = branch.get()

        return retval
