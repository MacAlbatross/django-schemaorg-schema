# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Event import inLanguageProp, attendeeProp, performerProp, workPerformedProp, startDateProp, previousStartDateProp, superEventProp, reviewProp, recordedInProp, aggregateRatingProp, subEventProp, offersProp, eventStatusProp, typicalAgeRangeProp, durationProp, endDateProp, organizerProp, doorTimeProp, locationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class UserDownloadsSchema(SchemaObject):

    """Schema Mixin for UserDownloads
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use
          Action-based vocabulary, alongside types such as Comment.

    """

    def __init__(self):
        self.schema = 'UserDownloads'


# schema.org version 2.0
