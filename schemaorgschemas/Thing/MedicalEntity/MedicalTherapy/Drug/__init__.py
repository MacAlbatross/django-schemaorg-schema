# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalTherapy import contraindicationProp, indicationProp, adverseOutcomeProp, seriousAdverseOutcomeProp, duplicateTherapyProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DrugSchema(SchemaObject):

    """Schema Mixin for Drug
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A chemical or biologic substance, used as a medical therapy, that has a physiological effect on an organism.
    """

    def __init__(self):
        self.schema = 'Drug'


class alcoholWarningProp(SchemaProperty):

    """
    SchemaField for alcoholWarning
    Usage: Include in SchemaObject SchemaFields as your_django_field = alcoholWarningProp()
    schema.org description:Any precaution, guidance, contraindication, etc. related to consumption of alcohol while taking this drug.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'alcoholWarning'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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


class relatedDrugProp(SchemaProperty):

    """
    SchemaField for relatedDrug
    Usage: Include in SchemaObject SchemaFields as your_django_field = relatedDrugProp()
    schema.org description:Any other drug related to this one, for example commonly-prescribed alternatives.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Drug"""

    _prop_schema = 'relatedDrug'
    _expected_schema = 'Drug'
    _enum = False
    _format_as = "ForeignKey"


class prescribingInfoProp(SchemaProperty):

    """
    SchemaField for prescribingInfo
    Usage: Include in SchemaObject SchemaFields as your_django_field = prescribingInfoProp()
    schema.org description:Link to prescribing information for the drug.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'prescribingInfo'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


class isAvailableGenericallyProp(SchemaProperty):

    """
    SchemaField for isAvailableGenerically
    Usage: Include in SchemaObject SchemaFields as your_django_field = isAvailableGenericallyProp()
    schema.org description:True if the drug is available in a generic form (regardless of name).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'isAvailableGenerically'
    _expected_schema = None
    _enum = False
    _format_as = "BooleanField"


class pregnancyCategoryProp(SchemaProperty):

    """
    SchemaField for pregnancyCategory
    Usage: Include in SchemaObject SchemaFields as your_django_field = pregnancyCategoryProp()
    schema.org description:Pregnancy category of this drug.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DrugPregnancyCategory"""

    _prop_schema = 'pregnancyCategory'
    _expected_schema = 'DrugPregnancyCategory'
    _enum = False
    _format_as = "ForeignKey"


class costProp(SchemaProperty):

    """
    SchemaField for cost
    Usage: Include in SchemaObject SchemaFields as your_django_field = costProp()
    schema.org description:Cost per unit of the drug, as reported by the source being tagged.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DrugCost"""

    _prop_schema = 'cost'
    _expected_schema = 'DrugCost'
    _enum = False
    _format_as = "ForeignKey"


class pregnancyWarningProp(SchemaProperty):

    """
    SchemaField for pregnancyWarning
    Usage: Include in SchemaObject SchemaFields as your_django_field = pregnancyWarningProp()
    schema.org description:Any precaution, guidance, contraindication, etc. related to this drug&#39;s use during pregnancy.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'pregnancyWarning'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class clincalPharmacologyProp(SchemaProperty):

    """
    SchemaField for clincalPharmacology
    Usage: Include in SchemaObject SchemaFields as your_django_field = clincalPharmacologyProp()
    schema.org description:Description of the absorption and elimination of drugs, including their concentration (pharmacokinetics, pK) and biological effects (pharmacodynamics, pD).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'clincalPharmacology'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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


class availableStrengthProp(SchemaProperty):

    """
    SchemaField for availableStrength
    Usage: Include in SchemaObject SchemaFields as your_django_field = availableStrengthProp()
    schema.org description:An available dosage strength for the drug.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DrugStrength"""

    _prop_schema = 'availableStrength'
    _expected_schema = 'DrugStrength'
    _enum = False
    _format_as = "ForeignKey"


class doseScheduleProp(SchemaProperty):

    """
    SchemaField for doseSchedule
    Usage: Include in SchemaObject SchemaFields as your_django_field = doseScheduleProp()
    schema.org description:A dosing schedule for the drug for a given population, either observed, recommended, or maximum dose based on the type used.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DoseSchedule"""

    _prop_schema = 'doseSchedule'
    _expected_schema = 'DoseSchedule'
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


class interactingDrugProp(SchemaProperty):

    """
    SchemaField for interactingDrug
    Usage: Include in SchemaObject SchemaFields as your_django_field = interactingDrugProp()
    schema.org description:Another drug that is known to interact with this drug in a way that impacts the effect of this drug or causes a risk to the patient. Note: disease interactions are typically captured as contraindications.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Drug"""

    _prop_schema = 'interactingDrug'
    _expected_schema = 'Drug'
    _enum = False
    _format_as = "ForeignKey"


class labelDetailsProp(SchemaProperty):

    """
    SchemaField for labelDetails
    Usage: Include in SchemaObject SchemaFields as your_django_field = labelDetailsProp()
    schema.org description:Link to the drug&#39;s label details.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'labelDetails'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


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


class administrationRouteProp(SchemaProperty):

    """
    SchemaField for administrationRoute
    Usage: Include in SchemaObject SchemaFields as your_django_field = administrationRouteProp()
    schema.org description:A route by which this drug may be administered, e.g. &#39;oral&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'administrationRoute'
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


class warningProp(SchemaProperty):

    """
    SchemaField for warning
    Usage: Include in SchemaObject SchemaFields as your_django_field = warningProp()
    schema.org description:Any FDA or other warnings about the drug (text or URL).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'warning'
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


class foodWarningProp(SchemaProperty):

    """
    SchemaField for foodWarning
    Usage: Include in SchemaObject SchemaFields as your_django_field = foodWarningProp()
    schema.org description:Any precaution, guidance, contraindication, etc. related to consumption of specific foods while taking this drug.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'foodWarning'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class drugClassProp(SchemaProperty):

    """
    SchemaField for drugClass
    Usage: Include in SchemaObject SchemaFields as your_django_field = drugClassProp()
    schema.org description:The class of drug this belongs to (e.g., statins).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DrugClass"""

    _prop_schema = 'drugClass'
    _expected_schema = 'DrugClass'
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


class overdosageProp(SchemaProperty):

    """
    SchemaField for overdosage
    Usage: Include in SchemaObject SchemaFields as your_django_field = overdosageProp()
    schema.org description:Any information related to overdose on a drug, including signs or symptoms, treatments, contact information for emergency response.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'overdosage'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class prescriptionStatusProp(SchemaProperty):

    """
    SchemaField for prescriptionStatus
    Usage: Include in SchemaObject SchemaFields as your_django_field = prescriptionStatusProp()
    schema.org description:Indicates whether this drug is available by prescription or over-the-counter.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DrugPrescriptionStatus"""

    _prop_schema = 'prescriptionStatus'
    _expected_schema = 'DrugPrescriptionStatus'
    _enum = False
    _format_as = "ForeignKey"


class breastfeedingWarningProp(SchemaProperty):

    """
    SchemaField for breastfeedingWarning
    Usage: Include in SchemaObject SchemaFields as your_django_field = breastfeedingWarningProp()
    schema.org description:Any precaution, guidance, contraindication, etc. related to this drug&#39;s use by breastfeeding mothers.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'breastfeedingWarning'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
