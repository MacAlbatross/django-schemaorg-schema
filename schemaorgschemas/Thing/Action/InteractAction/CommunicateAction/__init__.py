# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CommunicateActionSchema(SchemaObject):

    """Schema Mixin for CommunicateAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.
    """

    def __init__(self):
        self.schema = 'CommunicateAction'


class inLanguageProp(SchemaProperty):

    """
    SchemaField for inLanguage
    Usage: Include in SchemaObject SchemaFields as your_django_field = inLanguageProp()  
    schema.org description:The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. Supersedes language.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'inLanguage'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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
    used to reference Person"""

    _prop_schema = 'recipient'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
