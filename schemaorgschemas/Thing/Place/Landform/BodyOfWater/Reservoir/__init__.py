# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Place import isicV4Prop, openingHoursSpecificationProp, photoProp, hasMapProp, reviewProp, containedInProp, faxNumberProp, aggregateRatingProp, additionalPropertyProp, addressProp, telephoneProp, logoProp, geoProp, eventProp, globalLocationNumberProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ReservoirSchema(SchemaObject):

    """Schema Mixin for Reservoir
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir.
    """

    def __init__(self):
        self.schema = 'Reservoir'


# schema.org version 2.0
