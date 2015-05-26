# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EnergySchema(SchemaObject):

    """Schema Mixin for Energy
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Properties that take Energy as values are of the form &#39;&lt;Number&gt; &lt;Energy unit of measure&gt;&#39;.
    """

    def __init__(self):
        self.schema = 'Energy'


# schema.org version 2.0
