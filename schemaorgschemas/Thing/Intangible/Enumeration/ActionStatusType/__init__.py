# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ActionStatusTypeSchema(SchemaObject):

    """Schema Mixin for ActionStatusType
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The status of an Action.
    """

    def __init__(self):
        self.schema = 'ActionStatusType'


ACTIONSTATUS_CHOICES = (
    ('COMPLETEDACTIONSTATUS',
     'CompletedActionStatus: An action that has already taken place.'),
    ('FAILEDACTIONSTATUS',
     'FailedActionStatus: An action that failed to complete. The action&#39;s error property and the HTTP return code contain more information about the failure.'),
    ('POTENTIALACTIONSTATUS',
     'PotentialActionStatus: A description of an action that is supported.'),
    ('ACTIVEACTIONSTATUS',
     'ActiveActionStatus: An in-progress action (e.g, while watching the movie, or driving to a location).'),
)


class actionStatusProp(SchemaEnumProperty):

    """
    Enumeration for actionStatus
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'actionStatus'
    choices = ACTIONSTATUS_CHOICES
    _format_as = "enum"
    adapter = {
        'COMPLETEDACTIONSTATUS': 'CompletedActionStatus',
        'FAILEDACTIONSTATUS': 'FailedActionStatus',
        'POTENTIALACTIONSTATUS': 'PotentialActionStatus',
        'ACTIVEACTIONSTATUS': 'ActiveActionStatus',
    }


# schema.org version 2.0
