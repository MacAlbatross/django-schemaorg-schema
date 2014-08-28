# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.StructuredValue.PriceSpecification import validFromProp, priceCurrencyProp, priceProp, maxPriceProp, eligibleTransactionVolumeProp, valueAddedTaxIncludedProp, eligibleQuantityProp, validThroughProp, minPriceProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PaymentChargeSpecificationSchema(SchemaObject):

    """Schema Mixin for PaymentChargeSpecification
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The costs of settling the payment using a particular payment method.
    """

    def __init__(self):
        self.schema = 'PaymentChargeSpecification'


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


class appliesToPaymentMethodProp(SchemaProperty):

    """
    SchemaField for appliesToPaymentMethod
    Usage: Include in SchemaObject SchemaFields as your_django_field = appliesToPaymentMethodProp()
    schema.org description:The payment method(s) to which the payment charge specification applies.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PaymentMethod"""

    _prop_schema = 'appliesToPaymentMethod'
    _expected_schema = 'PaymentMethod'
    _enum = False
    _format_as = "ForeignKey"
