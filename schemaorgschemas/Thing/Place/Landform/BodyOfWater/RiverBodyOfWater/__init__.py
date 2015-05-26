# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, nameProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, descriptionProp
from schemaorgschemas.Thing.Place import isicV4Prop, openingHoursSpecificationProp, photoProp, hasMapProp, reviewProp, containedInProp, faxNumberProp, aggregateRatingProp, additionalPropertyProp, addressProp, telephoneProp, logoProp, geoProp, eventProp, globalLocationNumberProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RiverBodyOfWaterSchema(SchemaObject):

    """Schema Mixin for RiverBodyOfWater
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A river (for example, the broad majestic Shannon).
    """

    def __init__(self):
        self.schema = 'RiverBodyOfWater'


# schema.org version 2.0
