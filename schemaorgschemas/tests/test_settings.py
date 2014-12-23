import os
BASE_DIR = os.path.dirname(__file__)

INSTALLED_APPS = (
'django.contrib.auth',
'django.contrib.sessions',
'django.contrib.contenttypes',
'django.contrib.admin',
'schemaorgschemas',
)
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
}
}

MIDDLEWARE_CLASSES = (
'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
)
ROOT_URLCONF = 'test_urls'
SECRET_KEY = 'secretkey'
SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
# http://djangosnippets.org/snippets/646/
