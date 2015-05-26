# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PlanActionSchema(SchemaObject):

    """Schema Mixin for PlanAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of planning the execution of an event/task/action/reservation/plan to a future date.
    """

    def __init__(self):
        self.schema = 'PlanAction'


class scheduledTimeProp(SchemaProperty):

    """
    SchemaField for scheduledTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = scheduledTimeProp()  
    schema.org description:The time the object is scheduled to.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'scheduledTime'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


# schema.org version 2.0
