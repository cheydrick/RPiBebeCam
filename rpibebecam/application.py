from flask import Flask, request

def create_app():
    app = Flask(__name__)

    # flask.pocoo.org/snippets/67/
    @app.route('/shutdown')
    def shutdown_server():
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimError('Not running with the Werkzeug Server')
        func()
        return 'Shutting down server...'

    return app
