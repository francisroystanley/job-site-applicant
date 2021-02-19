from flask import request
from flask_restful import Resource, reqparse

from ..document import JobClassSchema

import re


class JobClassHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('job_class_name', type=str, default='')
            self.__reqparse.add_argument('with_category', type=bool, default=False)
        self.__args = self.__reqparse.parse_args()

    def get(self):
        job_class_name = self.__args['job_class_name']
        regex = re.compile('.*{}.*'.format(job_class_name), re.IGNORECASE)
        job_class_collection = []
        job_classes = JobClassSchema.objects(job_class_name=regex)

        for job_class in job_classes:
            job_class_data = {
                'job_class_code': job_class['job_class_code'],
                'job_class_name': job_class['job_class_name']
            }
            if self.__args['with_category']:
                job_class_data['job_class_category'] = job_class['job_class_category']

            job_class_collection.append(job_class_data)

        retval = {
            'status': 'SUCCESS',
            'job_class': job_class_collection
        }

        return retval
