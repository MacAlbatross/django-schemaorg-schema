# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.AssessAction.ChooseAction import actionOptionProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class VoteActionSchema(SchemaObject):

    """Schema Mixin for VoteAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of expressing a preference from a fixed/finite/structured set of choices/options.
    """

    def __init__(self):
        self.schema = 'VoteAction'


class candidateProp(SchemaProperty):

    """
    SchemaField for candidate
    Usage: Include in SchemaObject SchemaFields as your_django_field = candidateProp()  
    schema.org description:A sub property of object. The candidate subject of this action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'candidate'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
