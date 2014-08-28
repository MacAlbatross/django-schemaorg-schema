# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OwnershipInfoSchema(SchemaObject):

    """Schema Mixin for OwnershipInfo
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A structured value providing information about when a certain organization or person owned a certain product.
    """

    def __init__(self):
        self.schema = 'OwnershipInfo'


class ownedFromProp(SchemaProperty):

    """
    SchemaField for ownedFrom
    Usage: Include in SchemaObject SchemaFields as your_django_field = ownedFromProp()
    schema.org description:The date and time of obtaining the product.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'ownedFrom'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class acquiredFromProp(SchemaProperty):

    """
    SchemaField for acquiredFrom
    Usage: Include in SchemaObject SchemaFields as your_django_field = acquiredFromProp()
    schema.org description:The organization or person from which the product was acquired.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'acquiredFrom'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class typeOfGoodProp(SchemaProperty):

    """
    SchemaField for typeOfGood
    Usage: Include in SchemaObject SchemaFields as your_django_field = typeOfGoodProp()
    schema.org description:The product that this structured value is referring to.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Product"""

    _prop_schema = 'typeOfGood'
    _expected_schema = 'Product'
    _enum = False
    _format_as = "TextField"


class ownedThroughProp(SchemaProperty):

    """
    SchemaField for ownedThrough
    Usage: Include in SchemaObject SchemaFields as your_django_field = ownedThroughProp()
    schema.org description:The date and time of giving up ownership on the product.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'ownedThrough'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"
