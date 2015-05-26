# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EngineSpecificationSchema(SchemaObject):

    """Schema Mixin for EngineSpecification
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Information about the engine of the vehicle. A vehicle can have multiple engines represented by multiple engine specification entities.
    """

    def __init__(self):
        self.schema = 'EngineSpecification'


class fuelTypeProp(SchemaProperty):

    """
    SchemaField for fuelType
    Usage: Include in SchemaObject SchemaFields as your_django_field = fuelTypeProp()  
    schema.org description:The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only one engine, this property can be attached directly to the vehicle.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'fuelType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
