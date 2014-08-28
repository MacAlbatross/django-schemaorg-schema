# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Intangible.Reservation import reservationForProp, totalPriceProp, modifiedTimeProp, priceCurrencyProp, reservationStatusProp, programMembershipUsedProp, bookingAgentProp, reservedTicketProp, providerProp, reservationIdProp, bookingTimeProp, underNameProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RentalCarReservationSchema(SchemaObject):

    """Schema Mixin for RentalCarReservation
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A reservation for a rental car.
    """

    def __init__(self):
        self.schema = 'RentalCarReservation'


class dropoffTimeProp(SchemaProperty):

    """
    SchemaField for dropoffTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = dropoffTimeProp()  
    schema.org description:When a rental car can be dropped off.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'dropoffTime'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class dropoffLocationProp(SchemaProperty):

    """
    SchemaField for dropoffLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = dropoffLocationProp()  
    schema.org description:Where a rental car can be dropped off.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'dropoffLocation'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"


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
