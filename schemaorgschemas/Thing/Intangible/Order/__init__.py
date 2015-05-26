# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

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
    schema.org description:Party placing the order or paying the invoice.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'customer'
    _expected_schema = 'Organization'
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


class orderDeliveryProp(SchemaProperty):

    """
    SchemaField for orderDelivery
    Usage: Include in SchemaObject SchemaFields as your_django_field = orderDeliveryProp()  
    schema.org description:The delivery of the parcel related to this order or order item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ParcelDelivery"""

    _prop_schema = 'orderDelivery'
    _expected_schema = 'ParcelDelivery'
    _enum = False
    _format_as = "ForeignKey"


class orderedItemProp(SchemaProperty):

    """
    SchemaField for orderedItem
    Usage: Include in SchemaObject SchemaFields as your_django_field = orderedItemProp()  
    schema.org description:The item ordered.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference OrderItem"""

    _prop_schema = 'orderedItem'
    _expected_schema = 'OrderItem'
    _enum = False
    _format_as = "ForeignKey"


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


class brokerProp(SchemaProperty):

    """
    SchemaField for broker
    Usage: Include in SchemaObject SchemaFields as your_django_field = brokerProp()  
    schema.org description:An entity that arranges for an exchange between a buyer and a seller. In most cases a broker never acquires or releases ownership of a product or service involved in an exchange. If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred. Supersedes bookingAgent.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'broker'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


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


class sellerProp(SchemaProperty):

    """
    SchemaField for seller
    Usage: Include in SchemaObject SchemaFields as your_django_field = sellerProp()  
    schema.org description:An entity which offers (sells / leases / lends / loans) the services / goods. A seller may also be a provider. Supersedes vendor, merchant.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'seller'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


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


class partOfInvoiceProp(SchemaProperty):

    """
    SchemaField for partOfInvoice
    Usage: Include in SchemaObject SchemaFields as your_django_field = partOfInvoiceProp()  
    schema.org description:The order is being paid as part of the referenced Invoice.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Invoice"""

    _prop_schema = 'partOfInvoice'
    _expected_schema = 'Invoice'
    _enum = False
    _format_as = "ForeignKey"


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
    schema.org description:A number that confirms the given order or payment has been received.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'confirmationNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class paymentUrlProp(SchemaProperty):

    """
    SchemaField for paymentUrl
    Usage: Include in SchemaObject SchemaFields as your_django_field = paymentUrlProp()  
    schema.org description:The URL for sending a payment.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference URL"""

    _prop_schema = 'paymentUrl'
    _expected_schema = 'URL'
    _enum = False
    _format_as = "ForeignKey"


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


# schema.org version 2.0
