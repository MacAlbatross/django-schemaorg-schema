# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Place.CivicStructure import openingHoursProp
from schemaorgschemas.Thing.Place import isicV4Prop, openingHoursSpecificationProp, photoProp, reviewProp, telephoneProp, containedInProp, hasMapProp, aggregateRatingProp, additionalPropertyProp, addressProp, logoProp, faxNumberProp, geoProp, eventProp, globalLocationNumberProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AirportSchema(SchemaObject):

    """Schema Mixin for Airport
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An airport.
    """

    def __init__(self):
        self.schema = 'Airport'


class icaoCodeProp(SchemaProperty):

    """
    SchemaField for icaoCode
    Usage: Include in SchemaObject SchemaFields as your_django_field = icaoCodeProp()  
    schema.org description:IACO identifier for an airport.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'icaoCode'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class iataCodeProp(SchemaProperty):

    """
    SchemaField for iataCode
    Usage: Include in SchemaObject SchemaFields as your_django_field = iataCodeProp()  
    schema.org description:IATA identifier for an airline or airport.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'iataCode'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
