# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Place import isicV4Prop, mapProp, openingHoursSpecificationProp, photoProp, reviewProp, containedInProp, faxNumberProp, aggregateRatingProp, telephoneProp, addressProp, interactionCountProp, logoProp, geoProp, eventProp, globalLocationNumberProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AdministrativeAreaSchema(SchemaObject):

    """Schema Mixin for AdministrativeArea
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A geographical region under the jurisdiction of a particular government.
    """

    def __init__(self):
        self.schema = 'AdministrativeArea'
