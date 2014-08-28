# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AnatomicalSystemSchema(SchemaObject):

    """Schema Mixin for AnatomicalSystem
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An anatomical system is a group of anatomical structures that work together to perform a certain task. Anatomical systems, such as organ systems, are one organizing principle of anatomy, and can includes circulatory, digestive, endocrine, integumentary, immune, lymphatic, muscular, nervous, reproductive, respiratory, skeletal, urinary, vestibular, and other systems.
    """

    def __init__(self):
        self.schema = 'AnatomicalSystem'


class relatedStructureProp(SchemaProperty):

    """
    SchemaField for relatedStructure
    Usage: Include in SchemaObject SchemaFields as your_django_field = relatedStructureProp()
    schema.org description:Related anatomical structure(s) that are not part of the system but relate or connect to it, such as vascular bundles associated with an organ system.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalStructure"""

    _prop_schema = 'relatedStructure'
    _expected_schema = 'AnatomicalStructure'
    _enum = False
    _format_as = "ForeignKey"


class relatedConditionProp(SchemaProperty):

    """
    SchemaField for relatedCondition
    Usage: Include in SchemaObject SchemaFields as your_django_field = relatedConditionProp()
    schema.org description:A medical condition associated with this anatomy.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalCondition"""

    _prop_schema = 'relatedCondition'
    _expected_schema = 'MedicalCondition'
    _enum = False
    _format_as = "ForeignKey"


class comprisedOfProp(SchemaProperty):

    """
    SchemaField for comprisedOf
    Usage: Include in SchemaObject SchemaFields as your_django_field = comprisedOfProp()
    schema.org description:The underlying anatomical structures, such as organs, that comprise the anatomical system.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalStructure"""

    _prop_schema = 'comprisedOf'
    _expected_schema = 'AnatomicalStructure'
    _enum = False
    _format_as = "ForeignKey"


class associatedPathophysiologyProp(SchemaProperty):

    """
    SchemaField for associatedPathophysiology
    Usage: Include in SchemaObject SchemaFields as your_django_field = associatedPathophysiologyProp()
    schema.org description:If applicable, a description of the pathophysiology associated with the anatomical system, including potential abnormal changes in the mechanical, physical, and biochemical functions of the system.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'associatedPathophysiology'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class relatedTherapyProp(SchemaProperty):

    """
    SchemaField for relatedTherapy
    Usage: Include in SchemaObject SchemaFields as your_django_field = relatedTherapyProp()
    schema.org description:A medical therapy related to this anatomy.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalTherapy"""

    _prop_schema = 'relatedTherapy'
    _expected_schema = 'MedicalTherapy'
    _enum = False
    _format_as = "ForeignKey"
