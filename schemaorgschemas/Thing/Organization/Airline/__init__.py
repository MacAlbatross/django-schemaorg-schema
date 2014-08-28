# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, interactionCountProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, locationProp, employeeProp, emailProp, seeksProp, subOrganizationProp, brandProp, ownsProp, telephoneProp, departmentProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, legalNameProp, vatIDProp, globalLocationNumberProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AirlineSchema(SchemaObject):

    """Schema Mixin for Airline
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An organization that provides flights for passengers.
    """

    def __init__(self):
        self.schema = 'Airline'


class iataCodeProp(SchemaProperty):

    """
    SchemaField for iataCode
    Usage: Include in SchemaObject SchemaFields as your_django_field = iataCodeProp()  
    schema.org description:IATA identifier for an airline or airport

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'iataCode'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
