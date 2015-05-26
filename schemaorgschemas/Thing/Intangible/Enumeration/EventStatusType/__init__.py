# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EventStatusTypeSchema(SchemaObject):

    """Schema Mixin for EventStatusType
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    EventStatusType is an enumeration type whose instances represent several states that an Event may be in.
    """

    def __init__(self):
        self.schema = 'EventStatusType'


/EVENTSTATUS_CHOICES = (
    ('/EVENTPOSTPONED', '/EventPostponed'),
    ('/EVENTRESCHEDULED', '/EventRescheduled'),
    ('/EVENTSCHEDULED', '/EventScheduled'),
    ('/EVENTCANCELLED', '/EventCancelled'),
)


class / eventStatusProp(SchemaEnumProperty):

    """
    Enumeration for /eventStatus
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/eventStatus'
    choices = /EVENTSTATUS_CHOICES
    _format_as = "enum"
    adapter = {
        '/EVENTPOSTPONED': '/EventPostponed',
        '/EVENTRESCHEDULED': '/EventRescheduled',
        '/EVENTSCHEDULED': '/EventScheduled',
        '/EVENTCANCELLED': '/EventCancelled',
    }


# schema.org version 2.0
