# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TrainTripSchema(SchemaObject):

    """Schema Mixin for TrainTrip
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A trip on a commercial train line.
    """

    def __init__(self):
        self.schema = 'TrainTrip'


class departureStationProp(SchemaProperty):

    """
    SchemaField for departureStation
    Usage: Include in SchemaObject SchemaFields as your_django_field = departureStationProp()  
    schema.org description:The station from which the train departs.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference TrainStation"""

    _prop_schema = 'departureStation'
    _expected_schema = 'TrainStation'
    _enum = False
    _format_as = "ForeignKey"


class departureTimeProp(SchemaProperty):

    """
    SchemaField for departureTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = departureTimeProp()  
    schema.org description:The expected departure time.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'departureTime'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class departurePlatformProp(SchemaProperty):

    """
    SchemaField for departurePlatform
    Usage: Include in SchemaObject SchemaFields as your_django_field = departurePlatformProp()  
    schema.org description:The platform from which the train departs.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'departurePlatform'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class arrivalTimeProp(SchemaProperty):

    """
    SchemaField for arrivalTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = arrivalTimeProp()  
    schema.org description:The expected arrival time.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'arrivalTime'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class arrivalPlatformProp(SchemaProperty):

    """
    SchemaField for arrivalPlatform
    Usage: Include in SchemaObject SchemaFields as your_django_field = arrivalPlatformProp()  
    schema.org description:The platform where the train arrives.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'arrivalPlatform'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class trainNameProp(SchemaProperty):

    """
    SchemaField for trainName
    Usage: Include in SchemaObject SchemaFields as your_django_field = trainNameProp()  
    schema.org description:The name of the train (e.g. The Orient Express).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'trainName'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class providerProp(SchemaProperty):

    """
    SchemaField for provider
    Usage: Include in SchemaObject SchemaFields as your_django_field = providerProp()  
    schema.org description:The organization or agency that is providing the service.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'provider'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class trainNumberProp(SchemaProperty):

    """
    SchemaField for trainNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = trainNumberProp()  
    schema.org description:The unique identifier for the train.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'trainNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class arrivalStationProp(SchemaProperty):

    """
    SchemaField for arrivalStation
    Usage: Include in SchemaObject SchemaFields as your_django_field = arrivalStationProp()  
    schema.org description:The station where the train trip ends.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference TrainStation"""

    _prop_schema = 'arrivalStation'
    _expected_schema = 'TrainStation'
    _enum = False
    _format_as = "ForeignKey"
