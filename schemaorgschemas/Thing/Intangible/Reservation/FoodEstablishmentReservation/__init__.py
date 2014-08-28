# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Intangible.Reservation import reservationForProp, totalPriceProp, modifiedTimeProp, priceCurrencyProp, reservationStatusProp, programMembershipUsedProp, bookingAgentProp, reservedTicketProp, providerProp, reservationIdProp, bookingTimeProp, underNameProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FoodEstablishmentReservationSchema(SchemaObject):

    """Schema Mixin for FoodEstablishmentReservation
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A reservation to dine at a food-related business.
    """

    def __init__(self):
        self.schema = 'FoodEstablishmentReservation'


class startTimeProp(SchemaProperty):

    """
    SchemaField for startTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = startTimeProp()  
    schema.org description:When the Action was performed: start time. This is for actions that span a period of time. e.g. John wrote a book from *January* to December.

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
    """

    _prop_schema = 'partySize'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"
