# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OrderSchema(SchemaObject):

    """Schema Mixin for Order
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented by an Offer that has been accepted by the customer.
    """

    def __init__(self):
        self.schema = 'Order'


class customerProp(SchemaProperty):

    """
    SchemaField for customer
    Usage: Include in SchemaObject SchemaFields as your_django_field = customerProp()  
    schema.org description:Party placing the order.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'customer'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class merchantProp(SchemaProperty):

    """
    SchemaField for merchant
    Usage: Include in SchemaObject SchemaFields as your_django_field = merchantProp()  
    schema.org description:The party taking the order (e.g. Amazon.com is a merchant for many sellers).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'merchant'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class paymentMethodIdProp(SchemaProperty):

    """
    SchemaField for paymentMethodId
    Usage: Include in SchemaObject SchemaFields as your_django_field = paymentMethodIdProp()  
    schema.org description:An identifier for the method of payment used (e.g. the last 4 digits of the credit card).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'paymentMethodId'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class orderNumberProp(SchemaProperty):

    """
    SchemaField for orderNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = orderNumberProp()  
    schema.org description:The identifier of the transaction.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'orderNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class paymentMethodProp(SchemaProperty):

    """
    SchemaField for paymentMethod
    Usage: Include in SchemaObject SchemaFields as your_django_field = paymentMethodProp()  
    schema.org description:The name of the credit card or other method of payment for the order.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PaymentMethod"""

    _prop_schema = 'paymentMethod'
    _expected_schema = 'PaymentMethod'
    _enum = False
    _format_as = "ForeignKey"


class discountCodeProp(SchemaProperty):

    """
    SchemaField for discountCode
    Usage: Include in SchemaObject SchemaFields as your_django_field = discountCodeProp()  
    schema.org description:Code used to redeem a discount.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'discountCode'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class paymentDueProp(SchemaProperty):

    """
    SchemaField for paymentDue
    Usage: Include in SchemaObject SchemaFields as your_django_field = paymentDueProp()  
    schema.org description:The date that payment is due.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'paymentDue'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class orderedItemProp(SchemaProperty):

    """
    SchemaField for orderedItem
    Usage: Include in SchemaObject SchemaFields as your_django_field = orderedItemProp()  
    schema.org description:The item ordered.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Product"""

    _prop_schema = 'orderedItem'
    _expected_schema = 'Product'
    _enum = False
    _format_as = "TextField"


class acceptedOfferProp(SchemaProperty):

    """
    SchemaField for acceptedOffer
    Usage: Include in SchemaObject SchemaFields as your_django_field = acceptedOfferProp()  
    schema.org description:The offer(s) -- e.g., product, quantity and price combinations -- included in the order.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Offer"""

    _prop_schema = 'acceptedOffer'
    _expected_schema = 'Offer'
    _enum = False
    _format_as = "ForeignKey"


class paymentUrlProp(SchemaProperty):

    """
    SchemaField for paymentUrl
    Usage: Include in SchemaObject SchemaFields as your_django_field = paymentUrlProp()  
    schema.org description:The URL for sending a payment.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'paymentUrl'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


class discountProp(SchemaProperty):

    """
    SchemaField for discount
    Usage: Include in SchemaObject SchemaFields as your_django_field = discountProp()  
    schema.org description:Any discount applied (to an Order).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'discount'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


class billingAddressProp(SchemaProperty):

    """
    SchemaField for billingAddress
    Usage: Include in SchemaObject SchemaFields as your_django_field = billingAddressProp()  
    schema.org description:The billing address for the order.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PostalAddress"""

    _prop_schema = 'billingAddress'
    _expected_schema = 'PostalAddress'
    _enum = False
    _format_as = "ForeignKey"


class discountCurrencyProp(SchemaProperty):

    """
    SchemaField for discountCurrency
    Usage: Include in SchemaObject SchemaFields as your_django_field = discountCurrencyProp()  
    schema.org description:The currency (in 3-letter ISO 4217 format) of the discount.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'discountCurrency'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class confirmationNumberProp(SchemaProperty):

    """
    SchemaField for confirmationNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = confirmationNumberProp()  
    schema.org description:A number that confirms the given order.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'confirmationNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class isGiftProp(SchemaProperty):

    """
    SchemaField for isGift
    Usage: Include in SchemaObject SchemaFields as your_django_field = isGiftProp()  
    schema.org description:Was the offer accepted as a gift for someone other than the buyer.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'isGift'
    _expected_schema = None
    _enum = False
    _format_as = "BooleanField"


class orderDateProp(SchemaProperty):

    """
    SchemaField for orderDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = orderDateProp()  
    schema.org description:Date order was placed.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'orderDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class orderStatusProp(SchemaProperty):

    """
    SchemaField for orderStatus
    Usage: Include in SchemaObject SchemaFields as your_django_field = orderStatusProp()  
    schema.org description:The current status of the order.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference OrderStatus"""

    _prop_schema = 'orderStatus'
    _expected_schema = 'OrderStatus'
    _enum = False
    _format_as = "ForeignKey"
