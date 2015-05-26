# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Event import inLanguageProp, attendeeProp, performerProp, endDateProp, startDateProp, previousStartDateProp, superEventProp, reviewProp, recordedInProp, aggregateRatingProp, subEventProp, offersProp, eventStatusProp, typicalAgeRangeProp, durationProp, workPerformedProp, organizerProp, doorTimeProp, locationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SportsEventSchema(SchemaObject):

    """Schema Mixin for SportsEvent
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Event type: Sports event.
    """

    def __init__(self):
        self.schema = 'SportsEvent'


class awayTeamProp(SchemaProperty):

    """
    SchemaField for awayTeam
    Usage: Include in SchemaObject SchemaFields as your_django_field = awayTeamProp()  
    schema.org description:The away team in a sports event.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference SportsTeam"""

    _prop_schema = 'awayTeam'
    _expected_schema = 'SportsTeam'
    _enum = False
    _format_as = "ForeignKey"


class homeTeamProp(SchemaProperty):

    """
    SchemaField for homeTeam
    Usage: Include in SchemaObject SchemaFields as your_django_field = homeTeamProp()  
    schema.org description:The home team in a sports event.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference SportsTeam"""

    _prop_schema = 'homeTeam'
    _expected_schema = 'SportsTeam'
    _enum = False
    _format_as = "ForeignKey"


class competitorProp(SchemaProperty):

    """
    SchemaField for competitor
    Usage: Include in SchemaObject SchemaFields as your_django_field = competitorProp()  
    schema.org description:A competitor in a sports event.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference SportsTeam"""

    _prop_schema = 'competitor'
    _expected_schema = 'SportsTeam'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
