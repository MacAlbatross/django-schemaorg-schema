# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Offer import warrantyProp, ineligibleRegionProp, priceValidUntilProp, eligibleRegionProp, businessFunctionProp, deliveryLeadTimeProp, aggregateRatingProp, skuProp, availabilityProp, categoryProp, includesObjectProp, gtin14Prop, reviewProp, itemOfferedProp, sellerProp, availabilityStartsProp, eligibleDurationProp, addOnProp, inventoryLevelProp, availableAtOrFromProp, mpnProp, priceProp, eligibleCustomerTypeProp, priceSpecificationProp, acceptedPaymentMethodProp, eligibleTransactionVolumeProp, gtin8Prop, eligibleQuantityProp, itemConditionProp, availabilityEndsProp, priceCurrencyProp, serialNumberProp, availableDeliveryMethodProp, advanceBookingRequirementProp, gtin13Prop, gtin12Prop, validFromProp, validThroughProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AggregateOfferSchema(SchemaObject):

    """Schema Mixin for AggregateOffer
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    When a single product is associated with multiple offers (for example, the same pair of shoes is offered by different merchants), then AggregateOffer can be used.
    """

    def __init__(self):
        self.schema = 'AggregateOffer'


class lowPriceProp(SchemaProperty):

    """
    SchemaField for lowPrice
    Usage: Include in SchemaObject SchemaFields as your_django_field = lowPriceProp()  
    schema.org description:The lowest price of all offers available.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'lowPrice'
    _expected_schema = None
    _enum = False
    _format_as = "DecimalField"


class highPriceProp(SchemaProperty):

    """
    SchemaField for highPrice
    Usage: Include in SchemaObject SchemaFields as your_django_field = highPriceProp()  
    schema.org description:The highest price of all offers available.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'highPrice'
    _expected_schema = None
    _enum = False
    _format_as = "DecimalField"


class offersProp(SchemaProperty):

    """
    SchemaField for offers
    Usage: Include in SchemaObject SchemaFields as your_django_field = offersProp()  
    schema.org description:An offer to provide this itemfor example, an offer to sell a product, rent the DVD of a movie, or give away tickets to an event.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Offer"""

    _prop_schema = 'offers'
    _expected_schema = 'Offer'
    _enum = False
    _format_as = "ForeignKey"


class offerCountProp(SchemaProperty):

    """
    SchemaField for offerCount
    Usage: Include in SchemaObject SchemaFields as your_django_field = offerCountProp()  
    schema.org description:The number of offers for the product.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Integer"""

    _prop_schema = 'offerCount'
    _expected_schema = 'Integer'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
