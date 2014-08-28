# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SuperficialAnatomySchema(SchemaObject):

    """Schema Mixin for SuperficialAnatomy
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Anatomical features that can be observed by sight (without dissection), including the form and proportions of the human body as well as surface landmarks that correspond to deeper subcutaneous structures. Superficial anatomy plays an important role in sports medicine, phlebotomy, and other medical specialties as underlying anatomical structures can be identified through surface palpation. For example, during back surgery, superficial anatomy can be used to palpate and count vertebrae to find the site of incision. Or in phlebotomy, superficial anatomy can be used to locate an underlying vein; for example, the median cubital vein can be located by palpating the borders of the cubital fossa (such as the epicondyles of the humerus) and then looking for the superficial signs of the vein, such as size, prominence, ability to refill after depression, and feel of surrounding tissue support. As another example, in a subluxation (dislocation) of the glenohumeral joint, the bony structure becomes pronounced with the deltoid muscle failing to cover the glenohumeral joint allowing the edges of the scapula to be superficially visible. Here, the superficial anatomy is the visible edges of the scapula, implying the underlying dislocation of the joint (the related anatomical structure).
    """

    def __init__(self):
        self.schema = 'SuperficialAnatomy'


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


class relatedAnatomyProp(SchemaProperty):

    """
    SchemaField for relatedAnatomy
    Usage: Include in SchemaObject SchemaFields as your_django_field = relatedAnatomyProp()
    schema.org description:Anatomical systems or structures that relate to the superficial anatomy.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalStructure"""

    _prop_schema = 'relatedAnatomy'
    _expected_schema = 'AnatomicalStructure'
    _enum = False
    _format_as = "ForeignKey"


class significanceProp(SchemaProperty):

    """
    SchemaField for significance
    Usage: Include in SchemaObject SchemaFields as your_django_field = significanceProp()
    schema.org description:The significance associated with the superficial anatomy; as an example, how characteristics of the superficial anatomy can suggest underlying medical conditions or courses of treatment.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'significance'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
