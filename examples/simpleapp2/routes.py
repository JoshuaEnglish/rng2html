from bottle import Bottle, view, static_file

from db import get_addresses

app = Bottle()

class Utils:
    """Utils
    Utility functions to pass through to templates.
    """

    def get_url(self, thing):
        return app.get_url(thing)

utils = Utils()

@app.route('/')
@app.route('/index')
@view('index')
def hello():
    return dict(tools=utils, addressBook=get_addresses())

@app.route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='static')
    
@app.route('/hardcoded')
@view('hardcoded')
def hardcoded():
    return dict(tools=utils)
    
rapp = app