# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DayOfWeekSchema(SchemaObject):

    """Schema Mixin for DayOfWeek
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The day of the week, e.g. used to specify to which day the opening hours of an OpeningHoursSpecification refer.

    Commonly used values:

    http://purl.org/goodrelations/v1#Monday 
    http://purl.org/goodrelations/v1#Tuesday 
    http://purl.org/goodrelations/v1#Wednesday 
    http://purl.org/goodrelations/v1#Thursday 
    http://purl.org/goodrelations/v1#Friday 
    http://purl.org/goodrelations/v1#Saturday 
    http://purl.org/goodrelations/v1#Sunday 
    http://purl.org/goodrelations/v1#PublicHolidays 

    """

    def __init__(self):
        self.schema = 'DayOfWeek'


# schema.org version 2.0
