# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EndorseActionSchema(SchemaObject):

    """Schema Mixin for EndorseAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An agent approves/certifies/likes/supports/sanction an object.
    """

    def __init__(self):
        self.schema = 'EndorseAction'


class endorseeProp(SchemaProperty):

    """
    SchemaField for endorsee
    Usage: Include in SchemaObject SchemaFields as your_django_field = endorseeProp()
    schema.org description:A sub property of participant. The person/organization being supported.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'endorsee'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"
