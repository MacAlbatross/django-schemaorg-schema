# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ProgramMembershipSchema(SchemaObject):

    """Schema Mixin for ProgramMembership
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Used to describe membership in a loyalty programs (e.g. &quot;StarAliance&quot;), traveler clubs (e.g. &quot;AAA&quot;), purchase clubs (&quot;Safeway Club&quot;), etc.
    """

    def __init__(self):
        self.schema = 'ProgramMembership'


class hostingOrganizationProp(SchemaProperty):

    """
    SchemaField for hostingOrganization
    Usage: Include in SchemaObject SchemaFields as your_django_field = hostingOrganizationProp()  
    schema.org description:The organization (airline, travelers&#39; club, etc.) the membership is made with.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'hostingOrganization'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class memberProp(SchemaProperty):

    """
    SchemaField for member
    Usage: Include in SchemaObject SchemaFields as your_django_field = memberProp()  
    schema.org description:A member of this organization. Supercedes members.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'member'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class membershipNumberProp(SchemaProperty):

    """
    SchemaField for membershipNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = membershipNumberProp()  
    schema.org description:A unique identifier for the membership.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'membershipNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class programNameProp(SchemaProperty):

    """
    SchemaField for programName
    Usage: Include in SchemaObject SchemaFields as your_django_field = programNameProp()  
    schema.org description:The program providing the membership.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'programName'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
