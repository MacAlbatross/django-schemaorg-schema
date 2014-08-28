# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BroadcastServiceSchema(SchemaObject):

    """Schema Mixin for BroadcastService
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A delivery service through which content is provided via broadcast over the air or online.
    """

    def __init__(self):
        self.schema = 'BroadcastService'


class broadcasterProp(SchemaProperty):

    """
    SchemaField for broadcaster
    Usage: Include in SchemaObject SchemaFields as your_django_field = broadcasterProp()
    schema.org description:The organization owning or operating the broadcast service.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'broadcaster'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class parentServiceProp(SchemaProperty):

    """
    SchemaField for parentService
    Usage: Include in SchemaObject SchemaFields as your_django_field = parentServiceProp()
    schema.org description:A broadcast service to which the broadcast service may belong to such as regional variations of a national channel.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference BroadcastService"""

    _prop_schema = 'parentService'
    _expected_schema = 'BroadcastService'
    _enum = False
    _format_as = "ForeignKey"


class areaProp(SchemaProperty):

    """
    SchemaField for area
    Usage: Include in SchemaObject SchemaFields as your_django_field = areaProp()
    schema.org description:The area within which users can expect to reach the broadcast service.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'area'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"
