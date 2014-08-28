# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Intangible.Reservation import reservationForProp, totalPriceProp, modifiedTimeProp, priceCurrencyProp, reservationStatusProp, programMembershipUsedProp, bookingAgentProp, reservedTicketProp, providerProp, reservationIdProp, bookingTimeProp, underNameProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TaxiReservationSchema(SchemaObject):

    """Schema Mixin for TaxiReservation
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A reservation for a taxi.
    """

    def __init__(self):
        self.schema = 'TaxiReservation'


class pickupTimeProp(SchemaProperty):

    """
    SchemaField for pickupTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = pickupTimeProp()
    schema.org description:When a taxi will pickup a passenger or a rental car can be picked up.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'pickupTime'
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
    """

    _prop_schema = 'partySize'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class pickupLocationProp(SchemaProperty):

    """
    SchemaField for pickupLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = pickupLocationProp()
    schema.org description:Where a taxi will pick up a passenger or a rental car can be picked up.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'pickupLocation'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"
