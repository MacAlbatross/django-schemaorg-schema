# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CommunicateActionSchema(SchemaObject):

    """Schema Mixin for CommunicateAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.
    """

    def __init__(self):
        self.schema = 'CommunicateAction'


class aboutProp(SchemaProperty):

    """
    SchemaField for about
    Usage: Include in SchemaObject SchemaFields as your_django_field = aboutProp()
    schema.org description:The subject matter of the content.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'about'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


class recipientProp(SchemaProperty):

    """
    SchemaField for recipient
    Usage: Include in SchemaObject SchemaFields as your_django_field = recipientProp()
    schema.org description:A sub property of participant. The participant who is at the receiving end of the action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'recipient'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class languageProp(SchemaProperty):

    """
    SchemaField for language
    Usage: Include in SchemaObject SchemaFields as your_django_field = languageProp()
    schema.org description:A sub property of instrument. The languaged used on this action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Language"""

    _prop_schema = 'language'
    _expected_schema = 'Language'
    _enum = False
    _format_as = "ForeignKey"
