# bottle-rack

[![codecov](https://codecov.io/gh/peregrinius/bottle-rack/branch/master/graph/badge.svg)](https://codecov.io/gh/peregrinius/bottle-rack) [![Build Status](https://travis-ci.org/peregrinius/bottle-rack.svg?branch=master)](https://travis-ci.org/peregrinius/bottle-rack)

Similar to the concept of Flask Blueprints, Bottle-rack simplifies managing multiple Bottle services. You can use Bottle-rack to manage running and developing microservices locally and later deploying as separate services.


## Install & Run

```
git clone git@github.com:peregrinius/bottle-rack.git
cd bottle-rack

# if you want to use a virtual environment
virtualenv -p $(which python3) venv
source venv/bin/activate

pip install -r requirements.txt

python run.py
```


## Dependencies

The only required dependency is bottle-mold, which is used to promote cleaner code in your services by removing boilerplate code from services. It includes:

* handling CORS
* ORM plugin configuration

Note: sqlalchemy is also provided by default but only used for demonstation purposes

## Getting Started

### Configuration

Configuration is managed through the `config.py` file, here you can setup parameters for:

* Logging
* CORS
* ORM configuration
* registering services

The config file consists of two kinds of two ways of setting values, with environment variables and as variables.

* Environment variables should be used for values that need to be set for deploying services independently of bottle-rack
* Variables should be used for values that are only required for running the web service using bottle-rack
