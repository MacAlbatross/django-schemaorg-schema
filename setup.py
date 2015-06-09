import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'READ.md')) as readme:
    README = readme.read()

setup(
    name='django-schemaorg-schema',
    version='1.0.2',
    packages=['schemaorgschemas'],
    include_package_data=True,
    license='BSD License',  # example license
    description='This application provides mixins for Django models and template tags that format their values according to the schema.org specificiations.',
    long_description=README,
    url='https://github.com/MacAlbatross/django-schemaorg-schema',
    author='Paul Fleetwood',
    author_email='schema@paulfleetwood.co.uk',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)