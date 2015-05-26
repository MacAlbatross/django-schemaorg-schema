# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Place.CivicStructure import openingHoursProp
from schemaorgschemas.Thing.Place import isicV4Prop, openingHoursSpecificationProp, photoProp, reviewProp, telephoneProp, containedInProp, hasMapProp, aggregateRatingProp, additionalPropertyProp, addressProp, logoProp, faxNumberProp, geoProp, eventProp, globalLocationNumberProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PerformingArtsTheaterSchema(SchemaObject):

    """Schema Mixin for PerformingArtsTheater
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A theater or other performing art center.
    """

    def __init__(self):
        self.schema = 'PerformingArtsTheater'


# schema.org version 2.0
