# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Reservation import reservationForProp, totalPriceProp, modifiedTimeProp, priceCurrencyProp, reservationStatusProp, brokerProp, programMembershipUsedProp, reservationIdProp, reservedTicketProp, providerProp, bookingTimeProp, underNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BusReservationSchema(SchemaObject):

    """Schema Mixin for BusReservation
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A reservation for bus travel.
    """

    def __init__(self):
        self.schema = 'BusReservation'


# schema.org version 2.0
