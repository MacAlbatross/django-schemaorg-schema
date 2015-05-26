# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OrderItemSchema(SchemaObject):

    """Schema Mixin for OrderItem
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An order item is a line of an order. It includes the quantity and shipping details of a bought offer.
    """

    def __init__(self):
        self.schema = 'OrderItem'


class orderQuantityProp(SchemaProperty):

    """
    SchemaField for orderQuantity
    Usage: Include in SchemaObject SchemaFields as your_django_field = orderQuantityProp()  
    schema.org description:The number of the item ordered. If the property is not set, assume the quantity is one.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'orderQuantity'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


class orderItemStatusProp(SchemaProperty):

    """
    SchemaField for orderItemStatus
    Usage: Include in SchemaObject SchemaFields as your_django_field = orderItemStatusProp()  
    schema.org description:The current status of the order item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference OrderStatus"""

    _prop_schema = 'orderItemStatus'
    _expected_schema = 'OrderStatus'
    _enum = False
    _format_as = "ForeignKey"


class orderItemNumberProp(SchemaProperty):

    """
    SchemaField for orderItemNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = orderItemNumberProp()  
    schema.org description:The identifier of the order item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'orderItemNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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


# schema.org version 2.0
