# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ParcelDeliverySchema(SchemaObject):

    """Schema Mixin for ParcelDelivery
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The delivery of a parcel either via the postal service or a commercial service.
    """

    def __init__(self):
        self.schema = 'ParcelDelivery'


class itemShippedProp(SchemaProperty):

    """
    SchemaField for itemShipped
    Usage: Include in SchemaObject SchemaFields as your_django_field = itemShippedProp()  
    schema.org description:Item(s) being shipped.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Product"""

    _prop_schema = 'itemShipped'
    _expected_schema = 'Product'
    _enum = False
    _format_as = "TextField"


class originAddressProp(SchemaProperty):

    """
    SchemaField for originAddress
    Usage: Include in SchemaObject SchemaFields as your_django_field = originAddressProp()  
    schema.org description:Shipper&#39;s address.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PostalAddress"""

    _prop_schema = 'originAddress'
    _expected_schema = 'PostalAddress'
    _enum = False
    _format_as = "ForeignKey"


class expectedArrivalFromProp(SchemaProperty):

    """
    SchemaField for expectedArrivalFrom
    Usage: Include in SchemaObject SchemaFields as your_django_field = expectedArrivalFromProp()  
    schema.org description:The earliest date the package may arrive.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'expectedArrivalFrom'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class hasDeliveryMethodProp(SchemaProperty):

    """
    SchemaField for hasDeliveryMethod
    Usage: Include in SchemaObject SchemaFields as your_django_field = hasDeliveryMethodProp()  
    schema.org description:Method used for delivery or shipping.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DeliveryMethod"""

    _prop_schema = 'hasDeliveryMethod'
    _expected_schema = 'DeliveryMethod'
    _enum = False
    _format_as = "ForeignKey"


class providerProp(SchemaProperty):

    """
    SchemaField for provider
    Usage: Include in SchemaObject SchemaFields as your_django_field = providerProp()  
    schema.org description:The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller. Supersedes carrier.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'provider'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class trackingUrlProp(SchemaProperty):

    """
    SchemaField for trackingUrl
    Usage: Include in SchemaObject SchemaFields as your_django_field = trackingUrlProp()  
    schema.org description:Tracking url for the parcel delivery.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference URL"""

    _prop_schema = 'trackingUrl'
    _expected_schema = 'URL'
    _enum = False
    _format_as = "ForeignKey"


class deliveryStatusProp(SchemaProperty):

    """
    SchemaField for deliveryStatus
    Usage: Include in SchemaObject SchemaFields as your_django_field = deliveryStatusProp()  
    schema.org description:New entry added as the package passes through each leg of its journey (from shipment to final delivery).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DeliveryEvent"""

    _prop_schema = 'deliveryStatus'
    _expected_schema = 'DeliveryEvent'
    _enum = False
    _format_as = "ForeignKey"


class expectedArrivalUntilProp(SchemaProperty):

    """
    SchemaField for expectedArrivalUntil
    Usage: Include in SchemaObject SchemaFields as your_django_field = expectedArrivalUntilProp()  
    schema.org description:The latest date the package may arrive.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'expectedArrivalUntil'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class deliveryAddressProp(SchemaProperty):

    """
    SchemaField for deliveryAddress
    Usage: Include in SchemaObject SchemaFields as your_django_field = deliveryAddressProp()  
    schema.org description:Destination address.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PostalAddress"""

    _prop_schema = 'deliveryAddress'
    _expected_schema = 'PostalAddress'
    _enum = False
    _format_as = "ForeignKey"


class trackingNumberProp(SchemaProperty):

    """
    SchemaField for trackingNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = trackingNumberProp()  
    schema.org description:Shipper tracking number.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'trackingNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class partOfOrderProp(SchemaProperty):

    """
    SchemaField for partOfOrder
    Usage: Include in SchemaObject SchemaFields as your_django_field = partOfOrderProp()  
    schema.org description:The overall order the items in this delivery were included in.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Order"""

    _prop_schema = 'partOfOrder'
    _expected_schema = 'Order'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
