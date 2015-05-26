# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, nameProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, descriptionProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MapCategoryTypeSchema(SchemaObject):

    """Schema Mixin for MapCategoryType
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An enumeration of several kinds of Map.
    """

    def __init__(self):
        self.schema = 'MapCategoryType'


/MAPTYPE_CHOICES = (
    ('/SEATINGMAP', '/SeatingMap'),
    ('/TRANSITMAP', '/TransitMap'),
    ('/VENUEMAP', '/VenueMap'),
    ('/PARKINGMAP', '/ParkingMap'),
)


class / mapTypeProp(SchemaEnumProperty):

    """
    Enumeration for /mapType
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/mapType'
    choices = /MAPTYPE_CHOICES
    _format_as = "enum"
    adapter = {
        '/SEATINGMAP': '/SeatingMap',
        '/TRANSITMAP': '/TransitMap',
        '/VENUEMAP': '/VenueMap',
        '/PARKINGMAP': '/ParkingMap',
    }


# schema.org version 2.0
