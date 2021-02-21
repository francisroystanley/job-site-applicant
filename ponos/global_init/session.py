from mongoengine import connect


def setup_mongo_session(app):
    server = {
        'db': app.config['MONGO_DB'],
        'host': app.config['MONGO_SERVER'],
        'username': app.config['MONGO_USER'],
        'password': app.config['MONGO_PWD'],
        'authentication_source': app.config['MONGO_AUTHDB'],
        'connect': False
    }

    return connect(**server)
