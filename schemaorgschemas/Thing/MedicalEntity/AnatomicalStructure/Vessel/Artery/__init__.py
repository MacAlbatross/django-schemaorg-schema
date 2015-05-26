# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.MedicalEntity.AnatomicalStructure import functionProp, associatedPathophysiologyProp, bodyLocationProp, relatedTherapyProp, connectedToProp, partOfSystemProp, diagramProp, relatedConditionProp, subStructureProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ArterySchema(SchemaObject):

    """Schema Mixin for Artery
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A type of blood vessel that specifically carries blood away from the heart.
    """

    def __init__(self):
        self.schema = 'Artery'


class sourceProp(SchemaProperty):

    """
    SchemaField for source
    Usage: Include in SchemaObject SchemaFields as your_django_field = sourceProp()  
    schema.org description:The anatomical or organ system that the artery originates from.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalStructure"""

    _prop_schema = 'source'
    _expected_schema = 'AnatomicalStructure'
    _enum = False
    _format_as = "ForeignKey"


class supplyToProp(SchemaProperty):

    """
    SchemaField for supplyTo
    Usage: Include in SchemaObject SchemaFields as your_django_field = supplyToProp()  
    schema.org description:The area to which the artery supplies blood.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalStructure"""

    _prop_schema = 'supplyTo'
    _expected_schema = 'AnatomicalStructure'
    _enum = False
    _format_as = "ForeignKey"


class arterialBranchProp(SchemaProperty):

    """
    SchemaField for arterialBranch
    Usage: Include in SchemaObject SchemaFields as your_django_field = arterialBranchProp()  
    schema.org description:The branches that comprise the arterial structure.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalStructure"""

    _prop_schema = 'arterialBranch'
    _expected_schema = 'AnatomicalStructure'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
