# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class GeoShapeSchema(SchemaObject):

    """Schema Mixin for GeoShape
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The geographic shape of a place.
    """

    def __init__(self):
        self.schema = 'GeoShape'


class boxProp(SchemaProperty):

    """
    SchemaField for box
    Usage: Include in SchemaObject SchemaFields as your_django_field = boxProp()
    schema.org description:A polygon is the area enclosed by a point-to-point path for which the starting and ending points are the same. A polygon is expressed as a series of four or more spacedelimited points where the first and final points are identical.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'box'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class circleProp(SchemaProperty):

    """
    SchemaField for circle
    Usage: Include in SchemaObject SchemaFields as your_django_field = circleProp()
    schema.org description:A circle is the circular region of a specified radius centered at a specified latitude and longitude. A circle is expressed as a pair followed by a radius in meters.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'circle'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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


class lineProp(SchemaProperty):

    """
    SchemaField for line
    Usage: Include in SchemaObject SchemaFields as your_django_field = lineProp()
    schema.org description:A line is a point-to-point path consisting of two or more points. A line is expressed as a series of two or more point objects separated by space.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'line'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class polygonProp(SchemaProperty):

    """
    SchemaField for polygon
    Usage: Include in SchemaObject SchemaFields as your_django_field = polygonProp()
    schema.org description:A polygon is the area enclosed by a point-to-point path for which the starting and ending points are the same. A polygon is expressed as a series of four or more space delimited points where the first and final points are identical.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'polygon'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
