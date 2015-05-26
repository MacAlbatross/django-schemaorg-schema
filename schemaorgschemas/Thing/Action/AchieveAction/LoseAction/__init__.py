# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class LoseActionSchema(SchemaObject):

    """Schema Mixin for LoseAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of being defeated in a competitive activity.
    """

    def __init__(self):
        self.schema = 'LoseAction'


class winnerProp(SchemaProperty):

    """
    SchemaField for winner
    Usage: Include in SchemaObject SchemaFields as your_django_field = winnerProp()  
    schema.org description:A sub property of participant. The winner of the action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'winner'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
