# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Event import startDateProp, attendeeProp, performerProp, endDateProp, inLanguageProp, previousStartDateProp, superEventProp, reviewProp, recordedInProp, aggregateRatingProp, subEventProp, offersProp, eventStatusProp, typicalAgeRangeProp, durationProp, workPerformedProp, organizerProp, doorTimeProp, locationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DeliveryEventSchema(SchemaObject):

    """Schema Mixin for DeliveryEvent
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An event involving the delivery of an item.
    """

    def __init__(self):
        self.schema = 'DeliveryEvent'


class availableFromProp(SchemaProperty):

    """
    SchemaField for availableFrom
    Usage: Include in SchemaObject SchemaFields as your_django_field = availableFromProp()  
    schema.org description:When the item is available for pickup from the store, locker, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'availableFrom'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class availableThroughProp(SchemaProperty):

    """
    SchemaField for availableThrough
    Usage: Include in SchemaObject SchemaFields as your_django_field = availableThroughProp()  
    schema.org description:After this date, the item will no longer be available for pickup.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'availableThrough'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class hasDeliveryMethodProp(SchemaProperty):

    """
    SchemaField for hasDeliveryMethod
    Usage: Include in SchemaObject SchemaFields as your_django_field = hasDeliveryMethodProp()  
    schema.org description:Method used for delivery or shipping.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DeliveryMethod"""

    _prop_schema = 'hasDeliveryMethod'
    _expected_schema = 'DeliveryMethod'
    _enum = False
    _format_as = "ForeignKey"


class accessCodeProp(SchemaProperty):

    """
    SchemaField for accessCode
    Usage: Include in SchemaObject SchemaFields as your_django_field = accessCodeProp()  
    schema.org description:Password, PIN, or access code needed for delivery (e.g. from a locker).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'accessCode'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
