# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ReviewActionSchema(SchemaObject):

    """Schema Mixin for ReviewAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of producing a balanced opinion about the object for an audience. An agent reviews an object with participants resulting in a review.
    """

    def __init__(self):
        self.schema = 'ReviewAction'


class resultReviewProp(SchemaProperty):

    """
    SchemaField for resultReview
    Usage: Include in SchemaObject SchemaFields as your_django_field = resultReviewProp()
    schema.org description:A sub property of result. The review that resulted in the performing of the action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Review"""

    _prop_schema = 'resultReview'
    _expected_schema = 'Review'
    _enum = False
    _format_as = "ForeignKey"
