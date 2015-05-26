# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class GynecologicSchema(SchemaObject):

    """Schema Mixin for Gynecologic
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that pertains to the health care of women, particularly in the diagnosis and treatment of disorders affecting the female reproductive system.
    """

    def __init__(self):
        self.schema = 'Gynecologic'


# schema.org version 2.0
