# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BroadcastServiceSchema(SchemaObject):

    """Schema Mixin for BroadcastService
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A delivery service through which content is provided via broadcast over the air or online.
    """

    def __init__(self):
        self.schema = 'BroadcastService'


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


class broadcastAffiliateOfProp(SchemaProperty):

    """
    SchemaField for broadcastAffiliateOf
    Usage: Include in SchemaObject SchemaFields as your_django_field = broadcastAffiliateOfProp()  
    schema.org description:The media network(s) whose content is broadcast on this station.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'broadcastAffiliateOf'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


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


class broadcastDisplayNameProp(SchemaProperty):

    """
    SchemaField for broadcastDisplayName
    Usage: Include in SchemaObject SchemaFields as your_django_field = broadcastDisplayNameProp()  
    schema.org description:The name displayed in the channel guide. For many US affiliates, it is the network name.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'broadcastDisplayName'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class broadcastTimezoneProp(SchemaProperty):

    """
    SchemaField for broadcastTimezone
    Usage: Include in SchemaObject SchemaFields as your_django_field = broadcastTimezoneProp()  
    schema.org description:The timezone in ISO 8601 format for which the service bases its broadcasts.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'broadcastTimezone'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
