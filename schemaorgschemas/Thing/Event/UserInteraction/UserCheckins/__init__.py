# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Event import startDateProp, attendeeProp, performerProp, endDateProp, previousStartDateProp, superEventProp, subEventProp, offersProp, eventStatusProp, typicalAgeRangeProp, durationProp, workPerformedProp, doorTimeProp, locationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class UserCheckinsSchema(SchemaObject):

    """Schema Mixin for UserCheckins
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    User interaction: Check-in at a place.
    """

    def __init__(self):
        self.schema = 'UserCheckins'
