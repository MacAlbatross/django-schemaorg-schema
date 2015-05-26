# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MassSchema(SchemaObject):

    """Schema Mixin for Mass
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Properties that take Mass as values are of the form &#39;&lt;Number&gt; &lt;Mass unit of measure&gt;&#39;. E.g., &#39;7 kg&#39;.
    """

    def __init__(self):
        self.schema = 'Mass'


# schema.org version 2.0
