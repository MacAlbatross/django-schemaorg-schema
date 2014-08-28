# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class WarrantyPromiseSchema(SchemaObject):

    """Schema Mixin for WarrantyPromise
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A structured value representing the duration and scope of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.
    """

    def __init__(self):
        self.schema = 'WarrantyPromise'


class durationOfWarrantyProp(SchemaProperty):

    """
    SchemaField for durationOfWarranty
    Usage: Include in SchemaObject SchemaFields as your_django_field = durationOfWarrantyProp()  
    schema.org description:The duration of the warranty promise. Common unitCode values are ANN for year, MON for months, or DAY for days.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'durationOfWarranty'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class warrantyScopeProp(SchemaProperty):

    """
    SchemaField for warrantyScope
    Usage: Include in SchemaObject SchemaFields as your_django_field = warrantyScopeProp()  
    schema.org description:The scope of the warranty promise.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference WarrantyScope"""

    _prop_schema = 'warrantyScope'
    _expected_schema = 'WarrantyScope'
    _enum = False
    _format_as = "ForeignKey"
