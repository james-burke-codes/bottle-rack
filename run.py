#!env/bin/python3
import os
import logging
import argparse
import importlib

import config

logger = logging.getLogger(__name__)
logging.basicConfig(format="%(asctime)s:%(name)s:%(lineno)s:%(levelname)s - %(message)s",
                    level=os.environ.get('LOGGING_LEVEL'))

from bottle_mold import Mold
app = application = Mold()

for service in list(filter(lambda f: f.is_dir(), list(os.scandir('./services')))):
    mod = __import__('services.{service}.view'.format(service=service.name), fromlist=['app'])
    sub_app = getattr(mod, 'app')
    app.merge(sub_app)

    app.TEMPLATE_PATH.append('./services/{service}/templates/'.format(service=service.name))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--listen", dest="listen", type=str, default="localhost", help="IP Address to listen on")
    parser.add_argument("-p", "--port", dest="port", type=int, default=8090, help="Port to listen on")
    parser.add_argument("-d", "--debug", dest="debug", type=bool, default=True, help="Enable Bottle debug mode")
    pargs = vars(parser.parse_args())

    app.run(host=pargs["listen"], port=pargs["port"], debug=pargs["debug"], reloader=True)
