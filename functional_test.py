#!env/bin/python3
import os
import unittest
from boddle import boddle
import logging

# temp until mold is working
import sys
sys.path.append('../bottle-mold/')

logger = logging.getLogger(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FunctionalTestCase(unittest.TestCase):

    def setUp(self):
        # create database session
        Session = sessionmaker()
        self.engine = create_engine("sqlite:///:memory:", echo=False)
        Session.configure(bind=self.engine)
        Base.metadata.create_all(self.engine)
        self.db = Session()

        # import services
        self.services = dict()
        for service in list(filter(lambda f: f.is_dir(), list(os.scandir('./services')))):
            mod = __import__('services.{service}.view'.format(service=service.name), fromlist=['app'])
            self.services[service.name] = mod #getattr(mod, 'app')
            self.services[service.name].app.TEMPLATE_PATH.append('./services/{service}/templates/'.format(service=service.name))

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_home_get(self):
        with boddle(method='GET'):
            response = self.services['home'].index(db=self.db)
            assert 'Welcome to Bottle-rack!' in response

    def test_list_create_item(self):
        with boddle(method='GET'):
            response = self.services['list'].create(db=self.db)
            assert 'Welcome to Bottle-rack!' in response



if __name__ == '__main__':
    unittest.main()
