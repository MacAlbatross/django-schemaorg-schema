# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ItemAvailabilitySchema(SchemaObject):

    """Schema Mixin for ItemAvailability
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A list of possible product availability options.
    """

    def __init__(self):
        self.schema = 'ItemAvailability'


/AVAILABILITY_CHOICES = (
    ('/INSTOCK', '/InStock'),
    ('/INSTOREONLY', '/InStoreOnly'),
    ('/LIMITEDAVAILABILITY', '/LimitedAvailability'),
    ('/ONLINEONLY', '/OnlineOnly'),
    ('/OUTOFSTOCK', '/OutOfStock'),
    ('/PREORDER', '/PreOrder'),
    ('/SOLDOUT', '/SoldOut'),
    ('/DISCONTINUED', '/Discontinued'),
)


class / availabilityProp(SchemaEnumProperty):

    """
    Enumeration for /availability
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/availability'
    choices = /AVAILABILITY_CHOICES
    _format_as = "enum"
    adapter = {
        '/INSTOCK': '/InStock',
        '/INSTOREONLY': '/InStoreOnly',
        '/LIMITEDAVAILABILITY': '/LimitedAvailability',
        '/ONLINEONLY': '/OnlineOnly',
        '/OUTOFSTOCK': '/OutOfStock',
        '/PREORDER': '/PreOrder',
        '/SOLDOUT': '/SoldOut',
        '/DISCONTINUED': '/Discontinued',
    }


# schema.org version 2.0
