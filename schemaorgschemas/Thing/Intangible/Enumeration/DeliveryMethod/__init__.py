# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DeliveryMethodSchema(SchemaObject):

    """Schema Mixin for DeliveryMethod
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A delivery method is a standardized procedure for transferring the product or service to the destination of fulfillment chosen by the customer. Delivery methods are characterized by the means of transportation used, and by the organization or group that is the contracting party for the sending organization or person.

    Commonly used values:

    http://purl.org/goodrelations/v1#DeliveryModeDirectDownload 
    http://purl.org/goodrelations/v1#DeliveryModeFreight 
    http://purl.org/goodrelations/v1#DeliveryModeMail 
    http://purl.org/goodrelations/v1#DeliveryModeOwnFleet 
    http://purl.org/goodrelations/v1#DeliveryModePickUp 
    http://purl.org/goodrelations/v1#DHL 
    http://purl.org/goodrelations/v1#FederalExpress 
    http://purl.org/goodrelations/v1#UPS 

    """

    def __init__(self):
        self.schema = 'DeliveryMethod'


/HASDELIVERYMETHOD_CHOICES = (
    ('/ONSITEPICKUP', '/OnSitePickup'),
)


class / hasDeliveryMethodProp(SchemaEnumProperty):

    """
    Enumeration for /hasDeliveryMethod
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/hasDeliveryMethod'
    choices = /HASDELIVERYMETHOD_CHOICES
    _format_as = "enum"
    adapter = {
        '/ONSITEPICKUP': '/OnSitePickup',
    }


/DELIVERYMETHOD_CHOICES = (
    ('/ONSITEPICKUP', '/OnSitePickup'),
)


class / deliveryMethodProp(SchemaEnumProperty):

    """
    Enumeration for /deliveryMethod
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/deliveryMethod'
    choices = /DELIVERYMETHOD_CHOICES
    _format_as = "enum"
    adapter = {
        '/ONSITEPICKUP': '/OnSitePickup',
    }


/AVAILABLEDELIVERYMETHOD_CHOICES = (
    ('/ONSITEPICKUP', '/OnSitePickup'),
)


class / availableDeliveryMethodProp(SchemaEnumProperty):

    """
    Enumeration for /availableDeliveryMethod
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/availableDeliveryMethod'
    choices = /AVAILABLEDELIVERYMETHOD_CHOICES
    _format_as = "enum"
    adapter = {
        '/ONSITEPICKUP': '/OnSitePickup',
    }


/APPLIESTODELIVERYMETHOD_CHOICES = (
    ('/ONSITEPICKUP', '/OnSitePickup'),
)


class / appliesToDeliveryMethodProp(SchemaEnumProperty):

    """
    Enumeration for /appliesToDeliveryMethod
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/appliesToDeliveryMethod'
    choices = /APPLIESTODELIVERYMETHOD_CHOICES
    _format_as = "enum"
    adapter = {
        '/ONSITEPICKUP': '/OnSitePickup',
    }


# schema.org version 2.0
