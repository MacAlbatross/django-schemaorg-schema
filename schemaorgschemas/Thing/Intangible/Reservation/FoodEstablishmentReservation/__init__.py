# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Intangible.Reservation import reservationForProp, totalPriceProp, modifiedTimeProp, priceCurrencyProp, reservationStatusProp, brokerProp, reservedTicketProp, programMembershipUsedProp, reservationIdProp, underNameProp, providerProp, bookingTimeProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FoodEstablishmentReservationSchema(SchemaObject):

    """Schema Mixin for FoodEstablishmentReservation
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A reservation to dine at a food-related business.
    """

    def __init__(self):
        self.schema = 'FoodEstablishmentReservation'


class endTimeProp(SchemaProperty):

    """
    SchemaField for endTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = endTimeProp()  
    schema.org description:The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to *December*. Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'endTime'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class startTimeProp(SchemaProperty):

    """
    SchemaField for startTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = startTimeProp()  
    schema.org description:The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from *January* to December. Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'startTime'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class partySizeProp(SchemaProperty):

    """
    SchemaField for partySize
    Usage: Include in SchemaObject SchemaFields as your_django_field = partySizeProp()  
    schema.org description:Number of people the reservation should accommodate.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'partySize'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


# schema.org version 2.0
