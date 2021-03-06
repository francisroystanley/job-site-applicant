import os
from flask import redirect, render_template, request, url_for
from flask_login import login_required, logout_user, current_user


from .global_init import app, login_manager
from .middleware import MiddleWare, User


login_manager.login_view = 'index'


@login_manager.user_loader
def load_user(user_id):
    """
        Validate user identity via cookie
        And loads them
    """
    user = User.load_session(user_id)
    if user is not None:
        user.extend_session()
    return user


@login_manager.request_loader
def load_user_from_request(request):
    """
        Validate user identity via Request Headers
        Ussually token based authentication
    """
    session_token = request.headers.get('Authorization')
    if session_token:
        user = User.load_session_token(session_token)
        return user
    return None


@login_manager.unauthorized_handler
def unauthorized_handler():
    if request.is_xhr:
        return {'status': 'not authenticated'}, 401
    else:
        return redirect(url_for("login", next=request.endpoint))


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, '..',
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


# @app.route('/login')
# def login():
#     logout_user()
#     return redirect('/signin')


# @app.route('/logout')
# @login_required
# def logout():
#     current_user.remove()
#     logout_user()
#     return redirect('/')


# @app.route('/signin', endpoint='signin')
# @app.route('/register', endpoint='register')
# @app.route('/forgotpassword', endpoint='forgot_password')
# def guest():
#     if current_user.is_authenticated:
#         user_info = current_user.info
#         return redirect('/')
#     else:
#         user_info = None

#     return render_template('index.html', user_info=user_info, client_code=app.config['CLIENT_CODE'])


@app.route('/', endpoint='index')
def index(path=None):
    return ""


# @app.route('/myaccount', endpoint='myaccount')
# @app.route('/myaccount/<path:path>', endpoint='myaccountpages')
# @app.route('/profile', endpoint='profile')
# @app.route('/profile/edit', endpoint='profile_edit')
# @app.route('/profile/view', endpoint='profile_view')
# @login_required
# def profile(path=None):
#     user_info = current_user.info
#     banner_meta = 'ALL'
#     return render_template('index.html', user_info=user_info, banner_meta=banner_meta, client_code=app.config['CLIENT_CODE'])


# @app.errorhandler(404)
# def page_not_found(e):
#     if current_user.is_authenticated:
#         user_info = current_user.info
#     else:
#         user_info = None

#     return render_template('index.html', user_info=user_info, client_code=app.config['CLIENT_CODE'])


api = MiddleWare(app)
application = app
