# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OnSitePickupSchema(SchemaObject):

    """Schema Mixin for OnSitePickup
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A DeliveryMethod in which an item is collected on site, e.g. in a store or at a box office.
    """

    def __init__(self):
        self.schema = 'OnSitePickup'


# schema.org version 2.0
