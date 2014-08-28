# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OpeningHoursSpecificationSchema(SchemaObject):

    """Schema Mixin for OpeningHoursSpecification
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A structured value providing information about the opening hours of a place or a certain service inside a place.
    """

    def __init__(self):
        self.schema = 'OpeningHoursSpecification'


class dayOfWeekProp(SchemaProperty):

    """
    SchemaField for dayOfWeek
    Usage: Include in SchemaObject SchemaFields as your_django_field = dayOfWeekProp()
    schema.org description:The day of the week for which these opening hours are valid.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DayOfWeek"""

    _prop_schema = 'dayOfWeek'
    _expected_schema = 'DayOfWeek'
    _enum = False
    _format_as = "ForeignKey"


class closesProp(SchemaProperty):

    """
    SchemaField for closes
    Usage: Include in SchemaObject SchemaFields as your_django_field = closesProp()
    schema.org description:The closing hour of the place or service on the given day(s) of the week.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'closes'
    _expected_schema = None
    _enum = False
    _format_as = "TimeField"


class validFromProp(SchemaProperty):

    """
    SchemaField for validFrom
    Usage: Include in SchemaObject SchemaFields as your_django_field = validFromProp()
    schema.org description:The date when the item becomes valid.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'validFrom'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class validThroughProp(SchemaProperty):

    """
    SchemaField for validThrough
    Usage: Include in SchemaObject SchemaFields as your_django_field = validThroughProp()
    schema.org description:The end of the validity of offer, price specification, or opening hours data.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'validThrough'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class opensProp(SchemaProperty):

    """
    SchemaField for opens
    Usage: Include in SchemaObject SchemaFields as your_django_field = opensProp()
    schema.org description:The opening hour of the place or service on the given day(s) of the week.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Time"""

    _prop_schema = 'opens'
    _expected_schema = 'Time'
    _enum = False
    _format_as = "ForeignKey"
