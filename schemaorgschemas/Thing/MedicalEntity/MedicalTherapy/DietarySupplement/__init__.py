# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalTherapy import contraindicationProp, indicationProp, adverseOutcomeProp, seriousAdverseOutcomeProp, duplicateTherapyProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DietarySupplementSchema(SchemaObject):

    """Schema Mixin for DietarySupplement
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A product taken by mouth that contains a dietary ingredient intended to supplement the diet. Dietary ingredients may include vitamins, minerals, herbs or other botanicals, amino acids, and substances such as enzymes, organ tissues, glandulars and metabolites.
    """

    def __init__(self):
        self.schema = 'DietarySupplement'


class activeIngredientProp(SchemaProperty):

    """
    SchemaField for activeIngredient
    Usage: Include in SchemaObject SchemaFields as your_django_field = activeIngredientProp()  
    schema.org description:An active ingredient, typically chemical compounds and/or biologic substances.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'activeIngredient'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class dosageFormProp(SchemaProperty):

    """
    SchemaField for dosageForm
    Usage: Include in SchemaObject SchemaFields as your_django_field = dosageFormProp()  
    schema.org description:A dosage form in which this drug/supplement is available, e.g. &#39;tablet&#39;, &#39;suspension&#39;, &#39;injection&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'dosageForm'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class nonProprietaryNameProp(SchemaProperty):

    """
    SchemaField for nonProprietaryName
    Usage: Include in SchemaObject SchemaFields as your_django_field = nonProprietaryNameProp()  
    schema.org description:The generic name of this drug or supplement.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'nonProprietaryName'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class mechanismOfActionProp(SchemaProperty):

    """
    SchemaField for mechanismOfAction
    Usage: Include in SchemaObject SchemaFields as your_django_field = mechanismOfActionProp()  
    schema.org description:The specific biochemical interaction through which this drug or supplement produces its pharmacological effect.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'mechanismOfAction'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class safetyConsiderationProp(SchemaProperty):

    """
    SchemaField for safetyConsideration
    Usage: Include in SchemaObject SchemaFields as your_django_field = safetyConsiderationProp()  
    schema.org description:Any potential safety concern associated with the supplement. May include interactions with other drugs and foods, pregnancy, breastfeeding, known adverse reactions, and documented efficacy of the supplement.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'safetyConsideration'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class targetPopulationProp(SchemaProperty):

    """
    SchemaField for targetPopulation
    Usage: Include in SchemaObject SchemaFields as your_django_field = targetPopulationProp()  
    schema.org description:Characteristics of the population for which this is intended, or which typically uses it, e.g. &#39;adults&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'targetPopulation'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class backgroundProp(SchemaProperty):

    """
    SchemaField for background
    Usage: Include in SchemaObject SchemaFields as your_django_field = backgroundProp()  
    schema.org description:Descriptive information establishing a historical perspective on the supplement. May include the rationale for the name, the population where the supplement first came to prominence, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'background'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class recommendedIntakeProp(SchemaProperty):

    """
    SchemaField for recommendedIntake
    Usage: Include in SchemaObject SchemaFields as your_django_field = recommendedIntakeProp()  
    schema.org description:Recommended intake of this supplement for a given population as defined by a specific recommending authority.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference RecommendedDoseSchedule"""

    _prop_schema = 'recommendedIntake'
    _expected_schema = 'RecommendedDoseSchedule'
    _enum = False
    _format_as = "ForeignKey"


class isProprietaryProp(SchemaProperty):

    """
    SchemaField for isProprietary
    Usage: Include in SchemaObject SchemaFields as your_django_field = isProprietaryProp()  
    schema.org description:True if this item&#39;s name is a proprietary/brand name (vs. generic name).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'isProprietary'
    _expected_schema = None
    _enum = False
    _format_as = "BooleanField"


class maximumIntakeProp(SchemaProperty):

    """
    SchemaField for maximumIntake
    Usage: Include in SchemaObject SchemaFields as your_django_field = maximumIntakeProp()  
    schema.org description:Recommended intake of this supplement for a given population as defined by a specific recommending authority.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MaximumDoseSchedule"""

    _prop_schema = 'maximumIntake'
    _expected_schema = 'MaximumDoseSchedule'
    _enum = False
    _format_as = "ForeignKey"


class legalStatusProp(SchemaProperty):

    """
    SchemaField for legalStatus
    Usage: Include in SchemaObject SchemaFields as your_django_field = legalStatusProp()  
    schema.org description:The drug or supplement&#39;s legal status, including any controlled substance schedules that apply.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DrugLegalStatus"""

    _prop_schema = 'legalStatus'
    _expected_schema = 'DrugLegalStatus'
    _enum = False
    _format_as = "ForeignKey"


class manufacturerProp(SchemaProperty):

    """
    SchemaField for manufacturer
    Usage: Include in SchemaObject SchemaFields as your_django_field = manufacturerProp()  
    schema.org description:The manufacturer of the product.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'manufacturer'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"
