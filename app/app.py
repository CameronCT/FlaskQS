""" Main Module where magic happens """
from .config import CONFIG, SETTINGS, CDN
from .methods import buildMethods
from flask import Flask, url_for, render_template

def init():
    """ Initiate Flask Application """
    app = Flask(__name__, static_folder='assets')
    app.debug = SETTINGS['Debug']
    buildMethods(app)

    @app.route('/')
    def projects():
        """ Test """
        return render_template('index.html')

    return app
