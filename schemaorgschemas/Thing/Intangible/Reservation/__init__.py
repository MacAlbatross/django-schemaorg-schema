# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ReservationSchema(SchemaObject):

    """Schema Mixin for Reservation
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Describes a reservation for travel, dining or an event. Some reservations require tickets.
    """

    def __init__(self):
        self.schema = 'Reservation'


class reservationForProp(SchemaProperty):

    """
    SchemaField for reservationFor
    Usage: Include in SchemaObject SchemaFields as your_django_field = reservationForProp()
    schema.org description:The thing -- flight, event, restaurant,etc. being reserved.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'reservationFor'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


class totalPriceProp(SchemaProperty):

    """
    SchemaField for totalPrice
    Usage: Include in SchemaObject SchemaFields as your_django_field = totalPriceProp()
    schema.org description:The total price for the reservation or ticket, including applicable taxes, shipping, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'totalPrice'
    _expected_schema = None
    _enum = False
    _format_as = "DecimalField"


class modifiedTimeProp(SchemaProperty):

    """
    SchemaField for modifiedTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = modifiedTimeProp()
    schema.org description:The date and time the reservation was modified.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'modifiedTime'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class priceCurrencyProp(SchemaProperty):

    """
    SchemaField for priceCurrency
    Usage: Include in SchemaObject SchemaFields as your_django_field = priceCurrencyProp()
    schema.org description:The currency (in 3-letter ISO 4217 format) of the offer price or a price component, when attached to PriceSpecification and its subtypes.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'priceCurrency'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class reservationStatusProp(SchemaProperty):

    """
    SchemaField for reservationStatus
    Usage: Include in SchemaObject SchemaFields as your_django_field = reservationStatusProp()
    schema.org description:The current status of the reservation.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ReservationStatusType"""

    _prop_schema = 'reservationStatus'
    _expected_schema = 'ReservationStatusType'
    _enum = False
    _format_as = "ForeignKey"


class reservedTicketProp(SchemaProperty):

    """
    SchemaField for reservedTicket
    Usage: Include in SchemaObject SchemaFields as your_django_field = reservedTicketProp()
    schema.org description:A ticket associated with the reservation.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Ticket"""

    _prop_schema = 'reservedTicket'
    _expected_schema = 'Ticket'
    _enum = False
    _format_as = "ForeignKey"


class bookingAgentProp(SchemaProperty):

    """
    SchemaField for bookingAgent
    Usage: Include in SchemaObject SchemaFields as your_django_field = bookingAgentProp()
    schema.org description:If the reservation was not booked directly through the provider, the third-party booking agent can be recorded through this property.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'bookingAgent'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class programMembershipUsedProp(SchemaProperty):

    """
    SchemaField for programMembershipUsed
    Usage: Include in SchemaObject SchemaFields as your_django_field = programMembershipUsedProp()
    schema.org description:Any membership in a frequent flyer, hotel loyalty program, etc. being applied to the reservation.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ProgramMembership"""

    _prop_schema = 'programMembershipUsed'
    _expected_schema = 'ProgramMembership'
    _enum = False
    _format_as = "ForeignKey"


class providerProp(SchemaProperty):

    """
    SchemaField for provider
    Usage: Include in SchemaObject SchemaFields as your_django_field = providerProp()
    schema.org description:The organization or agency that is providing the service.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'provider'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class reservationIdProp(SchemaProperty):

    """
    SchemaField for reservationId
    Usage: Include in SchemaObject SchemaFields as your_django_field = reservationIdProp()
    schema.org description:A unique identifier for the reservation.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'reservationId'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class bookingTimeProp(SchemaProperty):

    """
    SchemaField for bookingTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = bookingTimeProp()
    schema.org description:The date and time the reservation was booked.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'bookingTime'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class underNameProp(SchemaProperty):

    """
    SchemaField for underName
    Usage: Include in SchemaObject SchemaFields as your_django_field = underNameProp()
    schema.org description:The person or organization the reservation or ticket is for.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'underName'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"
