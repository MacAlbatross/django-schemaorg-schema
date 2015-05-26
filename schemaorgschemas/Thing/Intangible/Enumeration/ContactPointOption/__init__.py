# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ContactPointOptionSchema(SchemaObject):

    """Schema Mixin for ContactPointOption
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Enumerated options related to a ContactPoint.
    """

    def __init__(self):
        self.schema = 'ContactPointOption'


CONTACTOPTION_CHOICES = (
    ('TOLLFREE', 'TollFree: The associated telephone number is toll free.'),
    ('HEARINGIMPAIREDSUPPORTED',
     'HearingImpairedSupported: Uses devices to support users with hearing impairments.'),
)


class contactOptionProp(SchemaEnumProperty):

    """
    Enumeration for contactOption
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'contactOption'
    choices = CONTACTOPTION_CHOICES
    _format_as = "enum"
    adapter = {
        'TOLLFREE': 'TollFree',
        'HEARINGIMPAIREDSUPPORTED': 'HearingImpairedSupported',
    }


# schema.org version 2.0
