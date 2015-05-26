# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, urlProp, imageProp, sameAsProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class StructuredValueSchema(SchemaObject):

    """Schema Mixin for StructuredValue
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.
    """

    def __init__(self):
        self.schema = 'StructuredValue'


# schema.org version 2.0
