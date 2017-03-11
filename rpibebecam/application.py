from flask import Flask, request, render_template, Blueprint, url_for, send_file
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from camera.camera import Camera
import os

def create_app():
    app = Flask(__name__)

    app.register_blueprint(viewer)
    Bootstrap(app)
    nav.init_app(app)
    
    if os.environ.get("WERKZEUG_RUN_MAIN") == 'true':
        print 'Initializing Camera'
        picamera.initialize()
    
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
picamera = Camera()

@viewer.route('/')
def index():
    return render_template('index.html')

@viewer.route('/frame')
def frame():
    if picamera.initialized == False:
        return 'Camera() isn''t initialized!'
    elif picamera.frame == None:
        return 'No available frame in Camera()'
    else:
        return send_file(picamera.get_frame(), mimetype='image/jpeg')

@nav.navigation()
def navbar():
    return Navbar('RPiBebeCam', View('Home', 'viewer.index'))
