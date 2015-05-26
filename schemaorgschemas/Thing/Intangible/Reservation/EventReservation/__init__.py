# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Reservation import reservationForProp, totalPriceProp, modifiedTimeProp, priceCurrencyProp, reservationStatusProp, brokerProp, programMembershipUsedProp, reservationIdProp, reservedTicketProp, providerProp, bookingTimeProp, underNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EventReservationSchema(SchemaObject):

    """Schema Mixin for EventReservation
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A reservation for an event like a concert, sporting event, or lecture.
    """

    def __init__(self):
        self.schema = 'EventReservation'


# schema.org version 2.0
