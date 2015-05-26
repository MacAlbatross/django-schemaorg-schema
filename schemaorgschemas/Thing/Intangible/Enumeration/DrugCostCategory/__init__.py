# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DrugCostCategorySchema(SchemaObject):

    """Schema Mixin for DrugCostCategory
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Enumerated categories of medical drug costs.
    """

    def __init__(self):
        self.schema = 'DrugCostCategory'


/COSTCATEGORY_CHOICES = (
    ('/RETAIL', '/Retail'),
    ('/WHOLESALE', '/Wholesale'),
    ('/REIMBURSEMENTCAP', '/ReimbursementCap'),
)


class / costCategoryProp(SchemaEnumProperty):

    """
    Enumeration for /costCategory
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/costCategory'
    choices = /COSTCATEGORY_CHOICES
    _format_as = "enum"
    adapter = {
        '/RETAIL': '/Retail',
        '/WHOLESALE': '/Wholesale',
        '/REIMBURSEMENTCAP': '/ReimbursementCap',
    }


# schema.org version 2.0
