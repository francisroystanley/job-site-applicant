from flask_login import login_required, current_user
from flask_restful import Resource, reqparse

from .model import RequestAction
from metis.global_init import limiter


class RequestHandler(Resource):
    decorators = [limiter.limit("2/minute")]

    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__args = self.__reqparse.parse_args()

    @login_required
    def post(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['created_by'] = self.__userdata['login_name']
        self.__args['requested_by'] = self.__userdata['login_name']
        self.__args['request_type'] = "PURGE"
        self.__args['request_subtype'] = "PERSON"
        self.__args['params'] = {'person_id': self.__userdata['person']['id']}

        send_request = RequestAction(self.__args)
        retval = send_request.save()

        return retval
