from flask_restful import Resource, reqparse

from ponos.global_init import app


class EnvHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__args = self.__reqparse.parse_args()

    def get(self):
        return {
            "status": 'SUCCESS',
            "env": {
                "client_code": app.config['CLIENT_CODE']
            }
        }
