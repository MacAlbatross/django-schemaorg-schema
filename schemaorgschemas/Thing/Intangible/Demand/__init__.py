# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DemandSchema(SchemaObject):

    """Schema Mixin for Demand
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement by an organization or person to seek a certain type of goods or services. For describing demand using this type, the very same properties used for Offer apply.
    """

    def __init__(self):
        self.schema = 'Demand'


class warrantyProp(SchemaProperty):

    """
    SchemaField for warranty
    Usage: Include in SchemaObject SchemaFields as your_django_field = warrantyProp()  
    schema.org description:The warranty promise(s) included in the offer. Supersedes warrantyPromise.

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
    schema.org description:The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'eligibleRegion'
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


class gtin8Prop(SchemaProperty):

    """
    SchemaField for gtin8
    Usage: Include in SchemaObject SchemaFields as your_django_field = gtin8Prop()  
    schema.org description:The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See GS1 GTIN Summary for more details.

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
    schema.org description:The availability of this itemfor example In stock, Out of stock, Pre-order, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ItemAvailability"""

    _prop_schema = 'availability'
    _expected_schema = 'ItemAvailability'
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
    schema.org description:The GTIN-14 code of the product, or the product to which the offer refers. See GS1 GTIN Summary for more details.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'gtin14'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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


class sellerProp(SchemaProperty):

    """
    SchemaField for seller
    Usage: Include in SchemaObject SchemaFields as your_django_field = sellerProp()  
    schema.org description:An entity which offers (sells / leases / lends / loans) the services / goods. A seller may also be a provider. Supersedes vendor, merchant.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'seller'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


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
    schema.org description:The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceeding zero. See GS1 GTIN Summary for more details.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'gtin13'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class gtin12Prop(SchemaProperty):

    """
    SchemaField for gtin12
    Usage: Include in SchemaObject SchemaFields as your_django_field = gtin12Prop()  
    schema.org description:The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See GS1 GTIN Summary for more details.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'gtin12'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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


# schema.org version 2.0
