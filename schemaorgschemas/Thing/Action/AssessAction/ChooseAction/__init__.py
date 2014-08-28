# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ChooseActionSchema(SchemaObject):

    """Schema Mixin for ChooseAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of expressing a preference from a set of options or a large or unbounded set of choices/options.
    """

    def __init__(self):
        self.schema = 'ChooseAction'


class optionProp(SchemaProperty):

    """
    SchemaField for option
    Usage: Include in SchemaObject SchemaFields as your_django_field = optionProp()
    schema.org description:A sub property of object. The options subject to this action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'option'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
