import os, sys
#os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
parent = os.path.dirname(os.path.dirname(os.path.dirname(
os.path.abspath('__file__'))))
sys.path.insert(0, parent)

from django.conf import settings

from django.test.simple import DjangoTestSuiteRunner
from schemaorgschemas.tests.test_templatetags import SchemaTemplateTagTester

def run_tests():
    return DjangoTestSuiteRunner(failfast=False).run_tests(['schemaorgschemas.tests.test_templatetags.SchemaTemplateTagTester',], verbosity=1, interactive=True)

if __name__ == '__main__':
    if run_tests():
        sys.exit(1)