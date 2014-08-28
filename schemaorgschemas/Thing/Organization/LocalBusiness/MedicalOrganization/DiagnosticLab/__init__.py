# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Organization.LocalBusiness import currenciesAcceptedProp, openingHoursProp, paymentAcceptedProp, branchOfProp, priceRangeProp
from schemaorgschemas.Thing.Place import isicV4Prop, mapProp, openingHoursSpecificationProp, photoProp, reviewProp, containedInProp, faxNumberProp, aggregateRatingProp, telephoneProp, addressProp, interactionCountProp, logoProp, geoProp, eventProp, globalLocationNumberProp
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, interactionCountProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, locationProp, employeeProp, emailProp, seeksProp, subOrganizationProp, brandProp, ownsProp, telephoneProp, departmentProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, legalNameProp, vatIDProp, globalLocationNumberProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DiagnosticLabSchema(SchemaObject):

    """Schema Mixin for DiagnosticLab
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A medical laboratory that offers on-site or off-site diagnostic services.
    """

    def __init__(self):
        self.schema = 'DiagnosticLab'


class availableTestProp(SchemaProperty):

    """
    SchemaField for availableTest
    Usage: Include in SchemaObject SchemaFields as your_django_field = availableTestProp()  
    schema.org description:A diagnostic test or procedure offered by this lab.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalTest"""

    _prop_schema = 'availableTest'
    _expected_schema = 'MedicalTest'
    _enum = False
    _format_as = "ForeignKey"
