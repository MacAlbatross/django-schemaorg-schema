# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class GeoCoordinatesSchema(SchemaObject):

    """Schema Mixin for GeoCoordinates
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The geographic coordinates of a place or event.
    """

    def __init__(self):
        self.schema = 'GeoCoordinates'


class latitudeProp(SchemaProperty):

    """
    SchemaField for latitude
    Usage: Include in SchemaObject SchemaFields as your_django_field = latitudeProp()  
    schema.org description:The latitude of a location. For example 37.42242.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'latitude'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


class elevationProp(SchemaProperty):

    """
    SchemaField for elevation
    Usage: Include in SchemaObject SchemaFields as your_django_field = elevationProp()  
    schema.org description:The elevation of a location.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'elevation'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


class longitudeProp(SchemaProperty):

    """
    SchemaField for longitude
    Usage: Include in SchemaObject SchemaFields as your_django_field = longitudeProp()  
    schema.org description:The longitude of a location. For example -122.08585.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'longitude'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


# schema.org version 2.0
