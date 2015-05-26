# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, telephoneProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, foundingLocationProp, locationProp, employeeProp, emailProp, seeksProp, numberOfEmployeesProp, subOrganizationProp, brandProp, ownsProp, awardProp, departmentProp, dissolutionDateProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, memberOfProp, legalNameProp, vatIDProp, globalLocationNumberProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SportsOrganizationSchema(SchemaObject):

    """Schema Mixin for SportsOrganization
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Represents the collection of all sports organizations, including sports teams, governing bodies, and sports associations.
    """

    def __init__(self):
        self.schema = 'SportsOrganization'


class sportProp(SchemaProperty):

    """
    SchemaField for sport
    Usage: Include in SchemaObject SchemaFields as your_django_field = sportProp()  
    schema.org description:A type of sport (e.g. Baseball).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'sport'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
