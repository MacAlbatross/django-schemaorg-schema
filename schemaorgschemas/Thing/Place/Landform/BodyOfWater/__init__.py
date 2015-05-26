# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Place import isicV4Prop, openingHoursSpecificationProp, photoProp, hasMapProp, reviewProp, containedInProp, faxNumberProp, aggregateRatingProp, additionalPropertyProp, addressProp, telephoneProp, logoProp, geoProp, eventProp, globalLocationNumberProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BodyOfWaterSchema(SchemaObject):

    """Schema Mixin for BodyOfWater
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A body of water, such as a sea, ocean, or lake.
    """

    def __init__(self):
        self.schema = 'BodyOfWater'


# schema.org version 2.0
