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


PREGNANCYCATEGORY_CHOICES = (
    ('FDACATEGORYB',
     'FDAcategoryB: A designation by the US FDA signifying that animal reproduction studies have failed to demonstrate a risk to the fetus and there are no adequate and well-controlled studies in pregnant women.'),
    ('FDACATEGORYC',
     'FDAcategoryC: A designation by the US FDA signifying that animal reproduction studies have shown an adverse effect on the fetus and there are no adequate and well-controlled studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.'),
    ('FDACATEGORYD',
     'FDAcategoryD: A designation by the US FDA signifying that there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience or studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.'),
    ('FDACATEGORYX',
     'FDAcategoryX: A designation by the US FDA signifying that studies in animals or humans have demonstrated fetal abnormalities and/or there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience, and the risks involved in use of the drug in pregnant women clearly outweigh potential benefits.'),
    ('FDANOTEVALUATED',
     'FDAnotEvaluated: A designation that the drug in question has not been assigned a pregnancy category designation by the US FDA.'),
    ('FDACATEGORYA',
     'FDAcategoryA: A designation by the US FDA signifying that adequate and well-controlled studies have failed to demonstrate a risk to the fetus in the first trimester of pregnancy (and there is no evidence of risk in later trimesters).'),
)


class pregnancyCategoryProp(SchemaEnumProperty):

    """
    Enumeration for pregnancyCategory
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'pregnancyCategory'
    choices = PREGNANCYCATEGORY_CHOICES
    _format_as = "enum"
    adapter = {
        'FDACATEGORYB': 'FDAcategoryB',
        'FDACATEGORYC': 'FDAcategoryC',
        'FDACATEGORYD': 'FDAcategoryD',
        'FDACATEGORYX': 'FDAcategoryX',
        'FDANOTEVALUATED': 'FDAnotEvaluated',
        'FDACATEGORYA': 'FDAcategoryA',
    }


# schema.org version 2.0
