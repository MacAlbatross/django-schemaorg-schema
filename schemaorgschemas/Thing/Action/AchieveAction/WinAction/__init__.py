# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class WinActionSchema(SchemaObject):

    """Schema Mixin for WinAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of achieving victory in a competitive activity.
    """

    def __init__(self):
        self.schema = 'WinAction'


class loserProp(SchemaProperty):

    """
    SchemaField for loser
    Usage: Include in SchemaObject SchemaFields as your_django_field = loserProp()  
    schema.org description:A sub property of participant. The loser of the action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'loser'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"
