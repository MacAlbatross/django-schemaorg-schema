# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RoleSchema(SchemaObject):

    """Schema Mixin for Role
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Represents additional information about a relationship or property. For example a Role can be used to say that a &#39;member&#39; role linking some SportsTeam to a player occurred during a particular time period. Or that a Person&#39;s &#39;actor&#39; role in a Movie was for some particular characterName. Such properties can be attached to a Role entity, which is then associated with the main entities using ordinary properties like &#39;member&#39; or &#39;actor&#39;.

      See also blog post.
    """

    def __init__(self):
        self.schema = 'Role'


class roleNameProp(SchemaProperty):

    """
    SchemaField for roleName
    Usage: Include in SchemaObject SchemaFields as your_django_field = roleNameProp()  
    schema.org description:A role played, performed or filled by a person or organization. For example, the team of creators for a comic book might fill the roles named &#39;inker&#39;, &#39;penciller&#39;, and &#39;letterer&#39;; or an athlete in a SportsTeam might play in the position named &#39;Quarterback&#39;. Supersedes namedPosition.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'roleName'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class endDateProp(SchemaProperty):

    """
    SchemaField for endDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = endDateProp()  
    schema.org description:The end date and time of the item (in ISO 8601 date format).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'endDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class startDateProp(SchemaProperty):

    """
    SchemaField for startDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = startDateProp()  
    schema.org description:The start date and time of the item (in ISO 8601 date format).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'startDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


# schema.org version 2.0
