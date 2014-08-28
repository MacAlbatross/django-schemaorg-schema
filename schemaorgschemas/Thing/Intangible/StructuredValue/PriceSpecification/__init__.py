# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PriceSpecificationSchema(SchemaObject):

    """Schema Mixin for PriceSpecification
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A structured value representing a monetary amount. Typically, only the subclasses of this type are used for markup.
    """

    def __init__(self):
        self.schema = 'PriceSpecification'


class eligibleQuantityProp(SchemaProperty):

    """
    SchemaField for eligibleQuantity
    Usage: Include in SchemaObject SchemaFields as your_django_field = eligibleQuantityProp()  
    schema.org description:The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'eligibleQuantity'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class validFromProp(SchemaProperty):

    """
    SchemaField for validFrom
    Usage: Include in SchemaObject SchemaFields as your_django_field = validFromProp()  
    schema.org description:The date when the item becomes valid.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'validFrom'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class validThroughProp(SchemaProperty):

    """
    SchemaField for validThrough
    Usage: Include in SchemaObject SchemaFields as your_django_field = validThroughProp()  
    schema.org description:The end of the validity of offer, price specification, or opening hours data.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'validThrough'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class priceCurrencyProp(SchemaProperty):

    """
    SchemaField for priceCurrency
    Usage: Include in SchemaObject SchemaFields as your_django_field = priceCurrencyProp()  
    schema.org description:The currency (in 3-letter ISO 4217 format) of the offer price or a price component, when attached to PriceSpecification and its subtypes.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'priceCurrency'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class priceProp(SchemaProperty):

    """
    SchemaField for price
    Usage: Include in SchemaObject SchemaFields as your_django_field = priceProp()  
    schema.org description:The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'price'
    _expected_schema = None
    _enum = False
    _format_as = "DecimalField"


class minPriceProp(SchemaProperty):

    """
    SchemaField for minPrice
    Usage: Include in SchemaObject SchemaFields as your_django_field = minPriceProp()  
    schema.org description:The lowest price if the price is a range.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'minPrice'
    _expected_schema = None
    _enum = False
    _format_as = "DecimalField"


class maxPriceProp(SchemaProperty):

    """
    SchemaField for maxPrice
    Usage: Include in SchemaObject SchemaFields as your_django_field = maxPriceProp()  
    schema.org description:The highest price if the price is a range.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'maxPrice'
    _expected_schema = None
    _enum = False
    _format_as = "DecimalField"


class eligibleTransactionVolumeProp(SchemaProperty):

    """
    SchemaField for eligibleTransactionVolume
    Usage: Include in SchemaObject SchemaFields as your_django_field = eligibleTransactionVolumeProp()  
    schema.org description:The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PriceSpecification"""

    _prop_schema = 'eligibleTransactionVolume'
    _expected_schema = 'PriceSpecification'
    _enum = False
    _format_as = "ForeignKey"


class valueAddedTaxIncludedProp(SchemaProperty):

    """
    SchemaField for valueAddedTaxIncluded
    Usage: Include in SchemaObject SchemaFields as your_django_field = valueAddedTaxIncludedProp()  
    schema.org description:Specifies whether the applicable value-added tax (VAT) is included in the price specification or not.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'valueAddedTaxIncluded'
    _expected_schema = None
    _enum = False
    _format_as = "BooleanField"
