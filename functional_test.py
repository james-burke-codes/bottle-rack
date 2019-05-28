#!env/bin/python3
import unittest
from boddle import boddle
import logging

import sys

# temp
sys.path.append('../bottle-mold/')

logger = logging.getLogger(__name__)

from home import view as home

SERVICES = (home,)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FunctionalTestCase(unittest.TestCase):

    def setUp(self):
        Session = sessionmaker()
        self.engine = create_engine("sqlite:///:memory:", echo=False)
        Session.configure(bind=self.engine)
        Base.metadata.create_all(self.engine)
        self.db = Session()

        for service in SERVICES:
            service.app.TEMPLATE_PATH.append('./{service}/templates/'.format(service=service.__name__.split('.')[0]))

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_get_home(self):

        with boddle(method='GET'):
            response = home.index(db=self.db)
            assert 'Welcome to Bottle-rack!' in response


if __name__ == '__main__':
    unittest.main()
