# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Event import inLanguageProp, attendeeProp, performerProp, endDateProp, startDateProp, previousStartDateProp, superEventProp, reviewProp, recordedInProp, aggregateRatingProp, subEventProp, offersProp, eventStatusProp, typicalAgeRangeProp, durationProp, workPerformedProp, organizerProp, doorTimeProp, locationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ScreeningEventSchema(SchemaObject):

    """Schema Mixin for ScreeningEvent
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A screening of a movie or other video.
    """

    def __init__(self):
        self.schema = 'ScreeningEvent'


class subtitleLanguageProp(SchemaProperty):

    """
    SchemaField for subtitleLanguage
    Usage: Include in SchemaObject SchemaFields as your_django_field = subtitleLanguageProp()  
    schema.org description:Languages in which subtitles/captions are available, in IETF BCP 47 standard format.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'subtitleLanguage'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class workPresentedProp(SchemaProperty):

    """
    SchemaField for workPresented
    Usage: Include in SchemaObject SchemaFields as your_django_field = workPresentedProp()  
    schema.org description:The movie presented during this event.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Movie"""

    _prop_schema = 'workPresented'
    _expected_schema = 'Movie'
    _enum = False
    _format_as = "ForeignKey"


class videoFormatProp(SchemaProperty):

    """
    SchemaField for videoFormat
    Usage: Include in SchemaObject SchemaFields as your_django_field = videoFormatProp()  
    schema.org description:The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'videoFormat'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
