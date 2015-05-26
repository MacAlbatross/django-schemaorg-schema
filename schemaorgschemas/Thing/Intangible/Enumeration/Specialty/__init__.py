# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SpecialtySchema(SchemaObject):

    """Schema Mixin for Specialty
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any branch of a field in which people typically develop specific expertise, usually after significant study, time, and effort.
    """

    def __init__(self):
        self.schema = 'Specialty'


# schema.org version 2.0
