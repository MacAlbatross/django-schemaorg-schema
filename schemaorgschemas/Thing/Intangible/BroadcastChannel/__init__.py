# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BroadcastChannelSchema(SchemaObject):

    """Schema Mixin for BroadcastChannel
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A unique instance of a BroadcastService on a CableOrSatelliteService lineup.
    """

    def __init__(self):
        self.schema = 'BroadcastChannel'


class inBroadcastLineupProp(SchemaProperty):

    """
    SchemaField for inBroadcastLineup
    Usage: Include in SchemaObject SchemaFields as your_django_field = inBroadcastLineupProp()  
    schema.org description:The CableOrSatelliteService offering the channel.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference CableOrSatelliteService"""

    _prop_schema = 'inBroadcastLineup'
    _expected_schema = 'CableOrSatelliteService'
    _enum = False
    _format_as = "ForeignKey"


class providesBroadcastServiceProp(SchemaProperty):

    """
    SchemaField for providesBroadcastService
    Usage: Include in SchemaObject SchemaFields as your_django_field = providesBroadcastServiceProp()  
    schema.org description:The BroadcastService offered on this channel.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference BroadcastService"""

    _prop_schema = 'providesBroadcastService'
    _expected_schema = 'BroadcastService'
    _enum = False
    _format_as = "ForeignKey"


class broadcastServiceTierProp(SchemaProperty):

    """
    SchemaField for broadcastServiceTier
    Usage: Include in SchemaObject SchemaFields as your_django_field = broadcastServiceTierProp()  
    schema.org description:The type of service required to have access to the channel (e.g. Standard or Premium).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'broadcastServiceTier'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class broadcastChannelIdProp(SchemaProperty):

    """
    SchemaField for broadcastChannelId
    Usage: Include in SchemaObject SchemaFields as your_django_field = broadcastChannelIdProp()  
    schema.org description:The unique address by which the BroadcastService can be identified in a provider lineup. In US, this is typically a number.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'broadcastChannelId'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
