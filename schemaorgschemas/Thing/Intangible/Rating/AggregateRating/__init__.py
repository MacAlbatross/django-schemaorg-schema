# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Intangible.Rating import worstRatingProp, ratingValueProp, bestRatingProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AggregateRatingSchema(SchemaObject):

    """Schema Mixin for AggregateRating
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The average rating based on multiple ratings or reviews.
    """

    def __init__(self):
        self.schema = 'AggregateRating'


class reviewCountProp(SchemaProperty):

    """
    SchemaField for reviewCount
    Usage: Include in SchemaObject SchemaFields as your_django_field = reviewCountProp()
    schema.org description:The count of total number of reviews.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'reviewCount'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class itemReviewedProp(SchemaProperty):

    """
    SchemaField for itemReviewed
    Usage: Include in SchemaObject SchemaFields as your_django_field = itemReviewedProp()
    schema.org description:The item that is being reviewed/rated.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'itemReviewed'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


class ratingCountProp(SchemaProperty):

    """
    SchemaField for ratingCount
    Usage: Include in SchemaObject SchemaFields as your_django_field = ratingCountProp()
    schema.org description:The count of total number of ratings.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'ratingCount'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"
