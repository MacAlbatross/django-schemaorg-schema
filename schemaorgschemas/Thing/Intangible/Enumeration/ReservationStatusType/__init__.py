# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ReservationStatusTypeSchema(SchemaObject):

    """Schema Mixin for ReservationStatusType
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Enumerated status values for Reservation.
    """

    def __init__(self):
        self.schema = 'ReservationStatusType'


RESERVATIONSTATUS_CHOICES = (
    ('RESERVATIONCONFIRMED',
     'ReservationConfirmed: The status of a confirmed reservation.'),
    ('RESERVATIONHOLD',
     'ReservationHold: The status of a reservation on hold pending an update like credit card number or flight changes.'),
    ('RESERVATIONPENDING',
     'ReservationPending: The status of a reservation when a request has been sent, but not confirmed.'),
    ('RESERVATIONCANCELLED',
     'ReservationCancelled: The status for a previously confirmed reservation that is now cancelled.'),
)


class reservationStatusProp(SchemaEnumProperty):

    """
    Enumeration for reservationStatus
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'reservationStatus'
    choices = RESERVATIONSTATUS_CHOICES
    _format_as = "enum"
    adapter = {
        'RESERVATIONCONFIRMED': 'ReservationConfirmed',
        'RESERVATIONHOLD': 'ReservationHold',
        'RESERVATIONPENDING': 'ReservationPending',
        'RESERVATIONCANCELLED': 'ReservationCancelled',
    }


# schema.org version 2.0
