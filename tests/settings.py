import os
import warnings
warnings.simplefilter('always')


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'schemaorgschemas',
    'tests',
    'django.contrib.sites'
)

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'djangoschema.sqlite',
    },
}

USE_L10N = False

#DATE_FORMAT = 'c'

STATIC_URL = '/static/'

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

ROOT_URLCONF = 'test_urls'
SECRET_KEY = 'secretkey'

SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
