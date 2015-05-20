import argparse
import os
import sys
import tests.settings


parent = os.path.dirname(os.path.abspath(__file__))
#print parent
sys.path.insert(0, parent)
tests = parent + '\\tests'
sys.path.insert(0, tests)
schem = parent + '\\schemaorgschemas'
sys.path.insert(0, schem)
#print sys.path

try:
    from schemaorgschemas import *
except ImportError:
    print "bugger override"

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'




def runtests(*argv):
    argv = list(argv) or [
        'tests',
		'schemaorgschemas',
        
    ]
    opts = argparser.parse_args(argv)



    # Run tests.
    from django.core.management import execute_from_command_line
    execute_from_command_line([sys.argv[0], 'test'] + opts.appname)



argparser = argparse.ArgumentParser(description='Process some integers.')
argparser.add_argument('appname', nargs='*')
argparser.add_argument('--no-coverage', dest='coverage', action='store_const',
                       const=False, default=True, help='Do not collect coverage data.')


if __name__ == '__main__':
    runtests(*sys.argv[1:])
