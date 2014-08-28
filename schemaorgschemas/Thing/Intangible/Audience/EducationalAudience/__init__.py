# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Audience import geographicAreaProp, audienceTypeProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EducationalAudienceSchema(SchemaObject):

    """Schema Mixin for EducationalAudience
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An EducationalAudience
    """

    def __init__(self):
        self.schema = 'EducationalAudience'


class educationalRoleProp(SchemaProperty):

    """
    SchemaField for educationalRole
    Usage: Include in SchemaObject SchemaFields as your_django_field = educationalRoleProp()  
    schema.org description:An educationalRole of an EducationalAudience

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'educationalRole'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
