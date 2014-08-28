# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EntryPointSchema(SchemaObject):

    """Schema Mixin for EntryPoint
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An entry point, within some Web-based protocol.
    """

    def __init__(self):
        self.schema = 'EntryPoint'


class applicationProp(SchemaProperty):

    """
    SchemaField for application
    Usage: Include in SchemaObject SchemaFields as your_django_field = applicationProp()  
    schema.org description:An application that can complete the request.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference SoftwareApplication"""

    _prop_schema = 'application'
    _expected_schema = 'SoftwareApplication'
    _enum = False
    _format_as = "ForeignKey"


class encodingTypeProp(SchemaProperty):

    """
    SchemaField for encodingType
    Usage: Include in SchemaObject SchemaFields as your_django_field = encodingTypeProp()  
    schema.org description:The supported encoding type(s) for an EntryPoint request.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'encodingType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class contentTypeProp(SchemaProperty):

    """
    SchemaField for contentType
    Usage: Include in SchemaObject SchemaFields as your_django_field = contentTypeProp()  
    schema.org description:The supported content type(s) for an EntryPoint response.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'contentType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class httpMethodProp(SchemaProperty):

    """
    SchemaField for httpMethod
    Usage: Include in SchemaObject SchemaFields as your_django_field = httpMethodProp()  
    schema.org description:An HTTP method that specifies the appropriate HTTP method for a request to an HTTP EntryPoint. Values are capitalized strings as used in HTTP.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'httpMethod'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
