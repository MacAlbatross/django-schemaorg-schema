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


AVAILABILITY_CHOICES = (
    ('INSTOCK', 'InStock: Indicates that the item is in stock.'),
    ('INSTOREONLY',
     'InStoreOnly: Indicates that the item is available only at physical locations.'),
    ('LIMITEDAVAILABILITY',
     'LimitedAvailability: Indicates that the item has limited availability.'),
    ('ONLINEONLY',
     'OnlineOnly: Indicates that the item is available only online.'),
    ('OUTOFSTOCK', 'OutOfStock: Indicates that the item is out of stock.'),
    ('PREORDER',
     'PreOrder: Indicates that the item is available for pre-order.'),
    ('SOLDOUT', 'SoldOut: Indicates that the item has sold out.'),
    ('DISCONTINUED',
     'Discontinued: Indicates that the item has been discontinued.'),
)


class availabilityProp(SchemaEnumProperty):

    """
    Enumeration for availability
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'availability'
    choices = AVAILABILITY_CHOICES
    _format_as = "enum"
    adapter = {
        'INSTOCK': 'InStock',
        'INSTOREONLY': 'InStoreOnly',
        'LIMITEDAVAILABILITY': 'LimitedAvailability',
        'ONLINEONLY': 'OnlineOnly',
        'OUTOFSTOCK': 'OutOfStock',
        'PREORDER': 'PreOrder',
        'SOLDOUT': 'SoldOut',
        'DISCONTINUED': 'Discontinued',
    }


# schema.org version 2.0
