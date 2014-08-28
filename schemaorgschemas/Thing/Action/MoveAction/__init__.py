# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MoveActionSchema(SchemaObject):

    """Schema Mixin for MoveAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of an agent relocating to a place.Related actions:TransferAction: Unlike TransferAction, the subject of the move is a living Person or Organization rather than an inanimate object.
    """

    def __init__(self):
        self.schema = 'MoveAction'


class fromLocationProp(SchemaProperty):

    """
    SchemaField for fromLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = fromLocationProp()  
    schema.org description:A sub property of location. The original location of the object or the agent before the action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'fromLocation'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


class toLocationProp(SchemaProperty):

    """
    SchemaField for toLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = toLocationProp()  
    schema.org description:A sub property of location. The final location of the object or the agent after the action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'toLocation'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"
