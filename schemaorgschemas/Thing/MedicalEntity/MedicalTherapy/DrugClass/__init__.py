# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, nameProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, descriptionProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.MedicalEntity.MedicalTherapy import contraindicationProp, indicationProp, adverseOutcomeProp, seriousAdverseOutcomeProp, duplicateTherapyProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DrugClassSchema(SchemaObject):

    """Schema Mixin for DrugClass
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A class of medical drugs, e.g., statins. Classes can represent general pharmacological class, common mechanisms of action, common physiological effects, etc.
    """

    def __init__(self):
        self.schema = 'DrugClass'


class drugProp(SchemaProperty):

    """
    SchemaField for drug
    Usage: Include in SchemaObject SchemaFields as your_django_field = drugProp()  
    schema.org description:A drug in this drug class.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Drug"""

    _prop_schema = 'drug'
    _expected_schema = 'Drug'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
