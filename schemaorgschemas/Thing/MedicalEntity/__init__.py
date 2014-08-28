# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalEntitySchema(SchemaObject):

    """Schema Mixin for MedicalEntity
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The most generic type of entity related to health and the practice of medicine.
    """

    def __init__(self):
        self.schema = 'MedicalEntity'


class codeProp(SchemaProperty):

    """
    SchemaField for code
    Usage: Include in SchemaObject SchemaFields as your_django_field = codeProp()  
    schema.org description:A medical code for the entity, taken from a controlled vocabulary or ontology such as ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalCode"""

    _prop_schema = 'code'
    _expected_schema = 'MedicalCode'
    _enum = False
    _format_as = "ForeignKey"


class recognizingAuthorityProp(SchemaProperty):

    """
    SchemaField for recognizingAuthority
    Usage: Include in SchemaObject SchemaFields as your_django_field = recognizingAuthorityProp()  
    schema.org description:If applicable, the organization that officially recognizes this entity as part of its endorsed system of medicine.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'recognizingAuthority'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class medicineSystemProp(SchemaProperty):

    """
    SchemaField for medicineSystem
    Usage: Include in SchemaObject SchemaFields as your_django_field = medicineSystemProp()  
    schema.org description:The system of medicine that includes this MedicalEntity, for example &#39;evidence-based&#39;, &#39;homeopathic&#39;, &#39;chiropractic&#39;, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicineSystem"""

    _prop_schema = 'medicineSystem'
    _expected_schema = 'MedicineSystem'
    _enum = False
    _format_as = "ForeignKey"


class relevantSpecialtyProp(SchemaProperty):

    """
    SchemaField for relevantSpecialty
    Usage: Include in SchemaObject SchemaFields as your_django_field = relevantSpecialtyProp()  
    schema.org description:If applicable, a medical specialty in which this entity is relevant.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalSpecialty"""

    _prop_schema = 'relevantSpecialty'
    _expected_schema = 'MedicalSpecialty'
    _enum = False
    _format_as = "ForeignKey"


class alternateNameProp(SchemaProperty):

    """
    SchemaField for alternateName
    Usage: Include in SchemaObject SchemaFields as your_django_field = alternateNameProp()  
    schema.org description:An alias for the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'alternateName'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class studyProp(SchemaProperty):

    """
    SchemaField for study
    Usage: Include in SchemaObject SchemaFields as your_django_field = studyProp()  
    schema.org description:A medical study or trial related to this entity.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalStudy"""

    _prop_schema = 'study'
    _expected_schema = 'MedicalStudy'
    _enum = False
    _format_as = "ForeignKey"


class guidelineProp(SchemaProperty):

    """
    SchemaField for guideline
    Usage: Include in SchemaObject SchemaFields as your_django_field = guidelineProp()  
    schema.org description:A medical guideline related to this entity.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalGuideline"""

    _prop_schema = 'guideline'
    _expected_schema = 'MedicalGuideline'
    _enum = False
    _format_as = "ForeignKey"
