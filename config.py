import os
import sys

"""
This config file is broken up into two sections
- environment variables : which are used while deploying locally and to when deployed as a services
- rack config : which are used specifically for running your services on rack
"""

# RACK CONFIG
## declaring services
services = ('home',)


# ENVIRONMENT VARIABLES
## logging - default INFO
os.environ['LOGGING_LEVEL'] = 'INFO'

## database - default sqlalchemy - sqlite://:memory:
os.environ['DATABASE_ORM'] = 'sqlalchemy'
os.environ['DATABASE_CONNECTION_STRING'] = 'sqlite://'
# e.g.
# sqlite:///test.db
# postgresql://scott:tiger@localhost/mydatabase
# mysql://scott:tiger@localhost/foo

## cors - default disabled
os.environ['CORS_URL'] = ''
