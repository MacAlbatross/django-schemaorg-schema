# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ItemListOrderTypeSchema(SchemaObject):

    """Schema Mixin for ItemListOrderType
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.
    """

    def __init__(self):
        self.schema = 'ItemListOrderType'


/ITEMLISTORDER_CHOICES = (
    ('/ITEMLISTORDERDESCENDING', '/ItemListOrderDescending'),
    ('/ITEMLISTUNORDERED', '/ItemListUnordered'),
    ('/ITEMLISTORDERASCENDING', '/ItemListOrderAscending'),
)


class / itemListOrderProp(SchemaEnumProperty):

    """
    Enumeration for /itemListOrder
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/itemListOrder'
    choices = /ITEMLISTORDER_CHOICES
    _format_as = "enum"
    adapter = {
        '/ITEMLISTORDERDESCENDING': '/ItemListOrderDescending',
        '/ITEMLISTUNORDERED': '/ItemListUnordered',
        '/ITEMLISTORDERASCENDING': '/ItemListOrderAscending',
    }


# schema.org version 2.0
