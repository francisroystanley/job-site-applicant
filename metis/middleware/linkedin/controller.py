from flask import request, redirect, url_for, current_app
from flask_restful import Resource, reqparse
from flask_login import login_user, current_user
from ua_parser import user_agent_parser

from .model import Auth, UserAuth, Profile


class LinkedInAuthRequestHandler(Resource):
    def get(self):
        url = Auth().get()
        retval = {
            'url': url
        }
        return retval


class LinkedInAuthCallbackHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('code', type=str)
            self.__reqparse.add_argument('state', type=str)
            self.__reqparse.add_argument('X-Forwarded-For', type=str, dest='ip', location='headers')
            self.__reqparse.add_argument('User-Agent', type=str, dest='ua', location='headers')
        self.__args = self.__reqparse.parse_args()

    def get(self):
        retval = {}

        if self.__args.get('code') is None:
            url = url_for('login', src='linkedin', status='failed')
            return redirect(url)

        if self.__args.get('ip', None) is None:
            self.__args['ip'] = request.remote_addr

        device = user_agent_parser.Parse(self.__args['ua'])
        self.__args['device'] = device['os']['family']

        auth = Auth().authenticate(self.__args)
        access_token = auth.get('access_token')
        if access_token is not None:
            profile = Profile(access_token)
            user = profile.get()
            user['src'] = 'linkedin'

            if current_user.is_authenticated:
                retval = url_for('index')
            else:
                login_params = {
                    'acct_code': current_app.config['GROUP_CODE'],
                    'user_type': 'WEB'
                }

                self.__args.pop('code')
                self.__args.pop('state')

                self.__args['id'] = profile.id
                self.__args['accountcode'] = current_app.config['GROUP_CODE']
                self.__args['company_code'] = 'METIS'
                self.__args['user_type'] = 'WEB'
                self.__args['login_params'] = login_params
                this_user = UserAuth.authenticate(**self.__args)
                if this_user.is_authenticated:
                    login_user(this_user)
                    retval = url_for('index', src='linkedin', status='success')
                else:
                    is_registered = this_user.check_is_registered(user['email'])
                    if is_registered:
                        retval = url_for('signin', src='linkedin', status='used', email=user['email'])
                    else:
                        user['code'] = request.args.get('code')
                        retval = url_for('register', **user)
        else:
            retval = url_for('signin', src='linkedin', status='failed')

        return redirect(retval)
