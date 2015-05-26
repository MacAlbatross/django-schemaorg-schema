# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.PlayAction import audienceProp, eventProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PerformActionSchema(SchemaObject):

    """Schema Mixin for PerformAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of participating in performance arts.
    """

    def __init__(self):
        self.schema = 'PerformAction'


class entertainmentBusinessProp(SchemaProperty):

    """
    SchemaField for entertainmentBusiness
    Usage: Include in SchemaObject SchemaFields as your_django_field = entertainmentBusinessProp()  
    schema.org description:A sub property of location. The entertainment business where the action occurred.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference EntertainmentBusiness"""

    _prop_schema = 'entertainmentBusiness'
    _expected_schema = 'EntertainmentBusiness'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
