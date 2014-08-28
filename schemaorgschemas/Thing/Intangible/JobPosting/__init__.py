# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class JobPostingSchema(SchemaObject):

    """Schema Mixin for JobPosting
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A listing that describes a job opening in a certain organization.
    """

    def __init__(self):
        self.schema = 'JobPosting'


class educationRequirementsProp(SchemaProperty):

    """
    SchemaField for educationRequirements
    Usage: Include in SchemaObject SchemaFields as your_django_field = educationRequirementsProp()
    schema.org description:Educational background needed for the position.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'educationRequirements'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class experienceRequirementsProp(SchemaProperty):

    """
    SchemaField for experienceRequirements
    Usage: Include in SchemaObject SchemaFields as your_django_field = experienceRequirementsProp()
    schema.org description:Description of skills and experience needed for the position.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'experienceRequirements'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class specialCommitmentsProp(SchemaProperty):

    """
    SchemaField for specialCommitments
    Usage: Include in SchemaObject SchemaFields as your_django_field = specialCommitmentsProp()
    schema.org description:Any special commitments associated with this job posting. Valid entries include VeteranCommit, MilitarySpouseCommit, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'specialCommitments'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class benefitsProp(SchemaProperty):

    """
    SchemaField for benefits
    Usage: Include in SchemaObject SchemaFields as your_django_field = benefitsProp()
    schema.org description:Description of benefits associated with the job.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'benefits'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class salaryCurrencyProp(SchemaProperty):

    """
    SchemaField for salaryCurrency
    Usage: Include in SchemaObject SchemaFields as your_django_field = salaryCurrencyProp()
    schema.org description:The currency (coded using ISO 4217, http://en.wikipedia.org/wiki/ISO_4217 used for the main salary information in this job posting.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'salaryCurrency'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class titleProp(SchemaProperty):

    """
    SchemaField for title
    Usage: Include in SchemaObject SchemaFields as your_django_field = titleProp()
    schema.org description:The title of the job.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'title'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class employmentTypeProp(SchemaProperty):

    """
    SchemaField for employmentType
    Usage: Include in SchemaObject SchemaFields as your_django_field = employmentTypeProp()
    schema.org description:Type of employment (e.g. full-time, part-time, contract, temporary, seasonal, internship).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'employmentType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class qualificationsProp(SchemaProperty):

    """
    SchemaField for qualifications
    Usage: Include in SchemaObject SchemaFields as your_django_field = qualificationsProp()
    schema.org description:Specific qualifications required for this role.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'qualifications'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class industryProp(SchemaProperty):

    """
    SchemaField for industry
    Usage: Include in SchemaObject SchemaFields as your_django_field = industryProp()
    schema.org description:The industry associated with the job position.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'industry'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class incentivesProp(SchemaProperty):

    """
    SchemaField for incentives
    Usage: Include in SchemaObject SchemaFields as your_django_field = incentivesProp()
    schema.org description:Description of bonus and commission compensation aspects of the job.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'incentives'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class datePostedProp(SchemaProperty):

    """
    SchemaField for datePosted
    Usage: Include in SchemaObject SchemaFields as your_django_field = datePostedProp()
    schema.org description:Publication date for the job posting.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'datePosted'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class skillsProp(SchemaProperty):

    """
    SchemaField for skills
    Usage: Include in SchemaObject SchemaFields as your_django_field = skillsProp()
    schema.org description:Skills required to fulfill this role.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'skills'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class responsibilitiesProp(SchemaProperty):

    """
    SchemaField for responsibilities
    Usage: Include in SchemaObject SchemaFields as your_django_field = responsibilitiesProp()
    schema.org description:Responsibilities associated with this role.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'responsibilities'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class workHoursProp(SchemaProperty):

    """
    SchemaField for workHours
    Usage: Include in SchemaObject SchemaFields as your_django_field = workHoursProp()
    schema.org description:The typical working hours for this job (e.g. 1st shift, night shift, 8am-5pm).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'workHours'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class jobLocationProp(SchemaProperty):

    """
    SchemaField for jobLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = jobLocationProp()
    schema.org description:A (typically single) geographic location associated with the job position.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'jobLocation'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"


class baseSalaryProp(SchemaProperty):

    """
    SchemaField for baseSalary
    Usage: Include in SchemaObject SchemaFields as your_django_field = baseSalaryProp()
    schema.org description:The base salary of the job.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'baseSalary'
    _expected_schema = None
    _enum = False
    _format_as = "DecimalField"


class hiringOrganizationProp(SchemaProperty):

    """
    SchemaField for hiringOrganization
    Usage: Include in SchemaObject SchemaFields as your_django_field = hiringOrganizationProp()
    schema.org description:Organization offering the job position.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'hiringOrganization'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class occupationalCategoryProp(SchemaProperty):

    """
    SchemaField for occupationalCategory
    Usage: Include in SchemaObject SchemaFields as your_django_field = occupationalCategoryProp()
    schema.org description:Category or categories describing the job. Use BLS O*NET-SOC taxonomy: http://www.onetcenter.org/taxonomy.html. Ideally includes textual label and formal code, with the property repeated for each applicable value.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'occupationalCategory'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
