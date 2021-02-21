from flask_restful import Resource, reqparse
from flask import request, url_for, render_template
from flask_login import login_required, current_user

from .model import Email
from ponos.global_init import app, limiter
from ..token import Token


class EmailHandler(Resource):
    decorators = [limiter.limit("2/minute")]

    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__args = self.__reqparse.parse_args()
        self.__args['group_code'] = app.config['GROUP_CODE']

    def post(self):
        email = Email(self.__args)
        retval = email.save()

        return retval


class EmailVerifyHandler(Resource):
    decorators = [limiter.limit("2/minute")]

    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__args = self.__reqparse.parse_args()

    @login_required
    def post(self):
        self.__userdata = current_user.info
        token_data = {
            'token_type': 'LOGIN_ACTIVATION',
            'login_uuid': self.__userdata['uuid']
        }
        get_token = Token(token_data)
        retval_token = get_token.get()
        token_param = retval_token['token'][0]['token']
        client_url = url_for('index', login_name=None, _external=True, _scheme='https')
        activation_url = '{}activate?code={}&email={}'.format(client_url, token_param, self.__userdata['person']['email'])
        data = {
            'client_code': app.config['CLIENT_CODE'],
            'name': self.__userdata['person']['firstname'],
            'link': activation_url,
            'img_link': client_url + 'static/assets/images/{}/email-logo.png'.format(app.config['CLIENT_CODE'].lower())
        }
        email_template = render_template('email/email-sign-up.html', data=data)
        email_data = {
            'body': '{} Recruitment Email Verification'.format(app.config['CLIENT_CODE']),
            'body_html': email_template,
            'recipient': self.__userdata['person']['email'],
            'sender': app.config['NOREPLY_EMAIL'],
            'subject': '{} Recruitment Email Verification'.format(app.config['CLIENT_CODE']),
            'acct_code': app.config['GROUP_CODE']
        }
        email = Email(email_data)
        email.save()

        return {
            'status': 'SUCCESS',
            'email': self.__userdata['person']['email']
        }
