# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Event import inLanguageProp, attendeeProp, performerProp, endDateProp, startDateProp, previousStartDateProp, superEventProp, reviewProp, recordedInProp, aggregateRatingProp, subEventProp, offersProp, eventStatusProp, typicalAgeRangeProp, durationProp, workPerformedProp, organizerProp, doorTimeProp, locationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PublicationEventSchema(SchemaObject):

    """Schema Mixin for PublicationEvent
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A PublicationEvent corresponds indifferently to the event of publication for a CreativeWork of any type e.g. a broadcast event, an on-demand event, a book/journal publication via a variety of delivery media.
    """

    def __init__(self):
        self.schema = 'PublicationEvent'


class isAccessibleForFreeProp(SchemaProperty):

    """
    SchemaField for isAccessibleForFree
    Usage: Include in SchemaObject SchemaFields as your_django_field = isAccessibleForFreeProp()  
    schema.org description:A flag to signal that the publication is accessible for free. Supersedes free.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'isAccessibleForFree'
    _expected_schema = None
    _enum = False
    _format_as = "BooleanField"


class publishedOnProp(SchemaProperty):

    """
    SchemaField for publishedOn
    Usage: Include in SchemaObject SchemaFields as your_django_field = publishedOnProp()  
    schema.org description:A broadcast service associated with the publication event.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference BroadcastService"""

    _prop_schema = 'publishedOn'
    _expected_schema = 'BroadcastService'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
