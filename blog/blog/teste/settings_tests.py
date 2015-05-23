#coding:utf-8
import logging

from settings import *

logging.disable(logging.INFO)


DEBUG = True 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME':':memory:',
    }
}

#
# Application
#
INSTALLED_APPS = list(INSTALLED_APPS)
INSTALLED_APPS += [
    'django_nose',
]


#
# Test settings
#
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
BROKER_BACKEND = 'memory'
SOUTH_TESTS_MIGRATE = False
SKIP_SLOW_TESTS = True
RUN_SLOW_TESTS = False
