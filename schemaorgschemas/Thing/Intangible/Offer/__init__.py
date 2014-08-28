# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OfferSchema(SchemaObject):

    """Schema Mixin for Offer
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An offer to transfer some rights to an item or to provide a service-for example, an offer to sell tickets to an event, to rent the DVD of a movie, to stream a TV show over the internet, to repair a motorcycle, or to loan a book.
    """

    def __init__(self):
        self.schema = 'Offer'


class warrantyProp(SchemaProperty):

    """
    SchemaField for warranty
    Usage: Include in SchemaObject SchemaFields as your_django_field = warrantyProp()  
    schema.org description:The warranty promise(s) included in the offer.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference WarrantyPromise"""

    _prop_schema = 'warranty'
    _expected_schema = 'WarrantyPromise'
    _enum = False
    _format_as = "ForeignKey"


class inventoryLevelProp(SchemaProperty):

    """
    SchemaField for inventoryLevel
    Usage: Include in SchemaObject SchemaFields as your_django_field = inventoryLevelProp()  
    schema.org description:The current approximate inventory level for the item or items.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'inventoryLevel'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class serialNumberProp(SchemaProperty):

    """
    SchemaField for serialNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = serialNumberProp()  
    schema.org description:The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'serialNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class availableAtOrFromProp(SchemaProperty):

    """
    SchemaField for availableAtOrFrom
    Usage: Include in SchemaObject SchemaFields as your_django_field = availableAtOrFromProp()  
    schema.org description:The place(s) from which the offer can be obtained (e.g. store locations).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'availableAtOrFrom'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"


class priceValidUntilProp(SchemaProperty):

    """
    SchemaField for priceValidUntil
    Usage: Include in SchemaObject SchemaFields as your_django_field = priceValidUntilProp()  
    schema.org description:The date after which the price is no longer available.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'priceValidUntil'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class mpnProp(SchemaProperty):

    """
    SchemaField for mpn
    Usage: Include in SchemaObject SchemaFields as your_django_field = mpnProp()  
    schema.org description:The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'mpn'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class eligibleRegionProp(SchemaProperty):

    """
    SchemaField for eligibleRegion
    Usage: Include in SchemaObject SchemaFields as your_django_field = eligibleRegionProp()  
    schema.org description:The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'eligibleRegion'
    _expected_schema = None
    _enum = False
    _format_as = "CharField"


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


class eligibleCustomerTypeProp(SchemaProperty):

    """
    SchemaField for eligibleCustomerType
    Usage: Include in SchemaObject SchemaFields as your_django_field = eligibleCustomerTypeProp()  
    schema.org description:The type(s) of customers for which the given offer is valid.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference BusinessEntityType"""

    _prop_schema = 'eligibleCustomerType'
    _expected_schema = 'BusinessEntityType'
    _enum = False
    _format_as = "ForeignKey"


class priceSpecificationProp(SchemaProperty):

    """
    SchemaField for priceSpecification
    Usage: Include in SchemaObject SchemaFields as your_django_field = priceSpecificationProp()  
    schema.org description:One or more detailed price specifications, indicating the unit price and delivery or payment charges.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PriceSpecification"""

    _prop_schema = 'priceSpecification'
    _expected_schema = 'PriceSpecification'
    _enum = False
    _format_as = "ForeignKey"


class acceptedPaymentMethodProp(SchemaProperty):

    """
    SchemaField for acceptedPaymentMethod
    Usage: Include in SchemaObject SchemaFields as your_django_field = acceptedPaymentMethodProp()  
    schema.org description:The payment method(s) accepted by seller for this offer.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PaymentMethod"""

    _prop_schema = 'acceptedPaymentMethod'
    _expected_schema = 'PaymentMethod'
    _enum = False
    _format_as = "ForeignKey"


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


class deliveryLeadTimeProp(SchemaProperty):

    """
    SchemaField for deliveryLeadTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = deliveryLeadTimeProp()  
    schema.org description:The typical delay between the receipt of the order and the goods leaving the warehouse.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'deliveryLeadTime'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


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


class aggregateRatingProp(SchemaProperty):

    """
    SchemaField for aggregateRating
    Usage: Include in SchemaObject SchemaFields as your_django_field = aggregateRatingProp()  
    schema.org description:The overall rating, based on a collection of reviews or ratings, of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AggregateRating"""

    _prop_schema = 'aggregateRating'
    _expected_schema = 'AggregateRating'
    _enum = False
    _format_as = "ForeignKey"


class skuProp(SchemaProperty):

    """
    SchemaField for sku
    Usage: Include in SchemaObject SchemaFields as your_django_field = skuProp()  
    schema.org description:The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'sku'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class itemConditionProp(SchemaProperty):

    """
    SchemaField for itemCondition
    Usage: Include in SchemaObject SchemaFields as your_django_field = itemConditionProp()  
    schema.org description:A predefined value from OfferItemCondition or a textual description of the condition of the product or service, or the products or services included in the offer.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference OfferItemCondition"""

    _prop_schema = 'itemCondition'
    _expected_schema = 'OfferItemCondition'
    _enum = False
    _format_as = "ForeignKey"


