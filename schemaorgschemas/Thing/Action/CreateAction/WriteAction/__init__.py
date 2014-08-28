# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class WriteActionSchema(SchemaObject):

    """Schema Mixin for WriteAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of authoring written creative content.
    """

    def __init__(self):
        self.schema = 'WriteAction'


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
