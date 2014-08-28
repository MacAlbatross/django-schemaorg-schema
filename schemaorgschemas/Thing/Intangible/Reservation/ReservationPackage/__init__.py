# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Intangible.Reservation import reservationForProp, totalPriceProp, modifiedTimeProp, priceCurrencyProp, reservationStatusProp, programMembershipUsedProp, bookingAgentProp, reservedTicketProp, providerProp, reservationIdProp, bookingTimeProp, underNameProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ReservationPackageSchema(SchemaObject):

    """Schema Mixin for ReservationPackage
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A group of multiple reservations with common values for all sub-reservations.
    """

    def __init__(self):
        self.schema = 'ReservationPackage'


class subReservationProp(SchemaProperty):

    """
    SchemaField for subReservation
    Usage: Include in SchemaObject SchemaFields as your_django_field = subReservationProp()  
    schema.org description:The individual reservations included in the package. Typically a repeated property.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Reservation"""

    _prop_schema = 'subReservation'
    _expected_schema = 'Reservation'
    _enum = False
    _format_as = "ForeignKey"
