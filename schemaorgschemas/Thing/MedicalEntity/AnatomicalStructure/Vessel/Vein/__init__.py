# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp
from schemaorgschemas.Thing.MedicalEntity.AnatomicalStructure import functionProp, associatedPathophysiologyProp, bodyLocationProp, relatedTherapyProp, connectedToProp, partOfSystemProp, diagramProp, relatedConditionProp, subStructureProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class VeinSchema(SchemaObject):

    """Schema Mixin for Vein
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A type of blood vessel that specifically carries blood to the heart.
    """

    def __init__(self):
        self.schema = 'Vein'


class regionDrainedProp(SchemaProperty):

    """
    SchemaField for regionDrained
    Usage: Include in SchemaObject SchemaFields as your_django_field = regionDrainedProp()  
    schema.org description:The anatomical or organ system drained by this vessel; generally refers to a specific part of an organ.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalStructure"""

    _prop_schema = 'regionDrained'
    _expected_schema = 'AnatomicalStructure'
    _enum = False
    _format_as = "ForeignKey"


class drainsToProp(SchemaProperty):

    """
    SchemaField for drainsTo
    Usage: Include in SchemaObject SchemaFields as your_django_field = drainsToProp()  
    schema.org description:The vasculature that the vein drains into.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Vessel"""

    _prop_schema = 'drainsTo'
    _expected_schema = 'Vessel'
    _enum = False
    _format_as = "ForeignKey"


class tributaryProp(SchemaProperty):

    """
    SchemaField for tributary
    Usage: Include in SchemaObject SchemaFields as your_django_field = tributaryProp()  
    schema.org description:The anatomical or organ system that the vein flows into; a larger structure that the vein connects to.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalStructure"""

    _prop_schema = 'tributary'
    _expected_schema = 'AnatomicalStructure'
    _enum = False
    _format_as = "ForeignKey"
