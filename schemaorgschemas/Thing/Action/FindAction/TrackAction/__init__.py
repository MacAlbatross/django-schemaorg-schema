# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TrackActionSchema(SchemaObject):

    """Schema Mixin for TrackAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An agent tracks an object for updates.Related actions:FollowAction: Unlike FollowAction, TrackAction refers to the interest on the location of innanimates objects.SubscribeAction: Unlike SubscribeAction, TrackAction refers to  the interest on the location of innanimate objects.
    """

    def __init__(self):
        self.schema = 'TrackAction'


class deliveryMethodProp(SchemaProperty):

    """
    SchemaField for deliveryMethod
    Usage: Include in SchemaObject SchemaFields as your_django_field = deliveryMethodProp()  
    schema.org description:A sub property of instrument. The method of delivery.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DeliveryMethod"""

    _prop_schema = 'deliveryMethod'
    _expected_schema = 'DeliveryMethod'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
