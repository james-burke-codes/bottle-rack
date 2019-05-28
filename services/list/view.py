#!env/bin/python3
import json
import logging

logger = logging.getLogger(__name__)

from bottle_mold import Mold

app = application = Mold()

from .model import List

@app.route('/list/create', method=['POST'])
def create(db):
    reqdata = app.request.json
    logger.info(reqdata)
    return {}

