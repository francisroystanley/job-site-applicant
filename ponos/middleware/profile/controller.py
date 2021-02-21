from flask import request
from flask_restful import Resource, reqparse
from flask_login import login_required

import json


class CitizenshipHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('citizenship_name', type=str, default='')

        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        citizenship_collection = []
        f = open("config/citizenship.json", "r+", encoding="utf-8")
        config_output = f.read()
        citizenships = json.loads(config_output)['citizenship']
        for citizenship in citizenships:
            citizenship_data = {
                'code': citizenship['code'],
                'name': citizenship['name']
            }
            citizenship_collection.append(citizenship_data)

        return {
            'status': 'SUCCESS',
            'citizenships': citizenship_collection
        }


class CourseHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('course_name', type=str, default='')

        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        course_collection = []
        f = open("config/course.json", "r+", encoding="utf-8")
        config_output = f.read()
        courses = json.loads(config_output)['course']
        for course in courses:
            course_data = {
                'course_code': course['code'],
                'course_name': course['name']
            }
            course_collection.append(course_data)

        return {
            'status': 'SUCCESS',
            'courses': course_collection
        }


class SchoolHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('school_name', type=str, default='')

        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        school_collection = []
        f = open("config/school.json", "r+", encoding="utf-8")
        config_output = f.read()
        schools = json.loads(config_output)['school']
        for school in schools:
            school_data = {
                'school_code': school['code'],
                'school_name': school['name']
            }
            school_collection.append(school_data)

        return {
            'status': 'SUCCESS',
            'schools': school_collection
        }


class ReligionHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('religion_name', type=str, default='')

        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        religion_collection = []
        f = open("config/religion.json", "r+", encoding="utf-8")
        config_output = f.read()
        religions = json.loads(config_output)['religion']
        for religion in religions:
            religion_data = {
                'code': religion['code'],
                'name': religion['name']
            }
            religion_collection.append(religion_data)

        return {
            'status': 'SUCCESS',
            'religions': religion_collection
        }
