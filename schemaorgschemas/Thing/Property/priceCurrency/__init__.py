# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class priceCurrencySchema(SchemaObject):

    """Schema Mixin for priceCurrency
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The currency (in 3-letter ISO 4217 format) of the price or a price component, when attached to PriceSpecification and its subtypes.
    """

    def __init__(self):
        self.schema = 'priceCurrency'


# schema.org version 2.0
