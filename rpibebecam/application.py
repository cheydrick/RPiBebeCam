from flask import Flask, request, render_template, Blueprint
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View

def create_app():
    app = Flask(__name__)

    app.register_blueprint(viewer)
    Bootstrap(app)
    nav.init_app(app)

    # flask.pocoo.org/snippets/67/
    @app.route('/shutdown')
    def shutdown_server():
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimError('Not running with the Werkzeug Server')
        func()
        return 'Shutting down server...'

    return app

viewer = Blueprint('viewer', __name__)
nav = Nav()

@viewer.route('/')
def index():
    return render_template('index.html')

@nav.navigation()
def navbar():
    return Navbar('RPiBebeCam', View('Home', 'viewer.index'))
