# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Intangible.Reservation import reservationForProp, reservedTicketProp, totalPriceProp, modifiedTimeProp, priceCurrencyProp, reservationStatusProp, brokerProp, underNameProp, reservationIdProp, programMembershipUsedProp, providerProp, bookingTimeProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FlightReservationSchema(SchemaObject):

    """Schema Mixin for FlightReservation
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A reservation for air travel.
    """

    def __init__(self):
        self.schema = 'FlightReservation'


class passengerPriorityStatusProp(SchemaProperty):

    """
    SchemaField for passengerPriorityStatus
    Usage: Include in SchemaObject SchemaFields as your_django_field = passengerPriorityStatusProp()  
    schema.org description:The priority status assigned to a passenger for security or boarding (e.g. FastTrack or Priority).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'passengerPriorityStatus'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class securityScreeningProp(SchemaProperty):

    """
    SchemaField for securityScreening
    Usage: Include in SchemaObject SchemaFields as your_django_field = securityScreeningProp()  
    schema.org description:The type of security screening the passenger is subject to.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'securityScreening'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class boardingGroupProp(SchemaProperty):

    """
    SchemaField for boardingGroup
    Usage: Include in SchemaObject SchemaFields as your_django_field = boardingGroupProp()  
    schema.org description:The airline-specific indicator of boarding order / preference.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'boardingGroup'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class passengerSequenceNumberProp(SchemaProperty):

    """
    SchemaField for passengerSequenceNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = passengerSequenceNumberProp()  
    schema.org description:The passenger&#39;s sequence number as assigned by the airline.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'passengerSequenceNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
