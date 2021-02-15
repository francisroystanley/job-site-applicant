from metis import application

if __name__ == '__main__':
    print(f'Listening on port {application.config["BIND_PORT"]} (DEBUG:{application.config["DEBUG"]}) ')
    application.run(
        host=application.config['BIND_IP'],
        port=application.config['BIND_PORT'],
        debug=True
    )
