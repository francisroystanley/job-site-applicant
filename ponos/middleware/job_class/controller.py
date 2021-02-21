from flask import request
from flask_restful import Resource, reqparse

import json


class JobClassHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('job_class_name', type=str, default='')
            self.__reqparse.add_argument('with_category', type=bool, default=False)
        self.__args = self.__reqparse.parse_args()

    def get(self):
        job_class_collection = []
        f = open("config/job_class.json", "r+", encoding="utf-8")
        config_output = f.read()
        job_classes = json.loads(config_output)['job_class']

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
