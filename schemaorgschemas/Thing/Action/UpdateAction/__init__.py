# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class UpdateActionSchema(SchemaObject):

    """Schema Mixin for UpdateAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of managing by changing/editing the state of the object.
    """

    def __init__(self):
        self.schema = 'UpdateAction'


class targetCollectionProp(SchemaProperty):

    """
    SchemaField for targetCollection
    Usage: Include in SchemaObject SchemaFields as your_django_field = targetCollectionProp()  
    schema.org description:A sub property of object. The collection target of the action. Supersedes collection.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'targetCollection'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
