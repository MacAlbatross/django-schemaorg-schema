# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DistanceSchema(SchemaObject):

    """Schema Mixin for Distance
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Properties that take Distances as values are of the form &#39;&lt;Number&gt; &lt;Length unit of measure&gt;&#39;. E.g., &#39;7 ft&#39;.
    """

    def __init__(self):
        self.schema = 'Distance'


# schema.org version 2.0
