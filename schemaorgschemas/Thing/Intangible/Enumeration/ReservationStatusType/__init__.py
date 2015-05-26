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


/RESERVATIONSTATUS_CHOICES = (
    ('/RESERVATIONCONFIRMED', '/ReservationConfirmed'),
    ('/RESERVATIONHOLD', '/ReservationHold'),
    ('/RESERVATIONPENDING', '/ReservationPending'),
    ('/RESERVATIONCANCELLED', '/ReservationCancelled'),
)


class / reservationStatusProp(SchemaEnumProperty):

    """
    Enumeration for /reservationStatus
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/reservationStatus'
    choices = /RESERVATIONSTATUS_CHOICES
    _format_as = "enum"
    adapter = {
        '/RESERVATIONCONFIRMED': '/ReservationConfirmed',
        '/RESERVATIONHOLD': '/ReservationHold',
        '/RESERVATIONPENDING': '/ReservationPending',
        '/RESERVATIONCANCELLED': '/ReservationCancelled',
    }


# schema.org version 2.0
