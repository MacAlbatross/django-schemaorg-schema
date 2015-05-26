# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, telephoneProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, foundingLocationProp, locationProp, employeeProp, emailProp, seeksProp, numberOfEmployeesProp, subOrganizationProp, brandProp, ownsProp, awardProp, departmentProp, dissolutionDateProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, memberOfProp, legalNameProp, vatIDProp, globalLocationNumberProp
from schemaorgschemas.Thing.Place.LocalBusiness import currenciesAcceptedProp, openingHoursProp, paymentAcceptedProp, priceRangeProp, parentOrganizationProp
from schemaorgschemas.Thing.Place import isicV4Prop, openingHoursSpecificationProp, photoProp, hasMapProp, reviewProp, containedInProp, faxNumberProp, aggregateRatingProp, additionalPropertyProp, addressProp, telephoneProp, logoProp, geoProp, eventProp, globalLocationNumberProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FoodEstablishmentSchema(SchemaObject):

    """Schema Mixin for FoodEstablishment
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A food-related business.
    """

    def __init__(self):
        self.schema = 'FoodEstablishment'


class menuProp(SchemaProperty):

    """
    SchemaField for menu
    Usage: Include in SchemaObject SchemaFields as your_django_field = menuProp()  
    schema.org description:Either the actual menu or a URL of the menu.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'menu'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class servesCuisineProp(SchemaProperty):

    """
    SchemaField for servesCuisine
    Usage: Include in SchemaObject SchemaFields as your_django_field = servesCuisineProp()  
    schema.org description:The cuisine of the restaurant.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'servesCuisine'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class acceptsReservationsProp(SchemaProperty):

    """
    SchemaField for acceptsReservations
    Usage: Include in SchemaObject SchemaFields as your_django_field = acceptsReservationsProp()  
    schema.org description:Indicates whether a FoodEstablishment accepts reservations. Values can be Boolean, an URL at which reservations can be made or (for backwards compatibility) the strings Yes or No.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Boolean"""

    _prop_schema = 'acceptsReservations'
    _expected_schema = 'Boolean'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
