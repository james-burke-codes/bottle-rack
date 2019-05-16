import os

"""
This config file is broken up into two sections
- environment variables : which are used while deploying locally and to when deployed as a services
- rack config : which are used specifically for running your services on rack
"""

# ENVIRONMENT VARIABLES
## logging
os.environ['LOGGING_LEVEL'] = 'INFO'

## database
os.environ['DATABASE_ORM'] = 'sqlalchemy'
os.environ['DBMS'] = 'postgresql'
os.environ['DATABASE_PASS'] = ''
os.environ['DATABASE_HOST'] = ''
os.environ['DATABASE_PORT'] = ''
os.environ['DATABASE'] = ''

## cors
os.environ['CORS_URL'] = ''

# RACK CONFIG
## declaring services
services = ('home',)
