from ponos import application

if __name__ == '__main__':
    DEBUG = application.config["DEBUG"]
    print(f'Listening on port {application.config["BIND_PORT"]} (DEBUG: {DEBUG}) ')
    application.run(
        host=application.config['BIND_IP'],
        port=application.config['BIND_PORT'],
        debug=DEBUG
    )
