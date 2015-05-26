# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, urlProp, imageProp, sameAsProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Place.CivicStructure import openingHoursProp
from schemaorgschemas.Thing.Place import isicV4Prop, openingHoursSpecificationProp, photoProp, hasMapProp, reviewProp, containedInProp, faxNumberProp, aggregateRatingProp, additionalPropertyProp, addressProp, telephoneProp, logoProp, geoProp, eventProp, globalLocationNumberProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BusStopSchema(SchemaObject):

    """Schema Mixin for BusStop
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A bus stop.
    """

    def __init__(self):
        self.schema = 'BusStop'


# schema.org version 2.0
