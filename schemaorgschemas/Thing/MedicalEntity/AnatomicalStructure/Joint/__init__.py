# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp
from schemaorgschemas.Thing.MedicalEntity.AnatomicalStructure import functionProp, associatedPathophysiologyProp, bodyLocationProp, relatedTherapyProp, connectedToProp, partOfSystemProp, diagramProp, relatedConditionProp, subStructureProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class JointSchema(SchemaObject):

    """Schema Mixin for Joint
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The anatomical location at which two or more bones make contact.
    """

    def __init__(self):
        self.schema = 'Joint'


class functionalClassProp(SchemaProperty):

    """
    SchemaField for functionalClass
    Usage: Include in SchemaObject SchemaFields as your_django_field = functionalClassProp()  
    schema.org description:The degree of mobility the joint allows.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'functionalClass'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class structuralClassProp(SchemaProperty):

    """
    SchemaField for structuralClass
    Usage: Include in SchemaObject SchemaFields as your_django_field = structuralClassProp()  
    schema.org description:The name given to how bone physically connects to each other.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'structuralClass'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class biomechnicalClassProp(SchemaProperty):

    """
    SchemaField for biomechnicalClass
    Usage: Include in SchemaObject SchemaFields as your_django_field = biomechnicalClassProp()  
    schema.org description:The biomechanical properties of the bone.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'biomechnicalClass'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
