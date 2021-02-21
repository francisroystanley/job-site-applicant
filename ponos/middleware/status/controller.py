from flask import request
from flask_restful import Resource, reqparse
from flask_login import current_user, login_required

from .model import AllStatusAction, Status, StatusAction


class AllStatusActionHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__reqparse.add_argument('status_code', type=str)
        self.__reqparse.add_argument('status_name', type=str)
        self.__reqparse.add_argument('sequence_number', type=str)
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        status_action = AllStatusAction(self.__args)

        return status_action.get()


class StatusHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__reqparse.add_argument('status_code', type=str)
        self.__reqparse.add_argument('status_name', type=str)
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        if id is not None:
            self.__args['id'] = id

        status = Status(self.__args)

        return status.get()


class StatusActionHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__reqparse.add_argument('status_code', type=str)
        self.__reqparse.add_argument('status_name', type=str)
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self, status_id, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        if status_id is None:
            return {'status': 'FAILED'}

        self.__args['status_id'] = status_id
        if id is not None:
            self.__args['id'] = id

        status = StatusAction(self.__args)

        return status.get()
