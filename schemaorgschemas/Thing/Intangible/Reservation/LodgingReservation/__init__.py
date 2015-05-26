# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Intangible.Reservation import reservationForProp, totalPriceProp, modifiedTimeProp, priceCurrencyProp, reservationStatusProp, brokerProp, reservedTicketProp, programMembershipUsedProp, reservationIdProp, underNameProp, providerProp, bookingTimeProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class LodgingReservationSchema(SchemaObject):

    """Schema Mixin for LodgingReservation
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A reservation for lodging at a hotel, motel, inn, etc.
    """

    def __init__(self):
        self.schema = 'LodgingReservation'


class checkoutTimeProp(SchemaProperty):

    """
    SchemaField for checkoutTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = checkoutTimeProp()  
    schema.org description:The latest someone may check out of a lodging establishment.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'checkoutTime'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class lodgingUnitTypeProp(SchemaProperty):

    """
    SchemaField for lodgingUnitType
    Usage: Include in SchemaObject SchemaFields as your_django_field = lodgingUnitTypeProp()  
    schema.org description:Textual description of the unit type (including suite vs. room, size of bed, etc.).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'lodgingUnitType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class lodgingUnitDescriptionProp(SchemaProperty):

    """
    SchemaField for lodgingUnitDescription
    Usage: Include in SchemaObject SchemaFields as your_django_field = lodgingUnitDescriptionProp()  
    schema.org description:A full description of the lodging unit.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'lodgingUnitDescription'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class checkinTimeProp(SchemaProperty):

    """
    SchemaField for checkinTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = checkinTimeProp()  
    schema.org description:The earliest someone may check into a lodging establishment.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'checkinTime'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class numAdultsProp(SchemaProperty):

    """
    SchemaField for numAdults
    Usage: Include in SchemaObject SchemaFields as your_django_field = numAdultsProp()  
    schema.org description:The number of adults staying in the unit.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'numAdults'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class numChildrenProp(SchemaProperty):

    """
    SchemaField for numChildren
    Usage: Include in SchemaObject SchemaFields as your_django_field = numChildrenProp()  
    schema.org description:The number of children staying in the unit.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'numChildren'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


# schema.org version 2.0
