from flask import make_response, current_app
from flask_restful import Resource, reqparse
from flask_login import login_required

from .model import Attachment, Image, ProfilePhoto, Resume

import datetime


class AttachmentHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__reqparse.add_argument('name', type=str, required=True, location='args')
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self, file_type, file_name):
        self.__args['acct_code'] = current_app.config['GROUP_CODE']
        self.__args['file_name'] = file_name
        self.__args['file_type'] = file_type
        ext = file_name.split(".")[2]
        name = self.__args['name']
        profile_attachment = Attachment(self.__args)
        profile_attachment.get()
        attachment = profile_attachment.download()
        retval = make_response(attachment)
        retval.headers['Content-Disposition'] = f'inline; filename="{name}"'
        if ext in ('pdf', 'doc', 'docx'):
            content_type = 'application'
        else:
            content_type = 'image'

        retval.headers['Content-Type'] = f'{content_type}/{ext}'
        retval.headers['cache-control'] = 'private, max-age=43200'
        now = datetime.datetime.utcnow()
        expires = now + datetime.timedelta(seconds=43200)
        expires = expires.strftime('%a, %d %b %Y %H:%M:%S GMT')
        retval.headers['expires'] = expires

        return retval


class ImageHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__args = self.__reqparse.parse_args()

    def get(self, image, file_name):
        self.__args['acct_code'] = current_app.config['GROUP_CODE']
        self.__args['image'] = image
        self.__args['file_name'] = file_name
        try:
            image = Image(self.__args)
        except Exception as e:
            retval = {'status': 'FAILED'}
            self.__app.logger.error(e)
            return retval, 400

        getImage = image.get()
        if getImage['status'] == 'FAILED':
            return getImage, 400

        photo = image.download()
        retval = make_response(photo)
        retval.headers['Content-Type'] = 'image/jpeg'
        retval.headers['cache-control'] = 'private, max-age=43200'
        now = datetime.datetime.utcnow()
        expires = now + datetime.timedelta(seconds=43200)
        expires = expires.strftime('%a, %d %b %Y %H:%M:%S GMT')
        retval.headers['expires'] = expires

        return retval


class PhotoHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__args = self.__reqparse.parse_args()

    def get(self, file_name):
        self.__args['acct_code'] = current_app.config['GROUP_CODE']
        self.__args['file_name'] = file_name
        profile_photo = ProfilePhoto(self.__args)
        profile_photo.get()
        photo = profile_photo.download()
        retval = make_response(photo)
        retval.headers['Content-Type'] = 'image/jpeg'
        retval.headers['cache-control'] = 'private, max-age=43200'
        now = datetime.datetime.utcnow()
        expires = now + datetime.timedelta(seconds=43200)
        expires = expires.strftime('%a, %d %b %Y %H:%M:%S GMT')
        retval.headers['expires'] = expires

        return retval


class ResumeHandler(Resource):
    def __init__(self):
        self.__reqparse = reqparse.RequestParser()
        self.__reqparse.add_argument('name', type=str, required=True, location='args')
        self.__args = self.__reqparse.parse_args()

    @login_required
    def get(self, file_name):
        self.__args['acct_code'] = current_app.config['GROUP_CODE']
        self.__args['file_name'] = file_name
        ext = file_name.split(".")[2]
        name = self.__args['name']
        profile_resume = Resume(self.__args)
        profile_resume.get()
        resume = profile_resume.download()
        retval = make_response(resume)
        retval.headers['Content-Disposition'] = f'inline; filename="{name}"'
        retval.headers['Content-Type'] = f'application/{ext}'
        retval.headers['cache-control'] = 'private, max-age=43200'
        now = datetime.datetime.utcnow()
        expires = now + datetime.timedelta(seconds=43200)
        expires = expires.strftime('%a, %d %b %Y %H:%M:%S GMT')
        retval.headers['expires'] = expires

        return retval
