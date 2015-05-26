# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OrderStatusSchema(SchemaObject):

    """Schema Mixin for OrderStatus
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Enumerated status values for Order.
    """

    def __init__(self):
        self.schema = 'OrderStatus'


/ORDERSTATUS_CHOICES = (
    ('/ORDERDELIVERED', '/OrderDelivered'),
    ('/ORDERINTRANSIT', '/OrderInTransit'),
    ('/ORDERPAYMENTDUE', '/OrderPaymentDue'),
    ('/ORDERPICKUPAVAILABLE', '/OrderPickupAvailable'),
    ('/ORDERPROBLEM', '/OrderProblem'),
    ('/ORDERPROCESSING', '/OrderProcessing'),
    ('/ORDERRETURNED', '/OrderReturned'),
    ('/ORDERCANCELLED', '/OrderCancelled'),
)


class / orderStatusProp(SchemaEnumProperty):

    """
    Enumeration for /orderStatus
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/orderStatus'
    choices = /ORDERSTATUS_CHOICES
    _format_as = "enum"
    adapter = {
        '/ORDERDELIVERED': '/OrderDelivered',
        '/ORDERINTRANSIT': '/OrderInTransit',
        '/ORDERPAYMENTDUE': '/OrderPaymentDue',
        '/ORDERPICKUPAVAILABLE': '/OrderPickupAvailable',
        '/ORDERPROBLEM': '/OrderProblem',
        '/ORDERPROCESSING': '/OrderProcessing',
        '/ORDERRETURNED': '/OrderReturned',
        '/ORDERCANCELLED': '/OrderCancelled',
    }


/ORDERITEMSTATUS_CHOICES = (
    ('/ORDERDELIVERED', '/OrderDelivered'),
    ('/ORDERINTRANSIT', '/OrderInTransit'),
    ('/ORDERPAYMENTDUE', '/OrderPaymentDue'),
    ('/ORDERPICKUPAVAILABLE', '/OrderPickupAvailable'),
    ('/ORDERPROBLEM', '/OrderProblem'),
    ('/ORDERPROCESSING', '/OrderProcessing'),
    ('/ORDERRETURNED', '/OrderReturned'),
    ('/ORDERCANCELLED', '/OrderCancelled'),
)


class / orderItemStatusProp(SchemaEnumProperty):

    """
    Enumeration for /orderItemStatus
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/orderItemStatus'
    choices = /ORDERITEMSTATUS_CHOICES
    _format_as = "enum"
    adapter = {
        '/ORDERDELIVERED': '/OrderDelivered',
        '/ORDERINTRANSIT': '/OrderInTransit',
        '/ORDERPAYMENTDUE': '/OrderPaymentDue',
        '/ORDERPICKUPAVAILABLE': '/OrderPickupAvailable',
        '/ORDERPROBLEM': '/OrderProblem',
        '/ORDERPROCESSING': '/OrderProcessing',
        '/ORDERRETURNED': '/OrderReturned',
        '/ORDERCANCELLED': '/OrderCancelled',
    }


# schema.org version 2.0
