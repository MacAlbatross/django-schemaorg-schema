# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Event import inLanguageProp, attendeeProp, performerProp, endDateProp, startDateProp, previousStartDateProp, superEventProp, reviewProp, recordedInProp, aggregateRatingProp, subEventProp, offersProp, eventStatusProp, typicalAgeRangeProp, durationProp, workPerformedProp, organizerProp, doorTimeProp, locationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class UserCommentsSchema(SchemaObject):

    """Schema Mixin for UserComments
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use
          Action-based vocabulary, alongside types such as Comment.

    """

    def __init__(self):
        self.schema = 'UserComments'


class discussesProp(SchemaProperty):

    """
    SchemaField for discusses
    Usage: Include in SchemaObject SchemaFields as your_django_field = discussesProp()  
    schema.org description:Specifies the CreativeWork associated with the UserComment.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference CreativeWork"""

    _prop_schema = 'discusses'
    _expected_schema = 'CreativeWork'
    _enum = False
    _format_as = "ForeignKey"


class commentTextProp(SchemaProperty):

    """
    SchemaField for commentText
    Usage: Include in SchemaObject SchemaFields as your_django_field = commentTextProp()  
    schema.org description:The text of the UserComment.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'commentText'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class creatorProp(SchemaProperty):

    """
    SchemaField for creator
    Usage: Include in SchemaObject SchemaFields as your_django_field = creatorProp()  
    schema.org description:The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'creator'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class replyToUrlProp(SchemaProperty):

    """
    SchemaField for replyToUrl
    Usage: Include in SchemaObject SchemaFields as your_django_field = replyToUrlProp()  
    schema.org description:The URL at which a reply may be posted to the specified UserComment.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference URL"""

    _prop_schema = 'replyToUrl'
    _expected_schema = 'URL'
    _enum = False
    _format_as = "ForeignKey"


class commentTimeProp(SchemaProperty):

    """
    SchemaField for commentTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = commentTimeProp()  
    schema.org description:The time at which the UserComment was made.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'commentTime'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


# schema.org version 2.0
