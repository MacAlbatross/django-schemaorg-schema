# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Audience import geographicAreaProp, audienceTypeProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PeopleAudienceSchema(SchemaObject):

    """Schema Mixin for PeopleAudience
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A set of characteristics belonging to people, e.g. who compose an item&#39;s target audience.
    """

    def __init__(self):
        self.schema = 'PeopleAudience'


class requiredMaxAgeProp(SchemaProperty):

    """
    SchemaField for requiredMaxAge
    Usage: Include in SchemaObject SchemaFields as your_django_field = requiredMaxAgeProp()  
    schema.org description:Audiences defined by a person&#39;s maximum age.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Integer"""

    _prop_schema = 'requiredMaxAge'
    _expected_schema = 'Integer'
    _enum = False
    _format_as = "ForeignKey"


class suggestedMinAgeProp(SchemaProperty):

    """
    SchemaField for suggestedMinAge
    Usage: Include in SchemaObject SchemaFields as your_django_field = suggestedMinAgeProp()  
    schema.org description:Minimal age recommended for viewing content.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'suggestedMinAge'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class suggestedMaxAgeProp(SchemaProperty):

    """
    SchemaField for suggestedMaxAge
    Usage: Include in SchemaObject SchemaFields as your_django_field = suggestedMaxAgeProp()  
    schema.org description:Maximal age recommended for viewing content.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'suggestedMaxAge'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class requiredMinAgeProp(SchemaProperty):

    """
    SchemaField for requiredMinAge
    Usage: Include in SchemaObject SchemaFields as your_django_field = requiredMinAgeProp()  
    schema.org description:Audiences defined by a person&#39;s minimum age.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Integer"""

    _prop_schema = 'requiredMinAge'
    _expected_schema = 'Integer'
    _enum = False
    _format_as = "ForeignKey"


class suggestedGenderProp(SchemaProperty):

    """
    SchemaField for suggestedGender
    Usage: Include in SchemaObject SchemaFields as your_django_field = suggestedGenderProp()  
    schema.org description:The gender of the person or audience.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'suggestedGender'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class requiredGenderProp(SchemaProperty):

    """
    SchemaField for requiredGender
    Usage: Include in SchemaObject SchemaFields as your_django_field = requiredGenderProp()  
    schema.org description:Audiences defined by a person&#39;s gender.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'requiredGender'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class healthConditionProp(SchemaProperty):

    """
    SchemaField for healthCondition
    Usage: Include in SchemaObject SchemaFields as your_django_field = healthConditionProp()  
    schema.org description:Expectations for health conditions of target audience.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalCondition"""

    _prop_schema = 'healthCondition'
    _expected_schema = 'MedicalCondition'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
