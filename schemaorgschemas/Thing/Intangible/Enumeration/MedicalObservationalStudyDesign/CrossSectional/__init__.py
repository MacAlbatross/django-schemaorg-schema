# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CrossSectionalSchema(SchemaObject):

    """Schema Mixin for CrossSectional
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Studies carried out on pre-existing data (usually from &#39;snapshot&#39; surveys), such as that collected by the Census Bureau. Sometimes called Prevalence Studies.
    """

    def __init__(self):
        self.schema = 'CrossSectional'


# schema.org version 2.0
