# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Organization.LocalBusiness import currenciesAcceptedProp, openingHoursProp, paymentAcceptedProp, branchOfProp, priceRangeProp
from schemaorgschemas.Thing.Place import isicV4Prop, mapProp, openingHoursSpecificationProp, photoProp, reviewProp, containedInProp, faxNumberProp, aggregateRatingProp, telephoneProp, addressProp, interactionCountProp, logoProp, geoProp, eventProp, globalLocationNumberProp
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, interactionCountProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, locationProp, employeeProp, emailProp, seeksProp, subOrganizationProp, brandProp, ownsProp, telephoneProp, departmentProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, legalNameProp, vatIDProp, globalLocationNumberProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PhysicianSchema(SchemaObject):

    """Schema Mixin for Physician
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A doctor&#39;s office.
    """

    def __init__(self):
        self.schema = 'Physician'


class availableServiceProp(SchemaProperty):

    """
    SchemaField for availableService
    Usage: Include in SchemaObject SchemaFields as your_django_field = availableServiceProp()  
    schema.org description:A medical service available from this provider.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalTest"""

    _prop_schema = 'availableService'
    _expected_schema = 'MedicalTest'
    _enum = False
    _format_as = "ForeignKey"


class hospitalAffiliationProp(SchemaProperty):

    """
    SchemaField for hospitalAffiliation
    Usage: Include in SchemaObject SchemaFields as your_django_field = hospitalAffiliationProp()  
    schema.org description:A hospital with which the physician or office is affiliated.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Hospital"""

    _prop_schema = 'hospitalAffiliation'
    _expected_schema = 'Hospital'
    _enum = False
    _format_as = "ForeignKey"


class medicalSpecialtyProp(SchemaProperty):

    """
    SchemaField for medicalSpecialty
    Usage: Include in SchemaObject SchemaFields as your_django_field = medicalSpecialtyProp()  
    schema.org description:A medical specialty of the provider.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalSpecialty"""

    _prop_schema = 'medicalSpecialty'
    _expected_schema = 'MedicalSpecialty'
    _enum = False
    _format_as = "ForeignKey"
