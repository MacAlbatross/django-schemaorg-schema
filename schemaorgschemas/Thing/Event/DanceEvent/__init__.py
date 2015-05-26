# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Event import inLanguageProp, attendeeProp, performerProp, endDateProp, startDateProp, previousStartDateProp, superEventProp, reviewProp, recordedInProp, aggregateRatingProp, subEventProp, offersProp, eventStatusProp, typicalAgeRangeProp, durationProp, workPerformedProp, organizerProp, doorTimeProp, locationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DanceEventSchema(SchemaObject):

    """Schema Mixin for DanceEvent
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Event type: A social dance.
    """

    def __init__(self):
        self.schema = 'DanceEvent'


# schema.org version 2.0
