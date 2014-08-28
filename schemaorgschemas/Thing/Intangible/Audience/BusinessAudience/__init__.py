# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Audience import geographicAreaProp, audienceTypeProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BusinessAudienceSchema(SchemaObject):

    """Schema Mixin for BusinessAudience
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A set of characteristics belonging to businesses, e.g. who compose an item&#39;s target audience.
    """

    def __init__(self):
        self.schema = 'BusinessAudience'


class yearlyRevenueProp(SchemaProperty):

    """
    SchemaField for yearlyRevenue
    Usage: Include in SchemaObject SchemaFields as your_django_field = yearlyRevenueProp()
    schema.org description:The size of the business in annual revenue.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'yearlyRevenue'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class yearsInOperationProp(SchemaProperty):

    """
    SchemaField for yearsInOperation
    Usage: Include in SchemaObject SchemaFields as your_django_field = yearsInOperationProp()
    schema.org description:The age of the business.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'yearsInOperation'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class numberofEmployeesProp(SchemaProperty):

    """
    SchemaField for numberofEmployees
    Usage: Include in SchemaObject SchemaFields as your_django_field = numberofEmployeesProp()
    schema.org description:The size of business by number of employees.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'numberofEmployees'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"
