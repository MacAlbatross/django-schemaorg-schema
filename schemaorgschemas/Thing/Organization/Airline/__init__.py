# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, telephoneProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, foundingLocationProp, locationProp, employeeProp, emailProp, seeksProp, numberOfEmployeesProp, subOrganizationProp, brandProp, ownsProp, awardProp, departmentProp, dissolutionDateProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, memberOfProp, legalNameProp, vatIDProp, globalLocationNumberProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AirlineSchema(SchemaObject):

    """Schema Mixin for Airline
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An organization that provides flights for passengers.
    """

    def __init__(self):
        self.schema = 'Airline'


class boardingPolicyProp(SchemaProperty):

    """
    SchemaField for boardingPolicy
    Usage: Include in SchemaObject SchemaFields as your_django_field = boardingPolicyProp()  
    schema.org description:The type of boarding policy used by the airline (e.g. zone-based or group-based).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference BoardingPolicyType"""

    _prop_schema = 'boardingPolicy'
    _expected_schema = 'BoardingPolicyType'
    _enum = False
    _format_as = "ForeignKey"


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
