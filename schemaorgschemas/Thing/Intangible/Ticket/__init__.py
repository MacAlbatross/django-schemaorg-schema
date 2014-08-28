# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TicketSchema(SchemaObject):

    """Schema Mixin for Ticket
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Used to describe a ticket to an event, a flight, a bus ride, etc.
    """

    def __init__(self):
        self.schema = 'Ticket'


class ticketTokenProp(SchemaProperty):

    """
    SchemaField for ticketToken
    Usage: Include in SchemaObject SchemaFields as your_django_field = ticketTokenProp()  
    schema.org description:Reference to an asset (e.g., Barcode, QR code image or PDF) usable for entrance.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'ticketToken'
    _expected_schema = None
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


class ticketedSeatProp(SchemaProperty):

    """
    SchemaField for ticketedSeat
    Usage: Include in SchemaObject SchemaFields as your_django_field = ticketedSeatProp()  
    schema.org description:The seat associated with the ticket.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Seat"""

    _prop_schema = 'ticketedSeat'
    _expected_schema = 'Seat'
    _enum = False
    _format_as = "ForeignKey"


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


class dateIssuedProp(SchemaProperty):

    """
    SchemaField for dateIssued
    Usage: Include in SchemaObject SchemaFields as your_django_field = dateIssuedProp()  
    schema.org description:The date the ticket was issued.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'dateIssued'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class ticketNumberProp(SchemaProperty):

    """
    SchemaField for ticketNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = ticketNumberProp()  
    schema.org description:The unique identifier for the ticket.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'ticketNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class issuedByProp(SchemaProperty):

    """
    SchemaField for issuedBy
    Usage: Include in SchemaObject SchemaFields as your_django_field = issuedByProp()  
    schema.org description:The organization issuing the permit.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'issuedBy'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


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
