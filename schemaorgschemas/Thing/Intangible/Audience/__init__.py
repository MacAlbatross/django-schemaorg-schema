# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AudienceSchema(SchemaObject):

    """Schema Mixin for Audience
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Intended audience for an item, i.e. the group for whom the item was created.
    """

    def __init__(self):
        self.schema = 'Audience'


class geographicAreaProp(SchemaProperty):

    """
    SchemaField for geographicArea
    Usage: Include in SchemaObject SchemaFields as your_django_field = geographicAreaProp()
    schema.org description:The geographic area associated with the audience.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AdministrativeArea"""

    _prop_schema = 'geographicArea'
    _expected_schema = 'AdministrativeArea'
    _enum = False
    _format_as = "ForeignKey"


class audienceTypeProp(SchemaProperty):

    """
    SchemaField for audienceType
    Usage: Include in SchemaObject SchemaFields as your_django_field = audienceTypeProp()
    schema.org description:The target group associated with a given audience (e.g. veterans, car owners, musicians, etc.) domain: Audience Range: Text

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'audienceType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
