# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DurationSchema(SchemaObject):

    """Schema Mixin for Duration
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Quantity: Duration (use  ISO 8601 duration format).
    """

    def __init__(self):
        self.schema = 'Duration'


# schema.org version 2.0
