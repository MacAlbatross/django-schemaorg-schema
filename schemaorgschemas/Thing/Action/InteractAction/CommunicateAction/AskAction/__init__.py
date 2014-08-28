# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.InteractAction.CommunicateAction import aboutProp, recipientProp, languageProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AskActionSchema(SchemaObject):

    """Schema Mixin for AskAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of posing a question / favor to someone.Related actions:ReplyAction: Appears generally as a response to AskAction.
    """

    def __init__(self):
        self.schema = 'AskAction'


class questionProp(SchemaProperty):

    """
    SchemaField for question
    Usage: Include in SchemaObject SchemaFields as your_django_field = questionProp()
    schema.org description:A sub property of object. A question.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'question'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
