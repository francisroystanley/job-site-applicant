from flask import request
from flask_restful import Resource, reqparse

import json


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
        f = open("config/city.json", "r+", encoding="utf-8")
        config_output = f.read()
        cities = json.loads(config_output)['city']
        for city in cities:
            city_data = {
                'city_code': city['city_code'],
                'city_name': city['city_name'],
                'province_code': city['province_code'],
                'province_name': city['province_name'],
                'country_code': city['country_code']
            }
            city_collection.append(city_data)

        return {
            'status': 'SUCCESS',
            'cities': city_collection
        }


class CountryHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('country_name', type=str)
            self.__reqparse.add_argument('country_code', type=str, default=None)

        self.__args = self.__reqparse.parse_args()

    def get(self):
        country_collection = []
        f = open("config/country.json", "r+", encoding="utf-8")
        config_output = f.read()
        countries = json.loads(config_output)['country']
        for country in countries:
            country_data = {
                'country_code': country['code'],
                'country_name': country['name']
            }
            country_collection.append(country_data)

        return {
            'status': 'SUCCESS',
            'countrys': country_collection
        }


class ProvinceHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        if request.method in ('GET'):
            self.__reqparse.add_argument('province_name', type=str)
            self.__reqparse.add_argument('province_code', type=str, default=None)

        self.__args = self.__reqparse.parse_args()

    def get(self):
        province_collection = []
        f = open("config/province.json", "r+", encoding="utf-8")
        config_output = f.read()
        provinces = json.loads(config_output)['province']
        for province in provinces:
            province_data = {
                'province_code': province['province_code'],
                'province_name': province['province_name'],
                'country_code': province['country_code']
            }
            province_collection.append(province_data)

        return {
            'status': 'SUCCESS',
            'provinces': province_collection
        }
