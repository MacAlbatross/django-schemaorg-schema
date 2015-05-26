# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, nameProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, descriptionProp
from schemaorgschemas.Thing.Place.LocalBusiness import currenciesAcceptedProp, openingHoursProp, paymentAcceptedProp, priceRangeProp, parentOrganizationProp
from schemaorgschemas.Thing.Place import isicV4Prop, openingHoursSpecificationProp, photoProp, hasMapProp, reviewProp, containedInProp, faxNumberProp, aggregateRatingProp, additionalPropertyProp, addressProp, telephoneProp, logoProp, geoProp, eventProp, globalLocationNumberProp
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, telephoneProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, foundingLocationProp, locationProp, employeeProp, emailProp, seeksProp, numberOfEmployeesProp, subOrganizationProp, brandProp, ownsProp, awardProp, departmentProp, dissolutionDateProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, memberOfProp, legalNameProp, vatIDProp, globalLocationNumberProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TelevisionStationSchema(SchemaObject):

    """Schema Mixin for TelevisionStation
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A television station.
    """

    def __init__(self):
        self.schema = 'TelevisionStation'


class videoFormatProp(SchemaProperty):

    """
    SchemaField for videoFormat
    Usage: Include in SchemaObject SchemaFields as your_django_field = videoFormatProp()  
    schema.org description:The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'videoFormat'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
