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


EVENTSTATUS_CHOICES = (
    ('EVENTPOSTPONED',
     'EventPostponed: The event has been postponed and no new date has been set. The event&#39;s previousStartDate should be set.'),
    ('EVENTRESCHEDULED',
     'EventRescheduled: The event has been rescheduled. The event&#39;s previousStartDate should be set to the old date and the startDate should be set to the event&#39;s new date. (If the event has been rescheduled multiple times, the previousStartDate property may be repeated).'),
    ('EVENTSCHEDULED',
     'EventScheduled: The event is taking place or has taken place on the startDate as scheduled. Use of this value is optional, as it is assumed by default.'),
    ('EVENTCANCELLED',
     'EventCancelled: The event has been cancelled. If the event has multiple startDate values, all are assumed to be cancelled. Either startDate or previousStartDate may be used to specify the event&#39;s cancelled date(s).'),
)


class eventStatusProp(SchemaEnumProperty):

    """
    Enumeration for eventStatus
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'eventStatus'
    choices = EVENTSTATUS_CHOICES
    _format_as = "enum"
    adapter = {
        'EVENTPOSTPONED': 'EventPostponed',
        'EVENTRESCHEDULED': 'EventRescheduled',
        'EVENTSCHEDULED': 'EventScheduled',
        'EVENTCANCELLED': 'EventCancelled',
    }


# schema.org version 2.0
