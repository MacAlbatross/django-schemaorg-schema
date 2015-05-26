# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PathologySchema(SchemaObject):

    """Schema Mixin for Pathology
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that is concerned with the study of the cause, origin and nature of a disease state, including its consequences as a result of manifestation of the disease. In clinical care, the term is used to designate a branch of medicine using laboratory tests to diagnose and determine the prognostic significance of illness.
    """

    def __init__(self):
        self.schema = 'Pathology'


# schema.org version 2.0
