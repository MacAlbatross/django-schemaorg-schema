# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DrugLegalStatusSchema(SchemaObject):

    """Schema Mixin for DrugLegalStatus
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The legal availability status of a medical drug.
    """

    def __init__(self):
        self.schema = 'DrugLegalStatus'


class applicableLocationProp(SchemaProperty):

    """
    SchemaField for applicableLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = applicableLocationProp()
    schema.org description:The location in which the status applies.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AdministrativeArea"""

    _prop_schema = 'applicableLocation'
    _expected_schema = 'AdministrativeArea'
    _enum = False
    _format_as = "ForeignKey"
