# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BusTripSchema(SchemaObject):

    """Schema Mixin for BusTrip
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A trip on a commercial bus line.
    """

    def __init__(self):
        self.schema = 'BusTrip'


class busNumberProp(SchemaProperty):

    """
    SchemaField for busNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = busNumberProp()  
    schema.org description:The unique identifier for the bus.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'busNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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


class departureBusStopProp(SchemaProperty):

    """
    SchemaField for departureBusStop
    Usage: Include in SchemaObject SchemaFields as your_django_field = departureBusStopProp()  
    schema.org description:The stop or station from which the bus departs.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference BusStation"""

    _prop_schema = 'departureBusStop'
    _expected_schema = 'BusStation'
    _enum = False
    _format_as = "ForeignKey"


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


class busNameProp(SchemaProperty):

    """
    SchemaField for busName
    Usage: Include in SchemaObject SchemaFields as your_django_field = busNameProp()  
    schema.org description:The name of the bus (e.g. Bolt Express).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'busName'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class providerProp(SchemaProperty):

    """
    SchemaField for provider
    Usage: Include in SchemaObject SchemaFields as your_django_field = providerProp()  
    schema.org description:The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller. Supersedes carrier.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'provider'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class arrivalBusStopProp(SchemaProperty):

    """
    SchemaField for arrivalBusStop
    Usage: Include in SchemaObject SchemaFields as your_django_field = arrivalBusStopProp()  
    schema.org description:The stop or station from which the bus arrives.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference BusStation"""

    _prop_schema = 'arrivalBusStop'
    _expected_schema = 'BusStation'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
