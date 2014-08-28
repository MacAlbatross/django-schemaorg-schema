# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SearchActionSchema(SchemaObject):

    """Schema Mixin for SearchAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of searching for an object.Related actions:FindAction: SearchAction generally leads to a FindAction, but not necessarily.
    """

    def __init__(self):
        self.schema = 'SearchAction'


class queryProp(SchemaProperty):

    """
    SchemaField for query
    Usage: Include in SchemaObject SchemaFields as your_django_field = queryProp()  
    schema.org description:A sub property of instrument. The query used on this action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'query'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
