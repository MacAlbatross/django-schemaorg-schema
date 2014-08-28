# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SeatSchema(SchemaObject):

    """Schema Mixin for Seat
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Used to describe a seat, such as a reserved seat in an event reservation.
    """

    def __init__(self):
        self.schema = 'Seat'


class seatRowProp(SchemaProperty):

    """
    SchemaField for seatRow
    Usage: Include in SchemaObject SchemaFields as your_django_field = seatRowProp()
    schema.org description:The row location of the reserved seat (e.g., B).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'seatRow'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class seatSectionProp(SchemaProperty):

    """
    SchemaField for seatSection
    Usage: Include in SchemaObject SchemaFields as your_django_field = seatSectionProp()
    schema.org description:The section location of the reserved seat (e.g. Orchestra).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'seatSection'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class seatingTypeProp(SchemaProperty):

    """
    SchemaField for seatingType
    Usage: Include in SchemaObject SchemaFields as your_django_field = seatingTypeProp()
    schema.org description:The type/class of the seat.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'seatingType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class seatNumberProp(SchemaProperty):

    """
    SchemaField for seatNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = seatNumberProp()
    schema.org description:The location of the reserved seat (e.g., 27).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'seatNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
