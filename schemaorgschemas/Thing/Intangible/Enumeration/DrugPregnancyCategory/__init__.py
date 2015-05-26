# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DrugPregnancyCategorySchema(SchemaObject):

    """Schema Mixin for DrugPregnancyCategory
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Categories that represent an assessment of the risk of fetal injury due to a drug or pharmaceutical used as directed by the mother during pregnancy.
    """

    def __init__(self):
        self.schema = 'DrugPregnancyCategory'


/PREGNANCYCATEGORY_CHOICES = (
    ('/FDACATEGORYB', '/FDAcategoryB'),
    ('/FDACATEGORYC', '/FDAcategoryC'),
    ('/FDACATEGORYD', '/FDAcategoryD'),
    ('/FDACATEGORYX', '/FDAcategoryX'),
    ('/FDANOTEVALUATED', '/FDAnotEvaluated'),
    ('/FDACATEGORYA', '/FDAcategoryA'),
)


class / pregnancyCategoryProp(SchemaEnumProperty):

    """
    Enumeration for /pregnancyCategory
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/pregnancyCategory'
    choices = /PREGNANCYCATEGORY_CHOICES
    _format_as = "enum"
    adapter = {
        '/FDACATEGORYB': '/FDAcategoryB',
        '/FDACATEGORYC': '/FDAcategoryC',
        '/FDACATEGORYD': '/FDAcategoryD',
        '/FDACATEGORYX': '/FDAcategoryX',
        '/FDANOTEVALUATED': '/FDAnotEvaluated',
        '/FDACATEGORYA': '/FDAcategoryA',
    }


# schema.org version 2.0
