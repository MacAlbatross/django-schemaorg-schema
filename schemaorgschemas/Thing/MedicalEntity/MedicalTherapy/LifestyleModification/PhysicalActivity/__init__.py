# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.MedicalEntity.MedicalTherapy import contraindicationProp, indicationProp, adverseOutcomeProp, seriousAdverseOutcomeProp, duplicateTherapyProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PhysicalActivitySchema(SchemaObject):

    """Schema Mixin for PhysicalActivity
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any bodily activity that enhances or maintains physical fitness and overall health and wellness. Includes activity that is part of daily living and routine, structured exercise, and exercise prescribed as part of a medical treatment or recovery plan.
    """

    def __init__(self):
        self.schema = 'PhysicalActivity'


class categoryProp(SchemaProperty):

    """
    SchemaField for category
    Usage: Include in SchemaObject SchemaFields as your_django_field = categoryProp()  
    schema.org description:A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'category'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class epidemiologyProp(SchemaProperty):

    """
    SchemaField for epidemiology
    Usage: Include in SchemaObject SchemaFields as your_django_field = epidemiologyProp()  
    schema.org description:The characteristics of associated patients, such as age, gender, race etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'epidemiology'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class pathophysiologyProp(SchemaProperty):

    """
    SchemaField for pathophysiology
    Usage: Include in SchemaObject SchemaFields as your_django_field = pathophysiologyProp()  
    schema.org description:Changes in the normal mechanical, physical, and biochemical functions that are associated with this activity or condition.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'pathophysiology'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class associatedAnatomyProp(SchemaProperty):

    """
    SchemaField for associatedAnatomy
    Usage: Include in SchemaObject SchemaFields as your_django_field = associatedAnatomyProp()  
    schema.org description:The anatomy of the underlying organ system or structures associated with this entity.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalStructure"""

    _prop_schema = 'associatedAnatomy'
    _expected_schema = 'AnatomicalStructure'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
