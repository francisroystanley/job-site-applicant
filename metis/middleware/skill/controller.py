from flask import request
from flask_restful import Resource, reqparse
from flask_login import login_required, current_user

from .model import Skill


class SkillHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('skill_name', type=str, default=None)
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']

        skill = Skill(self.__args)
        retval = skill.get()

        return retval
