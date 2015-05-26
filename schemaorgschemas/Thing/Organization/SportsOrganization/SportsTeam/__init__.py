# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, telephoneProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, foundingLocationProp, locationProp, employeeProp, emailProp, seeksProp, numberOfEmployeesProp, subOrganizationProp, brandProp, ownsProp, awardProp, departmentProp, dissolutionDateProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, memberOfProp, legalNameProp, vatIDProp, globalLocationNumberProp
from schemaorgschemas.Thing.Organization.SportsOrganization import sportProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SportsTeamSchema(SchemaObject):

    """Schema Mixin for SportsTeam
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Organization: Sports team.
    """

    def __init__(self):
        self.schema = 'SportsTeam'


class athleteProp(SchemaProperty):

    """
    SchemaField for athlete
    Usage: Include in SchemaObject SchemaFields as your_django_field = athleteProp()  
    schema.org description:A person that acts as performing member of a sports team; a player as opposed to a coach.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'athlete'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class coachProp(SchemaProperty):

    """
    SchemaField for coach
    Usage: Include in SchemaObject SchemaFields as your_django_field = coachProp()  
    schema.org description:A person that acts in a coaching role for a sports team.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'coach'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
