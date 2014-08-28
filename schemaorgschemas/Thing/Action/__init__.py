# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ActionSchema(SchemaObject):

    """Schema Mixin for Action
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An action performed by a direct agent and indirect     participants upon a direct object. Optionally happens at a location     with the help of an inanimate instrument. The execution of the action     may produce a result. Specific action sub-type documentation specifies     the exact expectation of each argument/role.
    """

    def __init__(self):
        self.schema = 'Action'


class actionStatusProp(SchemaProperty):

    """
    SchemaField for actionStatus
    Usage: Include in SchemaObject SchemaFields as your_django_field = actionStatusProp()  
    schema.org description:Indicates the current disposition of the Action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ActionStatusType"""

    _prop_schema = 'actionStatus'
    _expected_schema = 'ActionStatusType'
    _enum = False
    _format_as = "ForeignKey"


class instrumentProp(SchemaProperty):

    """
    SchemaField for instrument
    Usage: Include in SchemaObject SchemaFields as your_django_field = instrumentProp()  
    schema.org description:The object that helped the agent perform the action. e.g. John wrote a book with *a pen*.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'instrument'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


class objectProp(SchemaProperty):

    """
    SchemaField for object
    Usage: Include in SchemaObject SchemaFields as your_django_field = objectProp()  
    schema.org description:The object upon the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn&#39;t). e.g. John read *a book*.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'object'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


class participantProp(SchemaProperty):

    """
    SchemaField for participant
    Usage: Include in SchemaObject SchemaFields as your_django_field = participantProp()  
    schema.org description:Other co-agents that participated in the action indirectly. e.g. John wrote a book with *Steve*.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'participant'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class locationProp(SchemaProperty):

    """
    SchemaField for location
    Usage: Include in SchemaObject SchemaFields as your_django_field = locationProp()  
    schema.org description:The location of the event, organization or action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PostalAddress"""

    _prop_schema = 'location'
    _expected_schema = 'PostalAddress'
    _enum = False
    _format_as = "ForeignKey"


class startTimeProp(SchemaProperty):

    """
    SchemaField for startTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = startTimeProp()  
    schema.org description:When the Action was performed: start time. This is for actions that span a period of time. e.g. John wrote a book from *January* to December.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'startTime'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class targetProp(SchemaProperty):

    """
    SchemaField for target
    Usage: Include in SchemaObject SchemaFields as your_django_field = targetProp()  
    schema.org description:Indicates a target EntryPoint for an Action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference EntryPoint"""

    _prop_schema = 'target'
    _expected_schema = 'EntryPoint'
    _enum = False
    _format_as = "ForeignKey"


class endTimeProp(SchemaProperty):

    """
    SchemaField for endTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = endTimeProp()  
    schema.org description:When the Action was performed: end time. This is for actions that span a period of time. e.g. John wrote a book from January to *December*.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'endTime'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class agentProp(SchemaProperty):

    """
    SchemaField for agent
    Usage: Include in SchemaObject SchemaFields as your_django_field = agentProp()  
    schema.org description:The direct performer or driver of the action (animate or inanimate). e.g. *John* wrote a book.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'agent'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class resultProp(SchemaProperty):

    """
    SchemaField for result
    Usage: Include in SchemaObject SchemaFields as your_django_field = resultProp()  
    schema.org description:The result produced in the action. e.g. John wrote *a book*.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'result'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"
