# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.StructuredValue.PriceSpecification import minPriceProp, priceCurrencyProp, priceProp, maxPriceProp, eligibleTransactionVolumeProp, valueAddedTaxIncludedProp, eligibleQuantityProp, validThroughProp, validFromProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DeliveryChargeSpecificationSchema(SchemaObject):

    """Schema Mixin for DeliveryChargeSpecification
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The price for the delivery of an offer using a particular delivery method.
    """

    def __init__(self):
        self.schema = 'DeliveryChargeSpecification'


class eligibleRegionProp(SchemaProperty):

    """
    SchemaField for eligibleRegion
    Usage: Include in SchemaObject SchemaFields as your_django_field = eligibleRegionProp()  
    schema.org description:The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'eligibleRegion'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class ineligibleRegionProp(SchemaProperty):

    """
    SchemaField for ineligibleRegion
    Usage: Include in SchemaObject SchemaFields as your_django_field = ineligibleRegionProp()  
    schema.org description:The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'ineligibleRegion'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class appliesToDeliveryMethodProp(SchemaProperty):

    """
    SchemaField for appliesToDeliveryMethod
    Usage: Include in SchemaObject SchemaFields as your_django_field = appliesToDeliveryMethodProp()  
    schema.org description:The delivery method(s) to which the delivery charge or payment charge specification applies.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DeliveryMethod"""

    _prop_schema = 'appliesToDeliveryMethod'
    _expected_schema = 'DeliveryMethod'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
