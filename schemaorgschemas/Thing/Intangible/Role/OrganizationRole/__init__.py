# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Role import roleNameProp, endDateProp, startDateProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OrganizationRoleSchema(SchemaObject):

    """Schema Mixin for OrganizationRole
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A subclass of Role used to describe roles within organizations.
    """

    def __init__(self):
        self.schema = 'OrganizationRole'


class numberedPositionProp(SchemaProperty):

    """
    SchemaField for numberedPosition
    Usage: Include in SchemaObject SchemaFields as your_django_field = numberedPositionProp()  
    schema.org description:A number associated with a role in an organization, for example, the number on an athlete&#39;s jersey.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'numberedPosition'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


# schema.org version 2.0
