# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class VenueMapSchema(SchemaObject):

    """Schema Mixin for VenueMap
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A venue map (e.g. for malls, auditoriums, museums, etc.).
    """

    def __init__(self):
        self.schema = 'VenueMap'


# schema.org version 2.0
