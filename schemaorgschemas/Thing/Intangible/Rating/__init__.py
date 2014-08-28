# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RatingSchema(SchemaObject):

    """Schema Mixin for Rating
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The rating of the video.
    """

    def __init__(self):
        self.schema = 'Rating'


class worstRatingProp(SchemaProperty):

    """
    SchemaField for worstRating
    Usage: Include in SchemaObject SchemaFields as your_django_field = worstRatingProp()
    schema.org description:The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Number"""

    _prop_schema = 'worstRating'
    _expected_schema = 'Number'
    _enum = False
    _format_as = "FloatField"


class ratingValueProp(SchemaProperty):

    """
    SchemaField for ratingValue
    Usage: Include in SchemaObject SchemaFields as your_django_field = ratingValueProp()
    schema.org description:The rating for the content.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'ratingValue'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class bestRatingProp(SchemaProperty):

    """
    SchemaField for bestRating
    Usage: Include in SchemaObject SchemaFields as your_django_field = bestRatingProp()
    schema.org description:The highest value allowed in this rating system. If bestRating is omitted, 5 is assumed.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'bestRating'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"
