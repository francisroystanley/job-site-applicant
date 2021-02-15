from flask_login import LoginManager
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_ipaddr
from .flask_app import create_flask_app
from .session import setup_mongo_session
from .logger import setup_logger
from .model import GenericModel
from .permission import require_permission

from metis.plugin import VProfile, MetisApi, HermesApi, LinkedInApi

app = create_flask_app()
logger = setup_logger(app)
hermes = HermesApi(app)
vprofile = VProfile(app)
metisapi = MetisApi(app)
linkedin = LinkedInApi(app)

limiter = Limiter(
    app,
    key_func=get_ipaddr,
    default_limits=["10000 per day", "1000 per hour"]
)

login_manager = LoginManager(app)
login_manager.login_view = "login"

mongo = setup_mongo_session(app)


CORS(app, resources=r'/api/*')