class gtin8Prop(SchemaProperty):

    """
    SchemaField for gtin8
    Usage: Include in SchemaObject SchemaFields as your_django_field = gtin8Prop()  
    schema.org description:The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'gtin8'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class availabilityProp(SchemaProperty):

    """
    SchemaField for availability
    Usage: Include in SchemaObject SchemaFields as your_django_field = availabilityProp()  
    schema.org description:The availability of this item-for example In stock, Out of stock, Pre-order, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ItemAvailability"""

    _prop_schema = 'availability'
    _expected_schema = 'ItemAvailability'
    _enum = False
    _format_as = "ForeignKey"


class categoryProp(SchemaProperty):

    """
    SchemaField for category
    Usage: Include in SchemaObject SchemaFields as your_django_field = categoryProp()  
    schema.org description:A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'category'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class availabilityStartsProp(SchemaProperty):

    """
    SchemaField for availabilityStarts
    Usage: Include in SchemaObject SchemaFields as your_django_field = availabilityStartsProp()  
    schema.org description:The beginning of the availability of the product or service included in the offer.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'availabilityStarts'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class availabilityEndsProp(SchemaProperty):

    """
    SchemaField for availabilityEnds
    Usage: Include in SchemaObject SchemaFields as your_django_field = availabilityEndsProp()  
    schema.org description:The end of the availability of the product or service included in the offer.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'availabilityEnds'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class gtin14Prop(SchemaProperty):

    """
    SchemaField for gtin14
    Usage: Include in SchemaObject SchemaFields as your_django_field = gtin14Prop()  
    schema.org description:The GTIN-14 code of the product, or the product to which the offer refers.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'gtin14'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class reviewProp(SchemaProperty):

    """
    SchemaField for review
    Usage: Include in SchemaObject SchemaFields as your_django_field = reviewProp()  
    schema.org description:A review of the item. Supercedes reviews.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Review"""

    _prop_schema = 'review'
    _expected_schema = 'Review'
    _enum = False
    _format_as = "ForeignKey"


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


class itemOfferedProp(SchemaProperty):

    """
    SchemaField for itemOffered
    Usage: Include in SchemaObject SchemaFields as your_django_field = itemOfferedProp()  
    schema.org description:The item being offered.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Product"""

    _prop_schema = 'itemOffered'
    _expected_schema = 'Product'
    _enum = False
    _format_as = "TextField"


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


class sellerProp(SchemaProperty):

    """
    SchemaField for seller
    Usage: Include in SchemaObject SchemaFields as your_django_field = sellerProp()  
    schema.org description:The organization or person making the offer.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'seller'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class includesObjectProp(SchemaProperty):

    """
    SchemaField for includesObject
    Usage: Include in SchemaObject SchemaFields as your_django_field = includesObjectProp()  
    schema.org description:This links to a node or nodes indicating the exact quantity of the products included in the offer.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference TypeAndQuantityNode"""

    _prop_schema = 'includesObject'
    _expected_schema = 'TypeAndQuantityNode'
    _enum = False
    _format_as = "ForeignKey"


class availableDeliveryMethodProp(SchemaProperty):

    """
    SchemaField for availableDeliveryMethod
    Usage: Include in SchemaObject SchemaFields as your_django_field = availableDeliveryMethodProp()  
    schema.org description:The delivery method(s) available for this offer.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DeliveryMethod"""

    _prop_schema = 'availableDeliveryMethod'
    _expected_schema = 'DeliveryMethod'
    _enum = False
    _format_as = "ForeignKey"


class advanceBookingRequirementProp(SchemaProperty):

    """
    SchemaField for advanceBookingRequirement
    Usage: Include in SchemaObject SchemaFields as your_django_field = advanceBookingRequirementProp()  
    schema.org description:The amount of time that is required between accepting the offer and the actual usage of the resource or service.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'advanceBookingRequirement'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class gtin13Prop(SchemaProperty):

    """
    SchemaField for gtin13
    Usage: Include in SchemaObject SchemaFields as your_django_field = gtin13Prop()  
    schema.org description:The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceeding zero.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'gtin13'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class eligibleDurationProp(SchemaProperty):

    """
    SchemaField for eligibleDuration
    Usage: Include in SchemaObject SchemaFields as your_django_field = eligibleDurationProp()  
    schema.org description:The duration for which the given offer is valid.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'eligibleDuration'
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


class addOnProp(SchemaProperty):

    """
    SchemaField for addOn
    Usage: Include in SchemaObject SchemaFields as your_django_field = addOnProp()  
    schema.org description:An additional offer that can only be obtained in combination with the first base offer (e.g. supplements and extensions that are available for a surcharge).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Offer"""

    _prop_schema = 'addOn'
    _expected_schema = 'Offer'
    _enum = False
    _format_as = "ForeignKey"
