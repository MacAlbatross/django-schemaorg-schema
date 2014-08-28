# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PhysicalActivityCategorySchema(SchemaObject):

    """Schema Mixin for PhysicalActivityCategory
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Categories of physical activity, organized by physiologic classification.
    """

    def __init__(self):
        self.schema = 'PhysicalActivityCategory'


CATEGORY_CHOICES = (
    ('ANAEROBICACTIVITY',
     'AnaerobicActivity: Physical activity that is of high-intensity which utilizes the anaerobic metabolism of the body.'),
    ('BALANCE',
     'Balance: Physical activity that is engaged to help maintain posture and balance.'),
    ('FLEXIBILITY',
     'Flexibility: Physical activity that is engaged in to improve joint and muscle flexibility.'),
    ('LEISURETIMEACTIVITY',
     'LeisureTimeActivity: Any physical activity engaged in for recreational purposes. Examples may include ballroom dancing, roller skating, canoeing, fishing, etc.'),
    ('OCCUPATIONALACTIVITY',
     'OccupationalActivity: Any physical activity engaged in for job-related purposes. Examples may include waiting tables, maid service, carrying a mailbag, picking fruits or vegetables, construction work, etc.'),
    ('STRENGTHTRAINING',
     'StrengthTraining: Physical activity that is engaged in to improve muscle and bone strength. Also referred to as resistance training.'),
    ('AEROBICACTIVITY',
     'AerobicActivity: Physical activity of relatively low intensity that depends primarily on the aerobic energy-generating process; during activity, the aerobic metabolism uses oxygen to adequately meet energy demands during exercise.'),
)


class categoryProp(SchemaEnumProperty):

    """
    Enumeration for category
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'category'
    choices = CATEGORY_CHOICES
    _format_as = "enum"
    adapter = {
        'ANAEROBICACTIVITY': 'AnaerobicActivity',
        'BALANCE': 'Balance',
        'FLEXIBILITY': 'Flexibility',
        'LEISURETIMEACTIVITY': 'LeisureTimeActivity',
        'OCCUPATIONALACTIVITY': 'OccupationalActivity',
        'STRENGTHTRAINING': 'StrengthTraining',
        'AEROBICACTIVITY': 'AerobicActivity',
    }
