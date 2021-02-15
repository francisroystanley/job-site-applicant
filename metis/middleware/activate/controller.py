from flask import request
from flask_restful import Resource, reqparse
from flask_login import login_required, current_user, login_user
from ua_parser import user_agent_parser

from metis.global_init import app, limiter
from .model import Activate
from ..user.model import Users, User


class ActivateHandler(Resource):
    decorators = [limiter.limit("3/minute")]

    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__reqparse.add_argument('email', type=str, required=True)
        self.__reqparse.add_argument('code', type=str, required=True)
        self.__reqparse.add_argument('X-Forwarded-For', type=str, dest='ip')
        self.__reqparse.add_argument('User-Agent', type=str, dest='ua', location='headers')
        self.__args = self.__reqparse.parse_args()

    def post(self):
        data = {
            'login_name': self.__args['email'],
            'token': self.__args['code']
        }
        activate = Activate(data)
        retval = activate.activate_login()

        if retval['status'] == 'SUCCESS':
            if self.__args.get('ip', None) is None:
                self.__args['ip'] = request.remote_addr

            device = user_agent_parser.Parse(self.__args['ua'])
            self.__args['device'] = device['os']['family']

            login_data = {
                'login_name': self.__args['email']
            }
            users = Users(login_data)
            login_retval = users.get()

            if login_retval['status'] == 'SUCCESS':
                login_info = {}
                for data in login_retval['data']:

                    login_info['accountcode'] = app.config['GROUP_CODE']
                    login_info['auth_provider'] = 'login'
                    login_info['auth_token'] = ''
                    login_info['username'] = data['login_name']
                    login_info['login_name'] = data['login_name']
                    login_info['ua'] = self.__args['ua']
                    login_info['user_agent'] = self.__args['ua']
                    login_info['client_ipaddress'] = self.__args['ip']
                    login_info['ip'] = self.__args['ip']
                    login_info['device'] = self.__args['device']
                    login_info['uuid'] = data['login_uuid']
                    login_info['account_activated'] = data['is_activated']
                    login_info['last_login'] = data['last_login_date']
                    login_info['password_reset_count'] = data['password_reset_count']
                    login_info['login_params'] = {
                        'acct_code': app.config['GROUP_CODE'],
                        'user_type': 'WEB'
                    }
                    user = User.autologin(**login_info)
                    if user.is_authenticated:
                        login_user(user)

        return retval
