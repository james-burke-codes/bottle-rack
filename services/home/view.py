#!env/bin/python3
import json
import logging

logger = logging.getLogger(__name__)

from bottle_mold import Mold

app = application = Mold()

@app.route('/', method=['GET'])
def index(db):
    return app.template('home', msg='Welcome to Bottle-rack!')
