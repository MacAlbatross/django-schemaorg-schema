# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FollowActionSchema(SchemaObject):

    """Schema Mixin for FollowAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically to get updates polled from.Related actions:BefriendAction: Unlike BefriendAction, FollowAction implies that the connection is *not* necessarily reciprocal.SubscribeAction: Unlike SubscribeAction, FollowAction implies that the follower acts as an active agent constantly/actively polling for updates.RegisterAction: Unlike RegisterAction, FollowAction implies that the agent is interested in continuing receiving updates from the object.JoinAction: Unlike JoinAction, FollowAction implies that the agent is interested in getting updates from the object.TrackAction: Unlike TrackAction, FollowAction refers to the polling of updates of all aspects of animate objects rather than the location of inanimate objects (e.g. you track a package, but you don&#39;t follow it).
    """

    def __init__(self):
        self.schema = 'FollowAction'


class followeeProp(SchemaProperty):

    """
    SchemaField for followee
    Usage: Include in SchemaObject SchemaFields as your_django_field = followeeProp()
    schema.org description:A sub property of object. The person or organization being followed.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'followee'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"
