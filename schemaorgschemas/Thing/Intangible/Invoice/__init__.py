# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class InvoiceSchema(SchemaObject):

    """Schema Mixin for Invoice
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A statement of the money due for goods or services; a bill.
    """

    def __init__(self):
        self.schema = 'Invoice'


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


class minimumPaymentDueProp(SchemaProperty):

    """
    SchemaField for minimumPaymentDue
    Usage: Include in SchemaObject SchemaFields as your_django_field = minimumPaymentDueProp()  
    schema.org description:The minimum payment required at this time.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PriceSpecification"""

    _prop_schema = 'minimumPaymentDue'
    _expected_schema = 'PriceSpecification'
    _enum = False
    _format_as = "ForeignKey"


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


class paymentStatusProp(SchemaProperty):

    """
    SchemaField for paymentStatus
    Usage: Include in SchemaObject SchemaFields as your_django_field = paymentStatusProp()  
    schema.org description:The status of payment; whether the invoice has been paid or not.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'paymentStatus'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class totalPaymentDueProp(SchemaProperty):

    """
    SchemaField for totalPaymentDue
    Usage: Include in SchemaObject SchemaFields as your_django_field = totalPaymentDueProp()  
    schema.org description:The total amount due.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PriceSpecification"""

    _prop_schema = 'totalPaymentDue'
    _expected_schema = 'PriceSpecification'
    _enum = False
    _format_as = "ForeignKey"


class billingPeriodProp(SchemaProperty):

    """
    SchemaField for billingPeriod
    Usage: Include in SchemaObject SchemaFields as your_django_field = billingPeriodProp()  
    schema.org description:The time interval used to compute the invoice.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Duration"""

    _prop_schema = 'billingPeriod'
    _expected_schema = 'Duration'
    _enum = False
    _format_as = "TimeField"


class providerProp(SchemaProperty):

    """
    SchemaField for provider
    Usage: Include in SchemaObject SchemaFields as your_django_field = providerProp()  
    schema.org description:The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller. Supersedes carrier.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'provider'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class referencesOrderProp(SchemaProperty):

    """
    SchemaField for referencesOrder
    Usage: Include in SchemaObject SchemaFields as your_django_field = referencesOrderProp()  
    schema.org description:The Order(s) related to this Invoice. One or more Orders may be combined into a single Invoice.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Order"""

    _prop_schema = 'referencesOrder'
    _expected_schema = 'Order'
    _enum = False
    _format_as = "ForeignKey"


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


class scheduledPaymentDateProp(SchemaProperty):

    """
    SchemaField for scheduledPaymentDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = scheduledPaymentDateProp()  
    schema.org description:The date the invoice is scheduled to be paid.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'scheduledPaymentDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class accountIdProp(SchemaProperty):

    """
    SchemaField for accountId
    Usage: Include in SchemaObject SchemaFields as your_django_field = accountIdProp()  
    schema.org description:The identifier for the account the payment will be applied to.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'accountId'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
