# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Intangible.Reservation import reservationForProp, totalPriceProp, modifiedTimeProp, priceCurrencyProp, reservationStatusProp, brokerProp, programMembershipUsedProp, reservationIdProp, reservedTicketProp, providerProp, bookingTimeProp, underNameProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TrainReservationSchema(SchemaObject):

    """Schema Mixin for TrainReservation
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A reservation for train travel.
    """

    def __init__(self):
        self.schema = 'TrainReservation'


# schema.org version 2.0
