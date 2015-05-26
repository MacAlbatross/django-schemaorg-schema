# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EnumerationSchema(SchemaObject):

    """Schema Mixin for Enumeration
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Lists or enumerationsfor example, a list of cuisines or music genres, etc.
    """

    def __init__(self):
        self.schema = 'Enumeration'


class supersededByProp(SchemaProperty):

    """
    SchemaField for supersededBy
    Usage: Include in SchemaObject SchemaFields as your_django_field = supersededByProp()  
    schema.org description:Relates a term (i.e. a property, class or enumeration) to one that supersedes it.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Enumeration"""

    _prop_schema = 'supersededBy'
    _expected_schema = 'Enumeration'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
