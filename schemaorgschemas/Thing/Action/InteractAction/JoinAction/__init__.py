# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, nameProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, descriptionProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class JoinActionSchema(SchemaObject):

    """Schema Mixin for JoinAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An agent joins an event/group with participants/friends at a location.Related actions:RegisterAction: Unlike RegisterAction, JoinAction refers to joining a group/team of people.SubscribeAction: Unlike SubscribeAction, JoinAction does not imply that you&#39;ll be receiving updates.FollowAction: Unlike FollowAction, JoinAction does not imply that you&#39;ll be polling for updates.
    """

    def __init__(self):
        self.schema = 'JoinAction'


class eventProp(SchemaProperty):

    """
    SchemaField for event
    Usage: Include in SchemaObject SchemaFields as your_django_field = eventProp()  
    schema.org description:Upcoming or past event associated with this place, organization, or action. Supersedes events.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Event"""

    _prop_schema = 'event'
    _expected_schema = 'Event'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
