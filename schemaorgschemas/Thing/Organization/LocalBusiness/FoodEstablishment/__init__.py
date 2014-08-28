# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Organization.LocalBusiness import currenciesAcceptedProp, openingHoursProp, paymentAcceptedProp, branchOfProp, priceRangeProp
from schemaorgschemas.Thing.Place import isicV4Prop, mapProp, openingHoursSpecificationProp, photoProp, reviewProp, containedInProp, faxNumberProp, aggregateRatingProp, telephoneProp, addressProp, interactionCountProp, logoProp, geoProp, eventProp, globalLocationNumberProp
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, interactionCountProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, locationProp, employeeProp, emailProp, seeksProp, subOrganizationProp, brandProp, ownsProp, telephoneProp, departmentProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, legalNameProp, vatIDProp, globalLocationNumberProp

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
    schema.org description:Either Yes/No, or a URL at which reservations can be made.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'acceptsReservations'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
