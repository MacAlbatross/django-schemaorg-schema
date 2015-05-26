# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class GamePlayModeSchema(SchemaObject):

    """Schema Mixin for GamePlayMode
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates whether this game is multi-player, co-op or single-player.
    """

    def __init__(self):
        self.schema = 'GamePlayMode'


/PLAYMODE_CHOICES = (
    ('/MULTIPLAYER', '/MultiPlayer'),
    ('/SINGLEPLAYER', '/SinglePlayer'),
    ('/COOP', '/CoOp'),
)


class / playModeProp(SchemaEnumProperty):

    """
    Enumeration for /playMode
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/playMode'
    choices = /PLAYMODE_CHOICES
    _format_as = "enum"
    adapter = {
        '/MULTIPLAYER': '/MultiPlayer',
        '/SINGLEPLAYER': '/SinglePlayer',
        '/COOP': '/CoOp',
    }


# schema.org version 2.0
