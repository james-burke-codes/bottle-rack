#!env/bin/python3
import json
import logging

from bottle_mold import Mold

logger = logging.getLogger(__name__)

app = application = Mold()

@app.route('/', method=['GET'])
def index():
    return app.template('home', msg='Welcome to Bottle-rack!')

