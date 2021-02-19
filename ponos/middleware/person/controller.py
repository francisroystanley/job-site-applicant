from flask import request, url_for, render_template
from flask_restful import Resource, reqparse
from flask_login import login_required, current_user, login_user
from ua_parser import user_agent_parser

from ponos.global_init import app, limiter
from .model import Person, PersonAffiliation, PersonAttachment, PersonCertificate
from .model import PersonConsent, PersonDetail, PersonEducation, PersonIdentification
from .model import PersonLicense, PersonPortfolio, PersonPreference, PersonSkill
from .model import PersonSocialLink, PersonTraining, PersonWorkHistory
from ..consent import Consent
from ..document import CitySchema
from ..user.model import User, Users, UserPerson, UserAuthToken
from ..linkedin import Auth
from ..token import Token
from ..email import Email

import werkzeug


class PersonHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('is_searchable', type=str)
        elif request.method in ('PATCH'):
            self.__reqparse.add_argument('firstname', type=str, default=None)
            self.__reqparse.add_argument('middlename', type=str, default=None)
            self.__reqparse.add_argument('lastname', type=str, default=None)
            self.__reqparse.add_argument('gender', type=str, default=None)
            self.__reqparse.add_argument('email', type=str, default=None)
            self.__reqparse.add_argument('contact_number', type=str, default=None)
            self.__reqparse.add_argument('nationality', type=str, default=None)
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['id'] = self.__userdata['person']['id']

        person = Person(self.__args)
        retval = person.get()

        return retval

    @login_required
    def patch(self):
        self.__userdata = current_user.info

        person_data = self.__userdata['person']
        for key in self.__args:
            if self.__args[key] is not None:

                person_data[key] = self.__args[key]

        person_data['group_code'] = self.__userdata['group_code']
        person_data['login_user'] = self.__userdata['login_name']

        person = Person(person_data)
        retval = person.update()

        return retval


class PersonProfileAffiliationHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('POST', 'PATCH'):
            self.__reqparse.add_argument('affiliation', type=str, required=True)
            self.__reqparse.add_argument('position', type=str, required=True)
            self.__reqparse.add_argument('description', type=str, required=True)
            self.__reqparse.add_argument('date_start', type=str, required=True)
            self.__reqparse.add_argument('date_end', type=str, default=None)

        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['person_id'] = self.__userdata['person']['id']

        person_affiliation = PersonAffiliation(self.__args)
        retval = person_affiliation.get()

        return retval

    @login_required
    def post(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['created_by'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        self.__args['date_start'] = self.__args['date_start'] + 'T00:00:00Z'
        if self.__args['date_end'] is not None:
            self.__args['date_end'] = self.__args['date_end'] + 'T00:00:00Z'
        else:
            self.__args['date_end'] = '2099-12-31T00:00:00Z'

        person_affiliation = PersonAffiliation(self.__args)
        retval = person_affiliation.save()

        return retval

    @login_required
    def patch(self, id):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        self.__args['date_start'] = self.__args['date_start'] + 'T00:00:00Z'
        if self.__args['date_end'] is not None:
            self.__args['date_end'] = self.__args['date_end'] + 'T00:00:00Z'
        else:
            self.__args['date_end'] = '2099-12-31T00:00:00Z'

        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id

        person_affiliation = PersonAffiliation(self.__args)
        retval = person_affiliation.update()

        return retval

    @login_required
    def delete(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']
        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id
        person_affiliation = PersonAffiliation(self.__args)
        retval = person_affiliation.delete()

        return retval


class PersonProfileAttachmentHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('attachment_name', type=str)
            self.__reqparse.add_argument('attachment_type', type=str)
            self.__reqparse.add_argument('is_public', type=str)
        elif request.method in ('POST'):
            self.__reqparse.add_argument('attachment_ext', type=str, required=True)
            self.__reqparse.add_argument('attachment_name', type=str, required=True)
            self.__reqparse.add_argument('attachment_type', type=str, required=True)
            self.__reqparse.add_argument('file', type=werkzeug.FileStorage, required=True, location='files')
            self.__reqparse.add_argument('is_public', type=str, required=True)
        elif request.method in ('PATCH'):
            self.__reqparse.add_argument('is_public', type=str, required=True)

        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self, id=None):
        if id is not None:
            self.__args['id'] = id

        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['person_id'] = self.__userdata['person']['id']
        person_attachment = PersonAttachment(self.__args)
        retval = person_attachment.get()

        return retval

    @login_required
    def post(self):
        self.__userdata = current_user.info
        self.__args['acct_code'] = self.__userdata['acct_code']
        self.__args['group_code'] = self.__userdata['acct_code']
        self.__args['person_id'] = self.__userdata['person']['id']
        self.__args['created_by'] = self.__userdata['login_name']
        attachment = PersonAttachment(self.__args)
        file_data = self.__args.pop('file')
        ext = self.__args.pop('attachment_ext')
        filetype = self.__args['attachment_type']
        file_name, key = attachment.generate_filename(str(file_data), ext)
        request_data, path = attachment.request_file_upload(filetype, file_name, key)
        attachment.upload(**request_data, file=file_data)
        self.__args['file_name'] = file_name
        self.__args['path'] = path
        self.__args['key'] = key
        retval = attachment.save()

        return retval

    @login_required
    def patch(self, id):
        if id is None:
            return {'status': 'FAILED'}

        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']
        self.__args['id'] = id

        person_attachment = PersonAttachment(self.__args)
        retval = person_attachment.update()

        return retval

    @login_required
    def delete(self, id):
        if id is None:
            return {'status': 'FAILED'}

        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']
        self.__args['id'] = id
        person_attachment = PersonAttachment(self.__args)
        retval = person_attachment.delete()

        return retval


class PersonProfileCertificateHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('POST', 'PATCH'):
            self.__reqparse.add_argument('certificate_name', type=str, required=True)
            self.__reqparse.add_argument('certificate_type', type=str, required=True)
            self.__reqparse.add_argument('certificate_number', type=str, required=True)
            self.__reqparse.add_argument('certification_body', type=str, required=True)
            self.__reqparse.add_argument('date_taken', type=str, required=True)
            self.__reqparse.add_argument('date_expiry', type=str, required=True)

        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['person_id'] = self.__userdata['person']['id']

        person_certificate = PersonCertificate(self.__args)
        retval = person_certificate.get()

        return retval

    @login_required
    def post(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['created_by'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        person_certificate = PersonCertificate(self.__args)
        retval = person_certificate.save()

        return retval

    @login_required
    def patch(self, id):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id

        person_certificate = PersonCertificate(self.__args)
        retval = person_certificate.update()

        return retval

    @login_required
    def delete(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']
        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id
        person_certificate = PersonCertificate(self.__args)
        retval = person_certificate.delete()

        return retval


class PersonProfileConsentHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET', 'DELETE'):
            self.__reqparse.add_argument('consent_name', type=str)
            self.__reqparse.add_argument('businessunit_code', type=str)
        elif request.method in ('POST', 'PATCH'):
            self.__reqparse.add_argument('consent_code', type=str, required=True)
            self.__reqparse.add_argument('businessunit_code', type=str, required=True)
            self.__reqparse.add_argument('subscribe', type=str, required=True)
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['person_id'] = self.__userdata['person']['id']

        if id is not None:
            self.__args['id'] = id

        person_consent = PersonConsent(self.__args)
        retval = person_consent.get()

        return retval

    @login_required
    def post(self):
        self.__userdata = current_user.info
        consents = self.__args['consent_code']

        for code in consents.split('|'):
            consent = Consent({'consent_code': code, 'group_code': self.__userdata['group_code']}).get()

            consentData = {
                'consent_code': consent['consent'][0]['consent_code'],
                'consent_name': consent['consent'][0]['consent_name'],
                'description': consent['consent'][0]['description'],
                'businessunit_code': self.__args['businessunit_code'],
                'subscribe': self.__args['subscribe'],
                'group_code': self.__userdata['group_code'],
                'created_by': self.__userdata['login_name'],
                'person_id': self.__userdata['person']['id']
            }

            person_consent = PersonConsent(consentData)
            retval = person_consent.save()

        return retval

    @login_required
    def patch(self, id):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id

        person_consent = PersonConsent(self.__args)
        retval = person_consent.update()

        return retval

    @login_required
    def delete(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']
        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id
        person_consent = PersonConsent(self.__args)
        retval = person_consent.delete()

        return retval


class PersonProfileDetailHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('field_group', type=str)
            self.__reqparse.add_argument('field_code', type=str)
            self.__reqparse.add_argument('filter', type=str)
        elif request.method in ('POST'):
            self.__reqparse.add_argument('fields', type=dict, location='json', required=True)

        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['person_id'] = self.__userdata['person']['id']

        person_detail = PersonDetail(self.__args)
        retval = person_detail.get()

        return retval

    @login_required
    def post(self):
        retval = {'status': 'SUCCESS'}
        person_detail = []
        self.__userdata = current_user.info
        person_id = self.__userdata['person']['id']
        fields = self.__args['fields']['field_list']

        for field in fields:
            if 'old_value' in field:
                if 'code' in field['old_value'] and 'code' in field['value']:
                    if field['old_value']['code'] != field['value']['code']:
                        if 'id' in field['old_value']:
                            retval_delete = PersonDetail({
                                'id': field['old_value']['id'],
                                'person_id': person_id,
                                'group_code': self.__userdata['group_code'],
                                'login_user': self.__userdata['login_name']
                            }).delete()
                            if retval_delete['status'] != 'SUCCESS':
                                return {'status': 'FAILED'}

            if 'code' in field['value']:
                field_insert_data = {
                    'person_id': person_id,
                    'field_code': field['field'],
                    'field_type': field['type'],
                    'field_group': field['group'],
                    'field_sub_group': field['sub_group'],
                    'field_set': field['set'],
                    'field_value': field['value']['code'],
                    'field_description': field['value']['name'],
                    'group_code': self.__userdata['group_code'],
                    'created_by': self.__userdata['login_name']
                }
                retval_save = PersonDetail(field_insert_data).save()
                if retval_save['status'] != 'SUCCESS':
                    return {'status': 'FAILED'}

                person_detail.append(retval_save['person_detail'][0])

        retval['person_detail'] = person_detail
        retval['total_count'] = len(person_detail)

        return retval

    @login_required
    def delete(self, id):
        self.__userdata = current_user.info
        person_id = self.__userdata['person']['id']

        if id is None:
            retval = {'status': 'FAILED'}

            return retval

        for i in id.split('|'):
            retval = PersonDetail({
                'id': i,
                'person_id': person_id,
                'group_code': self.__userdata['group_code'],
                'login_user': self.__userdata['login_name']
            }).delete()

        return retval


class PersonProfileEducationHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('POST', 'PATCH'):
            self.__reqparse.add_argument('school_code', type=str)
            self.__reqparse.add_argument('school_name', type=str, required=True)
            self.__reqparse.add_argument('course_level', type=str, dest='level', required=True)
            self.__reqparse.add_argument('course_code', type=str)
            self.__reqparse.add_argument('course_name', type=str, default='')
            self.__reqparse.add_argument('course_major', type=str, default='')
            self.__reqparse.add_argument('award', type=str, required=True)
            self.__reqparse.add_argument('date_start', type=str, required=True)
            self.__reqparse.add_argument('date_end', type=str, default=None)

        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['person_id'] = self.__userdata['person']['id']

        person_education = PersonEducation(self.__args)
        retval = person_education.get()

        return retval

    @login_required
    def post(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['created_by'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        self.__args['date_start'] = self.__args['date_start'] + 'T00:00:00Z'
        if self.__args['date_end'] is not None:
            self.__args['date_end'] = self.__args['date_end'] + 'T00:00:00Z'
        else:
            self.__args['date_end'] = '2099-12-31T00:00:00Z'

        person_education = PersonEducation(self.__args)
        retval = person_education.save()

        return retval

    @login_required
    def patch(self, id):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        self.__args['date_start'] = self.__args['date_start'] + 'T00:00:00Z'
        if self.__args['date_end'] is not None:
            self.__args['date_end'] = self.__args['date_end'] + 'T00:00:00Z'
        else:
            self.__args['date_end'] = '2099-12-31T00:00:00Z'

        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id

        person_education = PersonEducation(self.__args)
        retval = person_education.update()

        return retval

    @login_required
    def delete(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']
        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id
        person_education = PersonEducation(self.__args)
        retval = person_education.delete()

        return retval


class PersonProfileIdentificationHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('POST', 'PATCH'):
            self.__reqparse.add_argument('identification_class', type=str, required=True)
            self.__reqparse.add_argument('identification_type', type=str, required=True)
            self.__reqparse.add_argument('identification_sub_type', type=str, required=True)
            self.__reqparse.add_argument('identification_number', type=str, required=True)
            self.__reqparse.add_argument('place_issued', type=str, required=True)
            self.__reqparse.add_argument('date_taken', type=str, required=True)
            self.__reqparse.add_argument('date_expiry', type=str, required=True)

        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['person_id'] = self.__userdata['person']['id']

        person_identification = PersonIdentification(self.__args)
        retval = person_identification.get()

        return retval

    @login_required
    def post(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['created_by'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        person_identification = PersonIdentification(self.__args)
        retval = person_identification.save()

        return retval

    @login_required
    def patch(self, id):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id

        person_identification = PersonIdentification(self.__args)
        retval = person_identification.update()

        return retval

    @login_required
    def delete(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']
        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id
        person_identification = PersonIdentification(self.__args)
        retval = person_identification.delete()

        return retval


class PersonProfileLicenseHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('POST', 'PATCH'):
            self.__reqparse.add_argument('restrictions', type=str, required=True)
            self.__reqparse.add_argument('license_id', type=str, required=True)
            self.__reqparse.add_argument('license_number', type=str, required=True)
            self.__reqparse.add_argument('place_issued', type=str, required=True)
            self.__reqparse.add_argument('date_taken', type=str, required=True)
            self.__reqparse.add_argument('date_expiry', type=str, required=True)
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['person_id'] = self.__userdata['person']['id']

        person_license = PersonLicense(self.__args)
        retval = person_license.get()

        return retval

    @login_required
    def post(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['created_by'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']
        self.__args['date_start'] = self.__args['date_taken'] + 'T00:00:00Z'
        self.__args['date_end'] = self.__args['date_expiry'] + 'T00:00:00Z'

        person_license = PersonLicense(self.__args)
        retval = person_license.save()

        return retval

    @login_required
    def patch(self, id):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id
        self.__args['date_start'] = self.__args['date_taken'] + 'T00:00:00Z'
        self.__args['date_end'] = self.__args['date_expiry'] + 'T00:00:00Z'

        person_license = PersonLicense(self.__args)
        retval = person_license.update()

        return retval

    @login_required
    def delete(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']
        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id
        person_license = PersonLicense(self.__args)
        retval = person_license.delete()

        return retval


class PersonProfilePortfolioHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('POST', 'PATCH'):
            self.__reqparse.add_argument('project_type', type=str, required=True)
            self.__reqparse.add_argument('project_name', type=str, required=True)
            self.__reqparse.add_argument('project_description', type=str, required=True)
            self.__reqparse.add_argument('role', type=str, required=True)
            self.__reqparse.add_argument('project_link', type=str, required=True)
            self.__reqparse.add_argument('client', type=str, required=True)
            self.__reqparse.add_argument('date_start', type=str, required=True)
            self.__reqparse.add_argument('date_end', type=str, default=None)

        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['person_id'] = self.__userdata['person']['id']

        person_portfolio = PersonPortfolio(self.__args)
        retval = person_portfolio.get()

        return retval

    @login_required
    def post(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['created_by'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        self.__args['date_start'] = self.__args['date_start'] + 'T00:00:00Z'
        if self.__args['date_end'] is not None:
            self.__args['date_end'] = self.__args['date_end'] + 'T00:00:00Z'
        else:
            self.__args['date_end'] = '2099-12-31T00:00:00Z'

        person_portfolio = PersonPortfolio(self.__args)
        retval = person_portfolio.save()

        return retval

    @login_required
    def patch(self, id):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        self.__args['date_start'] = self.__args['date_start'] + 'T00:00:00Z'
        if self.__args['date_end'] is not None:
            self.__args['date_end'] = self.__args['date_end'] + 'T00:00:00Z'
        else:
            self.__args['date_end'] = '2099-12-31T00:00:00Z'

        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id

        person_portfolio = PersonPortfolio(self.__args)
        retval = person_portfolio.update()

        return retval

    @login_required
    def delete(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']
        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id
        person_portfolio = PersonPortfolio(self.__args)
        retval = person_portfolio.delete()

        return retval


class PersonProfilePreferenceHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('preference_code', type=str)
            self.__reqparse.add_argument('preference_type', type=str)
        elif request.method in ('POST', 'PATCH'):
            self.__reqparse.add_argument('preference_code', type=str, required=True)
            self.__reqparse.add_argument('preference_type', type=str, required=True)
            self.__reqparse.add_argument('value_type', type=str, required=True)
            self.__reqparse.add_argument('cvalue_1', type=str, default=None)
            self.__reqparse.add_argument('cvalue_2', type=str, default=None)
            self.__reqparse.add_argument('cvalue_3', type=str, default=None)
            self.__reqparse.add_argument('cvalue_4', type=str, default=None)
            self.__reqparse.add_argument('cvalue_5', type=str, default=None)
            self.__reqparse.add_argument('nvalue_1', type=int, default=None)
            self.__reqparse.add_argument('nvalue_2', type=int, default=None)
            self.__reqparse.add_argument('nvalue_3', type=int, default=None)
            self.__reqparse.add_argument('nvalue_4', type=int, default=None)
            self.__reqparse.add_argument('nvalue_5', type=int, default=None)
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['person_id'] = self.__userdata['person']['id']

        if id is not None:
            self.__args['id'] = id

        person_preference = PersonPreference(self.__args)
        retval = person_preference.get()

        return retval

    @login_required
    def post(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['created_by'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        person_preference = PersonPreference(self.__args)
        retval = person_preference.save()

        return retval

    @login_required
    def patch(self, id):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id

        person_preference = PersonPreference(self.__args)
        retval = person_preference.update()

        return retval

    @login_required
    def delete(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id

        person_preference = PersonPreference(self.__args)
        retval = person_preference.delete()

        return retval


class PersonProfileSkillHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('POST'):
            self.__reqparse.add_argument('id', type=str, dest='skill_id', required=True)
            self.__reqparse.add_argument('skill_class', type=str, required=True)
            self.__reqparse.add_argument('skill_code', type=str, required=True)
            self.__reqparse.add_argument('skill_name', type=str, required=True)
            self.__reqparse.add_argument('rating', type=int)

        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['person_id'] = self.__userdata['person']['id']

        person_skill = PersonSkill(self.__args)
        retval = person_skill.get()

        return retval

    @login_required
    def post(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['created_by'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        person_skill = PersonSkill(self.__args)
        retval = person_skill.save()

        return retval

    @login_required
    def delete(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']
        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id
        person_skill = PersonSkill(self.__args)
        retval = person_skill.delete()

        return retval


class PersonProfileSocialLinksHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('POST', 'PATCH'):
            self.__reqparse.add_argument('social_code', type=str, required=True)
            self.__reqparse.add_argument('social_handle', type=str, required=True)
            self.__reqparse.add_argument('social_link', type=str, required=True)

        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['person_id'] = self.__userdata['person']['id']

        person_social_links = PersonSocialLink(self.__args)
        retval = person_social_links.get()

        return retval

    @login_required
    def post(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['created_by'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        person_social_links = PersonSocialLink(self.__args)
        retval = person_social_links.save()

        return retval

    @login_required
    def patch(self, id):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id

        person_social_links = PersonSocialLink(self.__args)
        retval = person_social_links.update()

        return retval

    @login_required
    def delete(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']
        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id
        person_social_links = PersonSocialLink(self.__args)
        retval = person_social_links.delete()

        return retval


class PersonProfileTrainingHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('POST', 'PATCH'):
            self.__reqparse.add_argument('training_name', type=str, required=True)
            self.__reqparse.add_argument('training_type', type=str, required=True)
            self.__reqparse.add_argument('venue', type=str, required=True)
            self.__reqparse.add_argument('facilitator', type=str, required=True)
            self.__reqparse.add_argument('rating', type=str, required=True)
            self.__reqparse.add_argument('date_start', type=str, required=True)
            self.__reqparse.add_argument('date_end', type=str, default=None)

        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['person_id'] = self.__userdata['person']['id']

        person_training = PersonTraining(self.__args)
        retval = person_training.get()

        return retval

    @login_required
    def post(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['created_by'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        self.__args['date_start'] = self.__args['date_start'] + 'T00:00:00Z'
        if self.__args['date_end'] is not None:
            self.__args['date_end'] = self.__args['date_end'] + 'T00:00:00Z'
        else:
            self.__args['date_end'] = '2099-12-31T00:00:00Z'

        person_training = PersonTraining(self.__args)
        retval = person_training.save()

        return retval

    @login_required
    def patch(self, id):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        self.__args['date_start'] = self.__args['date_start'] + 'T00:00:00Z'
        if self.__args['date_end'] is not None:
            self.__args['date_end'] = self.__args['date_end'] + 'T00:00:00Z'
        else:
            self.__args['date_end'] = '2099-12-31T00:00:00Z'

        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id

        person_training = PersonTraining(self.__args)
        retval = person_training.update()

        return retval

    @login_required
    def delete(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']
        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id
        person_training = PersonTraining(self.__args)
        retval = person_training.delete()

        return retval


class PersonProfileWorkHistoryHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('POST', 'PATCH'):
            self.__reqparse.add_argument('company_name', type=str, required=True)
            self.__reqparse.add_argument('department', type=str, required=True)
            self.__reqparse.add_argument('job_title', type=str, required=True)
            self.__reqparse.add_argument('job_description', type=str, required=True)
            self.__reqparse.add_argument('address', type=str, required=True)
            self.__reqparse.add_argument('city_code', type=str, required=True)
            self.__reqparse.add_argument('province_code', type=str, required=True)
            self.__reqparse.add_argument('country_code', type=str, required=True)
            self.__reqparse.add_argument('is_related_company', type=str, required=True)
            self.__reqparse.add_argument('date_start', type=str, required=True)
            self.__reqparse.add_argument('date_end', type=str, default=None)

        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['person_id'] = self.__userdata['person']['id']

        person_work_history = PersonWorkHistory(self.__args)
        retval = person_work_history.get()

        for work in retval['person_work_history']:
            cities = CitySchema.objects(city_code=work['city_code'])
            for city in cities:
                city_data = {
                    'city_code': city['city_code'],
                    'city_name': city['city_name'],
                    'province_code': city['province_code'],
                    'province_name': city['province_name'],
                    'country_code': city['country_code']
                }

                work['city'] = city_data

        return retval

    @login_required
    def post(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['created_by'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        self.__args['date_start'] = self.__args['date_start'] + 'T00:00:00Z'
        if self.__args['date_end'] is not None:
            self.__args['date_end'] = self.__args['date_end'] + 'T00:00:00Z'
        else:
            self.__args['date_end'] = '2099-12-31T00:00:00Z'

        person_work_history = PersonWorkHistory(self.__args)
        retval = person_work_history.save()

        return retval

    @login_required
    def patch(self, id):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        self.__args['date_start'] = self.__args['date_start'] + 'T00:00:00Z'
        if self.__args['date_end'] is not None:
            self.__args['date_end'] = self.__args['date_end'] + 'T00:00:00Z'
        else:
            self.__args['date_end'] = '2099-12-31T00:00:00Z'

        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id

        person_work_history = PersonWorkHistory(self.__args)
        retval = person_work_history.update()

        return retval

    @login_required
    def delete(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']
        if id is None:
            retval = {
                'status': 'FAILED'
            }

            return retval

        self.__args['id'] = id
        person_work_history = PersonWorkHistory(self.__args)
        retval = person_work_history.delete()

        return retval


class PersonRegisterHandler(Resource):
    decorators = [limiter.limit("3/minute")]

    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('POST'):
            self.__reqparse.add_argument('firstname', type=str, required=True)
            self.__reqparse.add_argument('lastname', type=str, required=True)
            self.__reqparse.add_argument('email', type=str, required=True)
            self.__reqparse.add_argument('contact_number', type=str, required=False)
            self.__reqparse.add_argument('gender', type=str, default='MALE')
            self.__reqparse.add_argument('password', type=str, required=True)
            self.__reqparse.add_argument('consent', type=dict, location='json', required=True)
            self.__reqparse.add_argument('city_code', type=str, required=True)
            self.__reqparse.add_argument('city_name', type=str, required=True)
            self.__reqparse.add_argument('province_code', type=str, required=True)
            self.__reqparse.add_argument('province_name', type=str, required=True)
            self.__reqparse.add_argument('country_code', type=str, required=True)
            self.__reqparse.add_argument('X-Forwarded-For', type=str, dest='ip', location='headers')
            self.__reqparse.add_argument('User-Agent', type=str, dest='ua', location='headers')
            self.__reqparse.add_argument('interests', type=dict, location='json', required=True)
            self.__reqparse.add_argument('auth_token', type=str, location='json')
            self.__reqparse.add_argument('auth_provider', type=str, location='json')
            self.__reqparse.add_argument('auth_code', type=str, location='json')
        self.__args = self.__reqparse.parse_args()

    def post(self):
        create_login_credential = False
        person_firstname_param = self.__args['firstname']
        recipient_email = self.__args['email']

        if self.__args['contact_number'] != '':
            self.__args['mobile'] = self.__args['contact_number']
        self.__args['nationality'] = 'PH'

        self.__args['title'] = ''
        self.__args['group_code'] = app.config['GROUP_CODE']
        self.__args['created_by'] = 'WEB'
        self.__args['identity_provider'] = 'VPROFILES'
        self.__args['override_check'] = False
        self.__args['is_verified'] = False
        self.__args['is_searchable'] = True

        signup = UserPerson(self.__args)
        retval = signup.save()
        if retval['status'] != 'SUCCESS':
            retval = {
                'status': 'FAILED',
                'message': 'Email or contact number is already exist.'
            }

            return retval

        create_login_credential = True
        person_uuid = retval['person'][0]['uuid']
        self.__args['uuid'] = person_uuid
        self.__args['person_type'] = 'WEB'
        person = Person(self.__args)
        retval = person.save()

        if retval['status'] != 'SUCCESS':
            retval = {
                'status': 'FAILED',
                'message': 'Something went wrong, please try again later.'
            }

            return retval

        person_id = retval['person'][0]['id']
        self.save_person_preference_consent(person_id)

        if create_login_credential:
            person_uuid = retval['person'][0]['uuid']
            acct_code = app.config['GROUP_CODE']
            login_params = {
                'acct_code': acct_code,
                'user_type': 'WEB'
            }
            login_data = {
                'person_uuid': person_uuid,
                'identity_provider': 'VPROFILES',
                'acct_code': acct_code,
                'company_code': 'PONOS',
                'login_name': self.__args['email'],
                'password': self.__args['password'],
                'requires_activation': True,
                'login_params': str(login_params)
            }
            signup_login = Users(login_data)
            login_data = signup_login.save()

            if self.__args['auth_provider'] is not None and self.__args['auth_token'] is not None:
                if len(login_data.get('data')) > 0 and login_data['data'][0].get('login_uuid') is not None:
                    login = login_data['data'][0]
                    data = {
                        'login_uuid': login['login_uuid'],
                        'auth_token': self.__args['auth_token'],
                        'auth_provider': self.__args['auth_provider']
                    }
                    auth_token = UserAuthToken(data)
                    auth_token.save()
                    url = Auth().get()
                    retval = {
                        'url': url,
                        'action': 'redirect',
                        'status': 'SUCCESS'
                    }
            else:
                retval = {
                    'status': 'SUCCESS'
                }

            login_uuid_param = login_data['data'][0]['login_uuid']
            token_data = {
                'token_type': 'LOGIN_ACTIVATION',
                'login_uuid': login_uuid_param
            }
            get_token = Token(token_data)
            retval_token = get_token.get()
            token_param = retval_token['token'][0]['token']

            client_url = url_for('index', login_name=None, _external=True, _scheme='https')
            activation_url = '{}activate?code={}&email={}'.format(client_url, token_param, recipient_email)

            data = {
                'client_code': app.config['CLIENT_CODE'],
                'name': person_firstname_param,
                'link': activation_url,
                'img_link': client_url + 'static/assets/images/{}/email-logo.png'.format(app.config['CLIENT_CODE'].lower())
            }

            email_template = render_template('email/email-sign-up.html', data=data)
            email_data = {
                'body': '{} Recruitment Email Verification'.format(app.config['CLIENT_CODE']),
                'body_html': email_template,
                'recipient': recipient_email,
                'sender': app.config['NOREPLY_EMAIL'],
                'subject': '{} Recruitment Email Verification'.format(app.config['CLIENT_CODE']),
                'acct_code': app.config['GROUP_CODE']
            }

            email = Email(email_data)
            email.save()

            login_params = {
                'acct_code': app.config['GROUP_CODE'],
                'user_type': 'WEB'
            }

            login_args = {
                'username': self.__args['email'],
                'password': self.__args['password'],
                'accountcode': app.config['GROUP_CODE'],
                'company_code': 'PONOS',
                'user_type': 'WEB',
                'login_params': login_params,
                'ua': self.__args['ua'],
                'ip': self.__args['ip']
            }

            if login_args.get('ip', None) is None:
                login_args['ip'] = request.remote_addr

            device = user_agent_parser.Parse(self.__args['ua'])
            login_args['device'] = device['os']['family']
            user = User.authenticate(**login_args)
            if user.is_authenticated:
                login_user(user)

        return retval

    def save_person_preference_consent(self, person_id):
        interest_list = self.__args['interests']['interests']

        self.__args['consent']['person_id'] = person_id
        self.__args['consent']['subscribe'] = True
        self.__args['consent']['group_code'] = app.config['GROUP_CODE']
        self.__args['consent']['created_by'] = self.__args['email']
        self.__args['consent'].pop('id', None)

        PersonConsent(self.__args['consent']).save()

        person_location = {
            'person_id': person_id,
            'preference_code': 'WORK_LOCATION',
            'preference_type': 'SINGLE',
            'value_type': 'CHAR',
            'cvalue_1': self.__args['city_code'],
            'cvalue_2': self.__args['city_name'],
            'cvalue_3': self.__args['province_code'],
            'cvalue_4': self.__args['province_name'],
            'cvalue_5': self.__args['country_code'],
            'group_code': app.config['GROUP_CODE'],
            'created_by': self.__args['email']
        }

        PersonPreference(person_location).save()

        person_salary = {
            'person_id': person_id,
            'preference_code': 'SALARYRANGE',
            'preference_type': 'RANGE',
            'value_type': 'NUMERIC',
            'nvalue_1': 0,
            'nvalue_2': 0,
            'group_code': app.config['GROUP_CODE'],
            'created_by': self.__args['email']
        }

        PersonPreference(person_salary).save()

        for interest in interest_list:
            person_interest = {
                'person_id': person_id,
                'preference_code': 'INTEREST',
                'preference_type': 'MULTIPLE',
                'value_type': 'CHAR',
                'cvalue_1': interest['job_class_code'],
                'cvalue_2': interest['job_class_name'],
                'group_code': app.config['GROUP_CODE'],
                'created_by': self.__args['email']
            }

            PersonPreference(person_interest).save()
