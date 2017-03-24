""" Context Processors """
import time
from .config import CONFIG, SETTINGS, CDN

def buildMethods(app):
    """ Call buildMethods in app.py """
    @app.context_processor
    def inject_config():
        """ Inject's Config into Jinja2 Templating """
        return dict(Config=CONFIG)

    # "CDN" in all Jinja2 Templates
    @app.context_processor
    def inject_cdn():
        """ Inject's CDN into Jinja2 Templating """
        def getCDN(category, location):
            """ Method for dynamic CDN """
            if SETTINGS['Development'] is True:
                return CDN[category] + '/' + location + '?v=' + str(time.time())
            elif SETTINGS['Development'] is False:
                return CDN[category] + '/' + location
        return dict(CDN=getCDN)
