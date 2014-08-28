# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BrandSchema(SchemaObject):

    """Schema Mixin for Brand
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A brand is a name used by an organization or business person for labeling a product, product group, or similar.
    """

    def __init__(self):
        self.schema = 'Brand'


class logoProp(SchemaProperty):

    """
    SchemaField for logo
    Usage: Include in SchemaObject SchemaFields as your_django_field = logoProp()  
    schema.org description:A logo associated with an organization.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'logo'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"
