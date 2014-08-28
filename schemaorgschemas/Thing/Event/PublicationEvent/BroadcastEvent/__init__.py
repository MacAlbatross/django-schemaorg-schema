# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Event.PublicationEvent import publishedOnProp, freeProp
from schemaorgschemas.Thing.Event import startDateProp, attendeeProp, performerProp, endDateProp, previousStartDateProp, superEventProp, subEventProp, offersProp, eventStatusProp, typicalAgeRangeProp, durationProp, workPerformedProp, doorTimeProp, locationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BroadcastEventSchema(SchemaObject):

    """Schema Mixin for BroadcastEvent
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An over the air or online broadcast event.
    """

    def __init__(self):
        self.schema = 'BroadcastEvent'
