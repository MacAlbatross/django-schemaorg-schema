# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Intangible.Reservation import reservationForProp, totalPriceProp, modifiedTimeProp, priceCurrencyProp, reservationStatusProp, programMembershipUsedProp, bookingAgentProp, reservedTicketProp, providerProp, reservationIdProp, bookingTimeProp, underNameProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FlightReservationSchema(SchemaObject):

    """Schema Mixin for FlightReservation
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A reservation for air travel.
    """

    def __init__(self):
        self.schema = 'FlightReservation'


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
