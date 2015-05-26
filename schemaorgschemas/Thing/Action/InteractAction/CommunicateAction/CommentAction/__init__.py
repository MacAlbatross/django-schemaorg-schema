# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.InteractAction.CommunicateAction import inLanguageProp, aboutProp, recipientProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CommentActionSchema(SchemaObject):

    """Schema Mixin for CommentAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of generating a comment about a subject.
    """

    def __init__(self):
        self.schema = 'CommentAction'


class resultCommentProp(SchemaProperty):

    """
    SchemaField for resultComment
    Usage: Include in SchemaObject SchemaFields as your_django_field = resultCommentProp()  
    schema.org description:A sub property of result. The Comment created or sent as a result of this action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Comment"""

    _prop_schema = 'resultComment'
    _expected_schema = 'Comment'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
