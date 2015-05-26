# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EBookSchema(SchemaObject):

    """Schema Mixin for EBook
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Book format: Ebook.
    """

    def __init__(self):
        self.schema = 'EBook'


# schema.org version 2.0
