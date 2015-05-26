# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Intangible.Enumeration.QualitativeValue import valueReferenceProp, greaterProp, lesserOrEqualProp, equalProp, lesserProp, additionalPropertyProp, greaterOrEqualProp, nonEqualProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CarUsageTypeSchema(SchemaObject):

    """Schema Mixin for CarUsageType
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A value indicating a special usage of a car, e.g. commercial rental, driving school, or as a taxi.
    """

    def __init__(self):
        self.schema = 'CarUsageType'


# schema.org version 2.0
