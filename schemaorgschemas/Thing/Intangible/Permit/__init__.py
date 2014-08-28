# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PermitSchema(SchemaObject):

    """Schema Mixin for Permit
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A permit issued by an organization, e.g. a parking pass.
    """

    def __init__(self):
        self.schema = 'Permit'


class validForProp(SchemaProperty):

    """
    SchemaField for validFor
    Usage: Include in SchemaObject SchemaFields as your_django_field = validForProp()
    schema.org description:The time validity of the permit.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Duration"""

    _prop_schema = 'validFor'
    _expected_schema = 'Duration'
    _enum = False
    _format_as = "TimeField"


class validUntilProp(SchemaProperty):

    """
    SchemaField for validUntil
    Usage: Include in SchemaObject SchemaFields as your_django_field = validUntilProp()
    schema.org description:The date when the item is no longer valid.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Date"""

    _prop_schema = 'validUntil'
    _expected_schema = 'Date'
    _enum = False
    _format_as = "ForeignKey"


class permitAudienceProp(SchemaProperty):

    """
    SchemaField for permitAudience
    Usage: Include in SchemaObject SchemaFields as your_django_field = permitAudienceProp()
    schema.org description:The target audience for this permit.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Audience"""

    _prop_schema = 'permitAudience'
    _expected_schema = 'Audience'
    _enum = False
    _format_as = "ForeignKey"


class validInProp(SchemaProperty):

    """
    SchemaField for validIn
    Usage: Include in SchemaObject SchemaFields as your_django_field = validInProp()
    schema.org description:The geographic area where the permit is valid.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AdministrativeArea"""

    _prop_schema = 'validIn'
    _expected_schema = 'AdministrativeArea'
    _enum = False
    _format_as = "ForeignKey"


class issuedThroughProp(SchemaProperty):

    """
    SchemaField for issuedThrough
    Usage: Include in SchemaObject SchemaFields as your_django_field = issuedThroughProp()
    schema.org description:The service through with the permit was granted.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Service"""

    _prop_schema = 'issuedThrough'
    _expected_schema = 'Service'
    _enum = False
    _format_as = "ForeignKey"


class issuedByProp(SchemaProperty):

    """
    SchemaField for issuedBy
    Usage: Include in SchemaObject SchemaFields as your_django_field = issuedByProp()
    schema.org description:The organization issuing the permit.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'issuedBy'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class validFromProp(SchemaProperty):

    """
    SchemaField for validFrom
    Usage: Include in SchemaObject SchemaFields as your_django_field = validFromProp()
    schema.org description:The date when the item becomes valid.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'validFrom'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"
