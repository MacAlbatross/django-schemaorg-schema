# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Event.PublicationEvent import isAccessibleForFreeProp, publishedOnProp
from schemaorgschemas.Thing.Event import inLanguageProp, attendeeProp, performerProp, endDateProp, startDateProp, previousStartDateProp, superEventProp, reviewProp, recordedInProp, aggregateRatingProp, subEventProp, offersProp, eventStatusProp, typicalAgeRangeProp, durationProp, workPerformedProp, organizerProp, doorTimeProp, locationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BroadcastEventSchema(SchemaObject):

    """Schema Mixin for BroadcastEvent
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An over the air or online broadcast event.
    """

    def __init__(self):
        self.schema = 'BroadcastEvent'


class isLiveBroadcastProp(SchemaProperty):

    """
    SchemaField for isLiveBroadcast
    Usage: Include in SchemaObject SchemaFields as your_django_field = isLiveBroadcastProp()  
    schema.org description:True is the broadcast is of a live event.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'isLiveBroadcast'
    _expected_schema = None
    _enum = False
    _format_as = "BooleanField"


# schema.org version 2.0
