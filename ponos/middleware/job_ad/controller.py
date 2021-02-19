from flask import request
from flask_restful import Resource, reqparse
from flask_login import login_required, current_user

from ponos.global_init import app
from .model import JobAd, JobAdAdvSearch, JobAdApplication, JobAdApplicationEvent, JobAdApplicationQuick
from .model import JobAdSearchTag, JobAdTag
from ..document import ProvinceSchema


class JobAdHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('businessunit_code', type=str)
            self.__reqparse.add_argument('is_advanced_search', type=bool, default=None)
            self.__reqparse.add_argument('branch_code', type=str)
            self.__reqparse.add_argument('city_code', type=str)
            self.__reqparse.add_argument('province_code', type=str)
            self.__reqparse.add_argument('country_code', type=str)
            self.__reqparse.add_argument('job_title', type=str)
            self.__reqparse.add_argument('status', type=str)
            self.__reqparse.add_argument('job_class', type=str)
            self.__reqparse.add_argument('filter', type=str)

        self.__args = self.__reqparse.parse_args()

    def get(self, id=None):
        self.__args['group_code'] = app.config['GROUP_CODE']
        if id is not None:
            self.__args['id'] = id

        if self.__args['is_advanced_search']:
            retval_jobad = JobAdAdvSearch(self.__args).get()
        else:
            retval_jobad = JobAd(self.__args).get()

        if retval_jobad['status'] != 'SUCCESS':
            retval = {
                'status': 'FAILED'
            }

            return retval

        job_ads = retval_jobad['job_ad']
        for job_ad in job_ads:
            job_ad['province'] = {}
            province = ProvinceSchema.objects(province_code=job_ad['province_code'])
            if len(province) > 0:
                job_ad['province'] = {
                    'province_code': province[0]['province_code'],
                    'province_name': province[0]['province_name'],
                    'country_code': province[0]['country_code']
                }

        retval = {
            'status': 'SUCCESS',
            'job_ad': job_ads,
            'total_count': retval_jobad['total_count']
        }

        return retval


class JobAdApplicationHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('status', type=str)
            self.__reqparse.add_argument('filter', type=str)
        if request.method in ('POST'):
            self.__reqparse.add_argument('job_ad_id', type=str, required=True)
            self.__reqparse.add_argument('businessunit_id', type=str, required=True)
            self.__reqparse.add_argument('branch_id', type=str, required=True)
            self.__reqparse.add_argument('result', type=str, required=True)
            self.__reqparse.add_argument('fullname', type=str, required=True)
            self.__reqparse.add_argument('gender', type=str, required=True)
            self.__reqparse.add_argument('city_code', type=str, required=False)
            self.__reqparse.add_argument('province_code', type=str, required=False)
            self.__reqparse.add_argument('ref_job_ad_application_id', type=str, required=True)
            self.__reqparse.add_argument('job_title', type=str, required=True)
            self.__reqparse.add_argument('status', type=str, required=False)
            self.__reqparse.add_argument('hiring_manager_person_id', type=str, required=True)
        if request.method in ('PATCH'):
            self.__reqparse.add_argument('id', type=str, required=True)
            self.__reqparse.add_argument('status', type=str, required=True)
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self, id=None):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['person_id'] = self.__userdata['person']['id']

        if id is not None:
            self.__args['id'] = id

        jobAdApplication = JobAdApplication(self.__args)
        retval = jobAdApplication.get()

        return retval

    @login_required
    def post(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['created_by'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        self.__args['status'] = 'OPEN'

        job_ad_application = JobAdApplication(self.__args)
        retval = job_ad_application.save()

        if retval['status'] != 'SUCCESS':
            retval = {
                'status': 'FAILED'
            }

            return retval

        for job_ad_app in retval['job_ad_application']:
            event_data = {
                'id': job_ad_app['id'],
                'job_ad_id': job_ad_app['id'],
                'event_code': 'JOB_APP_STATUS',
                'event_action': job_ad_app['status'],
                'event_detail': '{} Job application status'.format(job_ad_app['status']),
                'is_public': False,
                'created_by': self.__args['created_by'],
                'group_code': self.__args['group_code']
            }
            Job_ad_app_event = JobAdApplicationEvent(event_data)
            Job_ad_app_event.save()

        return retval

    @login_required
    def patch(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['login_user'] = self.__userdata['login_name']
        self.__args['created_by'] = self.__userdata['login_name']
        self.__args['person_id'] = self.__userdata['person']['id']

        self.__args['status'] = 'WITHDRAWED'

        this_object = JobAdApplication(self.__args)
        retval = this_object.update()

        if retval['status'] != 'SUCCESS':
            retval = {
                'status': 'FAILED',
                'message': 'Update Application status failed. Please try again later.'
            }

            return retval

        for job_ad_app in retval['job_ad_application']:
            event_data = {
                'id': job_ad_app['id'],
                'job_ad_id': job_ad_app['job_ad_id'],
                'event_code': 'JOB_APP_STATUS',
                'event_action': job_ad_app['status'],
                'event_detail': 'Withdraw job application',
                'is_public': False,
                'created_by': self.__args['created_by'],
                'group_code': self.__args['group_code']
            }

            Job_ad_app_event = JobAdApplicationEvent(event_data)
            Job_ad_app_event.save()

        return retval


class JobAdApplicationQuickHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('columns', type=str)
            self.__reqparse.add_argument('group_by', type=str)
            self.__reqparse.add_argument('from_date_created', type=str)
            self.__reqparse.add_argument('to_date_created', type=str)
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info
        self.__args['group_code'] = self.__userdata['group_code']
        self.__args['person_id'] = self.__userdata['person']['id']

        if self.__args['from_date_created'] is not None:
            self.__args['from_date_created'] = self.__args['from_date_created'] + 'T00:00:00Z'
        if self.__args['to_date_created'] is not None:
            self.__args['to_date_created'] = self.__args['to_date_created'] + 'T23:59:59Z'

        jobAdApplication = JobAdApplicationQuick(self.__args)
        retval = jobAdApplication.get()

        return retval


class JobAdSearchTagHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('tag_code', type=str, required=True)
            self.__reqparse.add_argument('tag_type', type=str, required=True)
            self.__reqparse.add_argument('tag_value', type=str, required=True)

        self.__args = self.__reqparse.parse_args()

    def get(self):
        self.__args['group_code'] = app.config['GROUP_CODE']
        retval = JobAdSearchTag(self.__args).get()

        return retval


class JobAdTagHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__args = self.__reqparse.parse_args()

    def get(self, id):
        if id is None:
            return {'status': 'FAILED'}

        self.__args['id'] = id
        self.__args['group_code'] = app.config['GROUP_CODE']
        job_ad_tag = JobAdTag(self.__args)
        retval = job_ad_tag.get()

        return retval
