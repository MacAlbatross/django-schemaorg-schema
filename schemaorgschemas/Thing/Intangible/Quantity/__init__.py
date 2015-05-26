# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class QuantitySchema(SchemaObject):

    """Schema Mixin for Quantity
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like &#39;3 Kg&#39; or &#39;4 milligrams&#39;.
    """

    def __init__(self):
        self.schema = 'Quantity'


# schema.org version 2.0
