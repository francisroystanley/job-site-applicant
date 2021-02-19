from flask import request, current_app
from flask_restful import Resource, reqparse
from flask_login import login_user, current_user, login_required, logout_user
from ua_parser import user_agent_parser

from ponos.global_init import app, limiter
from ponos.middleware.request import Request
from .model import User, Users, UserGroup, UserParams
from .model import UserPassword, UserPolicy
from .model import UserPhoto, UserResume
from ..person import Person

import werkzeug


class AuthenticateHandler(Resource):
    decorators = [limiter.limit("5/minute")]

    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__reqparse.add_argument('username', type=str, required=True)
        self.__reqparse.add_argument('password', type=str, required=True)
        self.__reqparse.add_argument('remember_me', type=bool)
        self.__reqparse.add_argument('X-Forwarded-For', type=str, dest='ip', location='headers')
        self.__reqparse.add_argument('User-Agent', type=str, dest='ua', location='headers')
        self.__args = self.__reqparse.parse_args()

    def post(self):
        retval = {}
        if self.__args.get('ip', None) is None:
            self.__args['ip'] = request.remote_addr

        device = user_agent_parser.Parse(self.__args['ua'])
        self.__args['device'] = device['os']['family']
        user = User.authenticate(**self.__args)
        if user.is_authenticated:
            retval['status'] = 'SUCCESS'
            retval['token'] = user.get_request_token()
        else:
            retval['status'] = 'FAILED'
            retval['message'] = 'Invalid login credentials'

        return retval


class LoginHandler(Resource):
    decorators = [limiter.limit("5/minute")]

    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__reqparse.add_argument('username', type=str, required=True)
        self.__reqparse.add_argument('password', type=str, required=True)
        self.__reqparse.add_argument('X-Forwarded-For', type=str, dest='ip')
        self.__reqparse.add_argument('User-Agent', type=str, dest='ua', location='headers')
        self.__args = self.__reqparse.parse_args()

    def post(self):
        retval = {}

        login_params = {
            'acct_code': app.config['GROUP_CODE'],
            'user_type': 'WEB'
        }

        self.__args['accountcode'] = app.config['GROUP_CODE']
        self.__args['company_code'] = 'PONOS'
        self.__args['user_type'] = 'WEB'
        self.__args['login_params'] = login_params

        if self.__args.get('ip', None) is None:
            self.__args['ip'] = request.remote_addr

        device = user_agent_parser.Parse(self.__args['ua'])
        self.__args['device'] = device['os']['family']
        user = User.authenticate(**self.__args)
        if user.is_authenticated:
            login_user(user)
            userdata = current_user.info
            args = {'requested_by': userdata['login_name']}
            get_request = Request(args).get()
            for req in get_request['request']:
                if req['status'] != 'FAILED':
                    current_user.remove()
                    logout_user()
                    return {
                        'status': 'FAILED',
                        'message': 'Invalid login credentials'
                    }

            retval['status'] = 'SUCCESS'
        else:
            retval['status'] = 'FAILED'
            retval['message'] = 'Invalid login credentials'

        return retval


class PasswordResetHandler(Resource):
    decorators = [limiter.limit("5/minute")]

    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__reqparse.add_argument('accountcode', type=str, required=True)
        self.__reqparse.add_argument('username', type=str, required=True)
        self.__reqparse.add_argument('email', type=str)
        self.__reqparse.add_argument('X-Forwarded-For', type=str, dest='ip')
        self.__reqparse.add_argument('User-Agent', type=str, dest='ua', location='headers')

    def post(self):
        self.__args = self.__reqparse.parse_args()
        retval = {
            'status': 'SUCCESS',
            'message': 'We have sent an email to the account holder if user exists.'
        }
        if self.__args.get('ip', None) is None:
            self.__args['ip'] = request.remote_addr

        device = user_agent_parser.Parse(self.__args['ua'])
        self.__args['device'] = device['os']['family']

        user = User(**self.__args)
        if user.is_exist:
            reset_token = user.generate_reset_token()

        return retval

    def get(self):
        self.__reqparse.add_argument('reset_token', type=str, required=True)
        self.__args = self.__reqparse.parse_args()

        retval = {}

        user = User.validate_token(**self.__args)
        if user.is_exist:
            retval['status'] = 'SUCCESS'
        else:
            retval['status'] = 'FAILED'

        return retval

    def patch(self):
        self.__reqparse.add_argument('reset_token', type=str, required=True)
        self.__reqparse.add_argument('password', type=str, required=True)
        self.__args = self.__reqparse.parse_args()

        retval = {}

        user = User.validate_token(**self.__args)
        if user.is_exist:
            user.update_password(self.__args['password'])
            user.remove_token()
            retval['status'] = 'SUCCESS'
        else:
            retval['status'] = 'FAILED'

        return retval


class MeHandler(Resource):
    decorators = [limiter.limit("5/minute")]

    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info
        self.__args['id'] = self.__userdata['uuid']
        self.__args['acct_code'] = self.__userdata['acct_code']

        users = Users(self.__args)
        retval = users.get()

        if retval['status'] == 'SUCCESS':
            login_info = []
            for data in retval['data']:
                login_info.append({'is_activated': data['is_activated']})

            retval['data'] = login_info

        return retval


class UserMeHandler(Resource):
    decorators = [limiter.limit("5/minute")]

    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('get_account_deletion_status', type=bool)

        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info
        person_data = {'id': self.__userdata['person']['id']}
        person = Person(person_data).get()
        retval = {
            'me': {
                'person': person['person'][0],
                'login_name': self.__userdata['login_name']
            }
        }
        if self.__args['get_account_deletion_status']:
            if app.config['ACTIVATE_ACCOUNT_DELETION'] == 'TRUE':
                retval['me']['activate_account_deletion'] = True
            else:
                retval['me']['activate_account_deletion'] = False

        return retval


class UserGroupHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self, login_uuid):
        self.__userdata = current_user.info
        self.__args['acct_code'] = self.__userdata['acct_code']
        if login_uuid == 'me':
            login_uuid = self.__userdata['uuid']
        self.__args['login_uuid'] = login_uuid

        user_group = UserGroup(self.__args)
        retval = user_group.get()

        return retval


class UserParamsHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self, login_uuid):
        self.__userdata = current_user.info
        self.__args['acct_code'] = self.__userdata['acct_code']
        self.__args['login_uuid'] = login_uuid

        user_params = UserParams(self.__args)
        retval = user_params.get()

        return retval

    @login_required
    def patch(self, login_uuid):
        self.__userdata = current_user.info
        self.__args['acct_code'] = self.__userdata['acct_code']
        self.__args['login_uuid'] = login_uuid

        self.__args['params'] = {
            'acct_code': current_app.config['GROUP_CODE'],
            'location_code': self.__args.get('location_code'),
            'agent_code': self.__args.get('agent_code')
        }
        self.__args['location_code'] = self.__args['main_location_code']

        login_args = {
            'id': login_uuid,
            'login_user': self.__userdata['agent_code'],
            'location_code': self.__args['location_code']
        }

        Users(login_args).update()

        user_params = UserParams(self.__args)
        retval = user_params.update()

        return retval


class UserPasswordHandler(Resource):
    decorators = [limiter.limit("5/minute")]

    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('POST'):
            self.__reqparse.add_argument('password', type=str, required=True)
        elif request.method in ('PATCH'):
            self.__reqparse.add_argument('old_password', type=str, required=True)
            self.__reqparse.add_argument('new_password', type=str, required=True)
        self.__args = self.__reqparse.parse_args()

    @login_required
    def patch(self):
        self.__userdata = current_user.info
        self.__args['acct_code'] = self.__userdata['acct_code']
        self.__args['login_uuid'] = self.__userdata['uuid']

        user_password = UserPassword(self.__args)
        retval = user_password.update()

        return retval

    @login_required
    def post(self, login_uuid):
        self.__userdata = current_user.info
        self.__args['acct_code'] = self.__userdata['acct_code']
        self.__args['login_uuid'] = login_uuid

        user_password = UserPassword(self.__args)
        retval = user_password.save()

        return retval


class UserPolicyHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self, login_uuid):
        self.__userdata = current_user.info
        self.__args['acct_code'] = self.__userdata['acct_code']
        if login_uuid == 'me':
            login_uuid = self.__userdata['uuid']
        self.__args['login_uuid'] = login_uuid

        policy = UserPolicy(self.__args)
        retval = policy.get()

        return retval

    @login_required
    def post(self, login_uuid):
        self.__userdata = current_user.info
        self.__args['acct_code'] = self.__userdata['acct_code']
        self.__args['login_uuid'] = login_uuid

        policy = UserPolicy(self.__args)
        retval = policy.save()

        return retval

    @login_required
    def delete(self, login_uuid, id):
        self.__userdata = current_user.info
        self.__args['acct_code'] = self.__userdata['acct_code']
        self.__args['login_uuid'] = login_uuid
        self.__args['id'] = id

        policy = UserPolicy(self.__args)
        retval = policy.delete()

        return retval


class UserPhotoHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('POST'):
            self.__reqparse.add_argument('file', type=werkzeug.FileStorage, required=True, location='files')
        self.__args = self.__reqparse.parse_args()

    @login_required
    def post(self, person_id):
        self.__userdata = current_user.info
        self.__args['acct_code'] = self.__userdata['acct_code']
        self.__args['group_code'] = self.__userdata['acct_code']
        self.__args['created_by'] = self.__userdata['login_name']
        retval = {}

        if person_id != 'me':
            return {'status', 'Invalid Path'}, 403
        else:
            self.__args['person_id'] = self.__userdata['person']['id']

        user_photo = UserPhoto(self.__args)
        file_data = self.__args.pop('file').stream
        file_name, key = user_photo.generate_filename(str(file_data))
        request_data = user_photo.request_file_upload(file_name, key)
        user_photo.upload(**request_data, file=file_data)
        retval = user_photo.save(file_name, key)

        return retval


class UserResumeHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('POST'):
            self.__reqparse.add_argument('file', type=werkzeug.FileStorage, required=True, location='files')
            self.__reqparse.add_argument('file_name', type=str, required=True)
        self.__args = self.__reqparse.parse_args()

    @login_required
    def post(self, person_id):
        self.__userdata = current_user.info
        self.__args['acct_code'] = self.__userdata['acct_code']
        self.__args['group_code'] = self.__userdata['acct_code']
        self.__args['created_by'] = self.__userdata['login_name']

        self.__args['field_group'] = 'RESUME'
        self.__args['field_code'] = 'RESUME'
        self.__args['field_type'] = 'STR'
        self.__args['field_description'] = self.__args['file_name']

        retval = {}

        if person_id != 'me':
            return {'status': 'Invalid Path'}, 403
        else:
            self.__args['person_id'] = self.__userdata['person']['id']

        user_resume = UserResume(self.__args)
        file_data = self.__args.pop('file')
        file_name, key = user_resume.generate_filename(str(file_data))
        request_data = user_resume.request_file_upload(file_name, key)
        user_resume.upload(**request_data, file=file_data)
        retval = user_resume.save(file_name, key)

        return retval
