# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.UpdateAction import collectionProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ReplaceActionSchema(SchemaObject):

    """Schema Mixin for ReplaceAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of editing a recipient by replacing an old object with a new object.
    """

    def __init__(self):
        self.schema = 'ReplaceAction'


class replacerProp(SchemaProperty):

    """
    SchemaField for replacer
    Usage: Include in SchemaObject SchemaFields as your_django_field = replacerProp()
    schema.org description:A sub property of object. The object that replaces.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'replacer'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


class replaceeProp(SchemaProperty):

    """
    SchemaField for replacee
    Usage: Include in SchemaObject SchemaFields as your_django_field = replaceeProp()
    schema.org description:A sub property of object. The object that is being replaced.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'replacee'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"
