# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalObservationalStudyDesignSchema(SchemaObject):

    """Schema Mixin for MedicalObservationalStudyDesign
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Design models for observational medical studies. Enumerated type.
    """

    def __init__(self):
        self.schema = 'MedicalObservationalStudyDesign'


STUDYDESIGN_CHOICES = (
    ('COHORTSTUDY',
     'CohortStudy: Also known as a panel study. A cohort study is a form of longitudinal study used in medicine and social science. It is one type of study design and should be compared with a cross-sectional study.  A cohort is a group of people who share a common characteristic or experience within a defined period (e.g., are born, leave school, lose their job, are exposed to a drug or a vaccine, etc.). The comparison group may be the general population from which the cohort is drawn, or it may be another cohort of persons thought to have had little or no exposure to the substance under investigation, but otherwise similar. Alternatively, subgroups within the cohort may be compared with each other.'),
    ('CROSSSECTIONAL',
     'CrossSectional: Studies carried out on pre-existing data (usually from &#39;snapshot&#39; surveys), such as that collected by the Census Bureau. Sometimes called Prevalence Studies.'),
    ('LONGITUDINAL',
     'Longitudinal: Unlike cross-sectional studies, longitudinal studies track the same people, and therefore the differences observed in those people are less likely to be the result of cultural differences across generations. Longitudinal studies are also used in medicine to uncover predictors of certain diseases.'),
    ('OBSERVATIONAL', 'Observational: An observational study design.'),
    ('REGISTRY', 'Registry: A registry-based study design.'),
    ('CASESERIES',
     'CaseSeries: A case series (also known as a clinical series) is a medical research study that tracks patients with a known exposure given similar treatment or examines their medical records for exposure and outcome. A case series can be retrospective or prospective and usually involves a smaller number of patients than the more powerful case-control studies or randomized controlled trials. Case series may be consecutive or non-consecutive, depending on whether all cases presenting to the reporting authors over a period of time were included, or only a selection.'),
)


class studyDesignProp(SchemaEnumProperty):

    """
    Enumeration for studyDesign
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'studyDesign'
    choices = STUDYDESIGN_CHOICES
    _format_as = "enum"
    adapter = {
        'COHORTSTUDY': 'CohortStudy',
        'CROSSSECTIONAL': 'CrossSectional',
        'LONGITUDINAL': 'Longitudinal',
        'OBSERVATIONAL': 'Observational',
        'REGISTRY': 'Registry',
        'CASESERIES': 'CaseSeries',
    }


# schema.org version 2.0
