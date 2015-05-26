# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class GameServerSchema(SchemaObject):

    """Schema Mixin for GameServer
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Server that provides game interaction in a multiplayer game.
    """

    def __init__(self):
        self.schema = 'GameServer'


class gameProp(SchemaProperty):

    """
    SchemaField for game
    Usage: Include in SchemaObject SchemaFields as your_django_field = gameProp()  
    schema.org description:Video game which is played on this server. Inverse property: gameServer.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference VideoGame"""

    _prop_schema = 'game'
    _expected_schema = 'VideoGame'
    _enum = False
    _format_as = "ForeignKey"


class serverStatusProp(SchemaProperty):

    """
    SchemaField for serverStatus
    Usage: Include in SchemaObject SchemaFields as your_django_field = serverStatusProp()  
    schema.org description:Status of a game server.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference GameServerStatus"""

    _prop_schema = 'serverStatus'
    _expected_schema = 'GameServerStatus'
    _enum = False
    _format_as = "ForeignKey"


class playersOnlineProp(SchemaProperty):

    """
    SchemaField for playersOnline
    Usage: Include in SchemaObject SchemaFields as your_django_field = playersOnlineProp()  
    schema.org description:Number of players on the server.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Integer"""

    _prop_schema = 'playersOnline'
    _expected_schema = 'Integer'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
