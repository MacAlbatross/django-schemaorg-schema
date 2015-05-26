# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class GameServerStatusSchema(SchemaObject):

    """Schema Mixin for GameServerStatus
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Status of a game server.
    """

    def __init__(self):
        self.schema = 'GameServerStatus'


/SERVERSTATUS_CHOICES = (
    ('/OFFLINETEMPORARILY', '/OfflineTemporarily'),
    ('/ONLINE', '/Online'),
    ('/ONLINEFULL', '/OnlineFull'),
    ('/OFFLINEPERMANENTLY', '/OfflinePermanently'),
)


class / serverStatusProp(SchemaEnumProperty):

    """
    Enumeration for /serverStatus
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/serverStatus'
    choices = /SERVERSTATUS_CHOICES
    _format_as = "enum"
    adapter = {
        '/OFFLINETEMPORARILY': '/OfflineTemporarily',
        '/ONLINE': '/Online',
        '/ONLINEFULL': '/OnlineFull',
        '/OFFLINEPERMANENTLY': '/OfflinePermanently',
    }


# schema.org version 2.0
