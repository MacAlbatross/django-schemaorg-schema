# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.BroadcastChannel import inBroadcastLineupProp, providesBroadcastServiceProp, broadcastServiceTierProp, broadcastChannelIdProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RadioChannelSchema(SchemaObject):

    """Schema Mixin for RadioChannel
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A unique instance of a radio BroadcastService on a CableOrSatelliteService lineup.
    """

    def __init__(self):
        self.schema = 'RadioChannel'


# schema.org version 2.0
