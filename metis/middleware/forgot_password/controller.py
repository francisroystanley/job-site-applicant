from flask import render_template, url_for
from flask_restful import Resource, reqparse

from ..user import Users, UserPerson, UserPassword
from metis.global_init import app, limiter
from ..email import Email

import random
import string


class ForgotPasswordHandler(Resource):
    decorators = [limiter.limit("2/days")]

    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__reqparse.add_argument('email', type=str, required=True)
        self.__args = self.__reqparse.parse_args()

    def post(self):
        recipient_email = self.__args['email']
        self.__args['login_name'] = recipient_email
        self.__args['acct_code'] = app.config['GROUP_CODE']

        forgotpassword = Users(self.__args)
        res = forgotpassword.get()
        retval_login = res

        if retval_login is None:
            retval = {
                'status': 'FAILED',
                'message': 'Internal Server Error.'
            }

            return retval

        if 'status' not in retval_login or retval_login['status'] != 'SUCCESS':
            retval = {
                'status': 'FAILED',
                'message': 'Invalid Email Address or Email Address Not Found.'
            }

            return retval

        person_uuid = retval_login['data'][0]['person_uuid']
        login_uuid = retval_login['data'][0]['login_uuid']
        person_data = {
            'person_uuid': person_uuid
        }
        person = UserPerson(person_data)
        res = person.get()

        retval_person = res
        if res is None:
            retval = {
                'status': 'FAILED',
                'message': 'Invalid Email Address or Email Address Not Found.'
            }

            return retval

        if retval_person['status'] != 'SUCCESS':
            retval = {
                'status': 'FAILED',
                'message': 'Invalid Email Address or Email Address Not Found.'
            }

            return retval

        person_firstname_param = retval_person['person'][0]['firstname']
        password_param = ''.join(random.choice(string.digits) for _ in range(7))
        password_data = {
            'password': password_param,
            'login_user': recipient_email,
            'login_uuid': login_uuid,
            'acct_code': app.config['GROUP_CODE']
        }

        updatepassword = UserPassword(password_data)
        res = updatepassword.save()

        if res is None:
            retval = {
                'status': 'FAILED',
                'message': 'Password Reset Failed. Please try again later.'
            }

            return retval

        client_url = url_for('index', login_name=None, _external=True, _scheme='https')

        email_template = render_template(
            'email/email-forgot-password.html',
            client_code=app.config['CLIENT_CODE'],
            fname=person_firstname_param,
            password=password_param,
            img_link=client_url + 'static/assets/images/{}/email-logo.png'.format(app.config['CLIENT_CODE'].lower())
        )

        email_data = {
            'body': '{} Recruitment Forgot Password'.format(app.config['CLIENT_CODE']),
            'body_html': email_template,
            'recipient': recipient_email,
            'sender': app.config['NOREPLY_EMAIL'],
            'subject': '{} Recruitment Forgot Password'.format(app.config['CLIENT_CODE']),
            'acct_code': app.config['GROUP_CODE']
        }

        email = Email(email_data)
        email_retval = email.send()

        if email_retval['status'] != 'SUCCESS':
            retval = {
                'status': 'FAILED',
                'message': 'Email sending failed. Please try again later.'
            }

            return retval

        retval = email_retval
        return retval
