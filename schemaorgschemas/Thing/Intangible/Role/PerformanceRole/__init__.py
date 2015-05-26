# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Role import roleNameProp, endDateProp, startDateProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PerformanceRoleSchema(SchemaObject):

    """Schema Mixin for PerformanceRole
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A PerformanceRole is a Role that some entity places with regard to a theatrical performance, e.g. in a Movie, TVSeries etc.
    """

    def __init__(self):
        self.schema = 'PerformanceRole'


class characterNameProp(SchemaProperty):

    """
    SchemaField for characterName
    Usage: Include in SchemaObject SchemaFields as your_django_field = characterNameProp()  
    schema.org description:The name of a character played in some acting or performing role, i.e. in a PerformanceRole.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'characterName'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
