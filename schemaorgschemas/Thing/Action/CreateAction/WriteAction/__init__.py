# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class WriteActionSchema(SchemaObject):

    """Schema Mixin for WriteAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of authoring written creative content.
    """

    def __init__(self):
        self.schema = 'WriteAction'


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


# schema.org version 2.0
