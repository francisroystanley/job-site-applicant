import os

BIND_IP = '127.0.0.1'
BIND_PORT = 5000
NOREPLY_EMAIL = os.environ['NOREPLY_EMAIL']

try:
    DEBUG = os.environ['DEBUG']

    if str.upper(DEBUG) == 'TRUE':
        DEBUG = True
    else:
        DEBUG = False
except Exception:
    DEBUG = False

GROUP_CODE = os.environ['GROUP_CODE']

CLIENT_CODE = os.environ['CLIENT_CODE']

ACTIVATE_ACCOUNT_DELETION = os.environ.get('ACTIVATE_ACCOUNT_DELETION', 'FALSE')

VPROFILE_API = os.environ['VPROFILE_API']
VPROFILE_USER = os.environ['VPROFILE_USER']
VPROFILE_PWD = os.environ['VPROFILE_PWD']
VPROFILE_APPNAME = os.environ['VPROFILE_APPNAME']

PONOS_API = os.environ['PONOS_API']
PONOS_USER = os.environ['PONOS_USER']
PONOS_PWD = os.environ['PONOS_PWD']
PONOS_APPNAME = os.environ['PONOS_APPNAME']

HERMES_API = os.environ['HERMES_API']
HERMES_USER = os.environ['HERMES_USER']
HERMES_PWD = os.environ['HERMES_PWD']
HERMES_APPNAME = os.environ['HERMES_APPNAME']

LINKEDIN_CLIENT_ID = os.environ.get('LINKEDIN_CLIENT_ID')
LINKEDIN_CLIENT_SECRET = os.environ.get('LINKEDIN_CLIENT_SECRET')

GOOGLE_RECAPTCHA_CLIENT_KEY = os.environ.get('GOOGLE_RECAPTCHA_CLIENT_KEY')
GOOGLE_RECAPTCHA_KEY = os.environ.get('GOOGLE_RECAPTCHA_KEY')
GOOGLE_RECAPTCHA_URL = os.environ.get('GOOGLE_RECAPTCHA_URL')

MONGO_SERVER = os.environ.get('MONGO_SERVER', 'localhost:27017')
MONGO_DB = os.environ.get('MONGO_DB', 'ponos')
MONGO_USER = os.environ.get('MONGO_USER', 'user')
MONGO_PWD = os.environ.get('MONGO_PWD', 'password')
MONGO_AUTHDB = os.environ.get('MONGO_AUTHDB', 'ponos')

SECRET_KEY = os.environ.get('APP_SECRET', 'mysuperlongsecretkeythatisunique')
