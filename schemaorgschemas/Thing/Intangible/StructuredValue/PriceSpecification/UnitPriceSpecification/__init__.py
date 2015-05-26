# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.StructuredValue.PriceSpecification import minPriceProp, priceCurrencyProp, priceProp, maxPriceProp, eligibleTransactionVolumeProp, valueAddedTaxIncludedProp, eligibleQuantityProp, validThroughProp, validFromProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class UnitPriceSpecificationSchema(SchemaObject):

    """Schema Mixin for UnitPriceSpecification
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The price asked for a given offer by the respective organization or person.
    """

    def __init__(self):
        self.schema = 'UnitPriceSpecification'


class billingIncrementProp(SchemaProperty):

    """
    SchemaField for billingIncrement
    Usage: Include in SchemaObject SchemaFields as your_django_field = billingIncrementProp()  
    schema.org description:This property specifies the minimal quantity and rounding increment that will be the basis for the billing. The unit of measurement is specified by the unitCode property.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'billingIncrement'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


class unitCodeProp(SchemaProperty):

    """
    SchemaField for unitCode
    Usage: Include in SchemaObject SchemaFields as your_django_field = unitCodeProp()  
    schema.org description:The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'unitCode'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class priceTypeProp(SchemaProperty):

    """
    SchemaField for priceType
    Usage: Include in SchemaObject SchemaFields as your_django_field = priceTypeProp()  
    schema.org description:A short text or acronym indicating multiple price specifications for the same offer, e.g. SRP for the suggested retail price or INVOICE for the invoice price, mostly used in the car industry.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'priceType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class unitTextProp(SchemaProperty):

    """
    SchemaField for unitText
    Usage: Include in SchemaObject SchemaFields as your_django_field = unitTextProp()  
    schema.org description:A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for unitCode.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'unitText'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
