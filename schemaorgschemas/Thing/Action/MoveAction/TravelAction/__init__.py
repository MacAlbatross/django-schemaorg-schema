# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.MoveAction import fromLocationProp, toLocationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TravelActionSchema(SchemaObject):

    """Schema Mixin for TravelAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of traveling from an fromLocation to a destination by a specified mode of transport, optionally with participants.
    """

    def __init__(self):
        self.schema = 'TravelAction'


class distanceProp(SchemaProperty):

    """
    SchemaField for distance
    Usage: Include in SchemaObject SchemaFields as your_django_field = distanceProp()  
    schema.org description:The distance travelled, e.g. exercising or travelling.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Distance"""

    _prop_schema = 'distance'
    _expected_schema = 'Distance'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
