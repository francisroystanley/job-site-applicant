from flask import request
from flask_restful import Resource, reqparse
from flask_login import login_required, current_user

from .model import Place
from ..document import CitySchema, ProvinceSchema

import re


class PlaceHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('sample_parameter', type=str)
        else:
            self.__reqparse.add_argument('sample_parameter', type=str, required=True)
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self):
        self.__userdata = current_user.info

        place = Place(self.__args)
        retval = place.get()

        return retval

    @login_required
    def post(self):
        self.__userdata = current_user.info

        place = Place(self.__args)
        retval = place.save()

        return retval


class CityHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('city_name', type=str)
            self.__reqparse.add_argument('city_code', type=str, default=None)
            self.__reqparse.add_argument('province_name', type=str)
            self.__reqparse.add_argument('province_code', type=str)
        self.__args = self.__reqparse.parse_args()

    def get(self):
        city_collection = []
        if self.__args['city_name']:
            self.__args['city_name'] = re.compile('.*{}.*'.format(self.__args['city_name']), re.IGNORECASE)

        args = {k: v for k, v in self.__args.items() if v is not None}
        cities = CitySchema.objects(**args)

        for city in cities:
            city_data = {
                'city_code': city['city_code'],
                'city_name': city['city_name'],
                'province_code': city['province_code'],
                'province_name': city['province_name'],
                'country_code': city['country_code']
            }

            city_collection.append(city_data)

        retval = {
            'status': 'SUCCESS',
            'cities': city_collection
        }

        return retval


class ProvinceHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('province_name', type=str)
            self.__reqparse.add_argument('province_code', type=str, default=None)
        self.__args = self.__reqparse.parse_args()

    def get(self):
        province_name = self.__args['province_name']
        province_code = self.__args['province_code']

        province_collection = []

        if province_code is None:
            regex = re.compile('.*{}.*'.format(province_name), re.IGNORECASE)
            provinces = ProvinceSchema.objects(province_name=regex)
        else:
            provinces = ProvinceSchema.objects(province_code=province_code)

        for province in provinces:
            province_data = {
                'province_code': province['province_code'],
                'province_name': province['province_name'],
                'country_code': province['country_code']
            }

            province_collection.append(province_data)

        retval = {
            'status': 'SUCCESS',
            'provinces': province_collection
        }

        return retval
