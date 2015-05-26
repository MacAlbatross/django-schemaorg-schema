# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DatedMoneySpecificationSchema(SchemaObject):

    """Schema Mixin for DatedMoneySpecification
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A DatedMoneySpecification represents monetary values with optional start and end dates. For example, this could represent an employee&#39;s salary over a specific period of time.
    """

    def __init__(self):
        self.schema = 'DatedMoneySpecification'


class currencyProp(SchemaProperty):

    """
    SchemaField for currency
    Usage: Include in SchemaObject SchemaFields as your_django_field = currencyProp()  
    schema.org description:The currency in which the monetary amount is expressed (in 3-letter ISO 4217 format).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'currency'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class amountProp(SchemaProperty):

    """
    SchemaField for amount
    Usage: Include in SchemaObject SchemaFields as your_django_field = amountProp()  
    schema.org description:The amount of money.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'amount'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


class endDateProp(SchemaProperty):

    """
    SchemaField for endDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = endDateProp()  
    schema.org description:The end date and time of the item (in ISO 8601 date format).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'endDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class startDateProp(SchemaProperty):

    """
    SchemaField for startDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = startDateProp()  
    schema.org description:The start date and time of the item (in ISO 8601 date format).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'startDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


# schema.org version 2.0
