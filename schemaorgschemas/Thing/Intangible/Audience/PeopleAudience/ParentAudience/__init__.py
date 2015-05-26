# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Audience import geographicAreaProp, audienceTypeProp
from schemaorgschemas.Thing.Intangible.Audience.PeopleAudience import suggestedMinAgeProp, requiredMinAgeProp, suggestedGenderProp, healthConditionProp, requiredMaxAgeProp, suggestedMaxAgeProp, requiredGenderProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ParentAudienceSchema(SchemaObject):

    """Schema Mixin for ParentAudience
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A set of characteristics describing parents, who can be interested in viewing some content.
    """

    def __init__(self):
        self.schema = 'ParentAudience'


class childMaxAgeProp(SchemaProperty):

    """
    SchemaField for childMaxAge
    Usage: Include in SchemaObject SchemaFields as your_django_field = childMaxAgeProp()  
    schema.org description:Maximal age of the child.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'childMaxAge'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class childMinAgeProp(SchemaProperty):

    """
    SchemaField for childMinAge
    Usage: Include in SchemaObject SchemaFields as your_django_field = childMinAgeProp()  
    schema.org description:Minimal age of the child.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'childMinAge'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


# schema.org version 2.0
