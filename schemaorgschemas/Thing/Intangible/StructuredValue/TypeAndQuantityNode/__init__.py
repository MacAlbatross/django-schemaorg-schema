# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TypeAndQuantityNodeSchema(SchemaObject):

    """Schema Mixin for TypeAndQuantityNode
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A structured value indicating the quantity, unit of measurement, and business function of goods included in a bundle offer.
    """

    def __init__(self):
        self.schema = 'TypeAndQuantityNode'


class unitCodeProp(SchemaProperty):

    """
    SchemaField for unitCode
    Usage: Include in SchemaObject SchemaFields as your_django_field = unitCodeProp()
    schema.org description:The unit of measurement given using the UN/CEFACT Common Code (3 characters).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'unitCode'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class businessFunctionProp(SchemaProperty):

    """
    SchemaField for businessFunction
    Usage: Include in SchemaObject SchemaFields as your_django_field = businessFunctionProp()
    schema.org description:The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference BusinessFunction"""

    _prop_schema = 'businessFunction'
    _expected_schema = 'BusinessFunction'
    _enum = False
    _format_as = "ForeignKey"


class amountOfThisGoodProp(SchemaProperty):

    """
    SchemaField for amountOfThisGood
    Usage: Include in SchemaObject SchemaFields as your_django_field = amountOfThisGoodProp()
    schema.org description:The quantity of the goods included in the offer.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'amountOfThisGood'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


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
