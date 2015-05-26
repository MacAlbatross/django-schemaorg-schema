# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Event.PublicationEvent import isAccessibleForFreeProp, publishedOnProp
from schemaorgschemas.Thing.Event import inLanguageProp, attendeeProp, performerProp, endDateProp, startDateProp, previousStartDateProp, superEventProp, reviewProp, recordedInProp, aggregateRatingProp, subEventProp, offersProp, eventStatusProp, typicalAgeRangeProp, durationProp, workPerformedProp, organizerProp, doorTimeProp, locationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OnDemandEventSchema(SchemaObject):

    """Schema Mixin for OnDemandEvent
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A publication event e.g. catch-up TV or radio podcast, during which a program is available on-demand.
    """

    def __init__(self):
        self.schema = 'OnDemandEvent'


# schema.org version 2.0
