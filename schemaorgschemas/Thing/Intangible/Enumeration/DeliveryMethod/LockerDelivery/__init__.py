# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class LockerDeliverySchema(SchemaObject):

    """Schema Mixin for LockerDelivery
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A DeliveryMethod in which an item is made available via locker.
    """

    def __init__(self):
        self.schema = 'LockerDelivery'
