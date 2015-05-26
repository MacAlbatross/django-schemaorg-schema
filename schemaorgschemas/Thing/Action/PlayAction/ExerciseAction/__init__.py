# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.PlayAction import audienceProp, eventProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ExerciseActionSchema(SchemaObject):

    """Schema Mixin for ExerciseAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of participating in exertive activity for the purposes of improving health and fitness.
    """

    def __init__(self):
        self.schema = 'ExerciseAction'


class distanceProp(SchemaProperty):

    """
    SchemaField for distance
    Usage: Include in SchemaObject SchemaFields as your_django_field = distanceProp()  
    schema.org description:The distance travelled, e.g. exercising or travelling.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Distance"""

    _prop_schema = 'distance'
    _expected_schema = 'Distance'
    _enum = False
    _format_as = "ForeignKey"


class toLocationProp(SchemaProperty):

    """
    SchemaField for toLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = toLocationProp()  
    schema.org description:A sub property of location. The final location of the object or the agent after the action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'toLocation'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"


class exerciseTypeProp(SchemaProperty):

    """
    SchemaField for exerciseType
    Usage: Include in SchemaObject SchemaFields as your_django_field = exerciseTypeProp()  
    schema.org description:Type(s) of exercise or activity, such as strength training, flexibility training, aerobics, cardiac rehabilitation, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'exerciseType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class sportsTeamProp(SchemaProperty):

    """
    SchemaField for sportsTeam
    Usage: Include in SchemaObject SchemaFields as your_django_field = sportsTeamProp()  
    schema.org description:A sub property of participant. The sports team that participated on this action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference SportsTeam"""

    _prop_schema = 'sportsTeam'
    _expected_schema = 'SportsTeam'
    _enum = False
    _format_as = "ForeignKey"


class sportsActivityLocationProp(SchemaProperty):

    """
    SchemaField for sportsActivityLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = sportsActivityLocationProp()  
    schema.org description:A sub property of location. The sports activity location where this action occurred.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference SportsActivityLocation"""

    _prop_schema = 'sportsActivityLocation'
    _expected_schema = 'SportsActivityLocation'
    _enum = False
    _format_as = "ForeignKey"


class exercisePlanProp(SchemaProperty):

    """
    SchemaField for exercisePlan
    Usage: Include in SchemaObject SchemaFields as your_django_field = exercisePlanProp()  
    schema.org description:A sub property of instrument. The exercise plan used on this action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ExercisePlan"""

    _prop_schema = 'exercisePlan'
    _expected_schema = 'ExercisePlan'
    _enum = False
    _format_as = "ForeignKey"


class fromLocationProp(SchemaProperty):

    """
    SchemaField for fromLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = fromLocationProp()  
    schema.org description:A sub property of location. The original location of the object or the agent before the action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'fromLocation'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"


class exerciseRelatedDietProp(SchemaProperty):

    """
    SchemaField for exerciseRelatedDiet
    Usage: Include in SchemaObject SchemaFields as your_django_field = exerciseRelatedDietProp()  
    schema.org description:A sub property of instrument. The diet used in this action. Supersedes diet.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Diet"""

    _prop_schema = 'exerciseRelatedDiet'
    _expected_schema = 'Diet'
    _enum = False
    _format_as = "ForeignKey"


class sportsEventProp(SchemaProperty):

    """
    SchemaField for sportsEvent
    Usage: Include in SchemaObject SchemaFields as your_django_field = sportsEventProp()  
    schema.org description:A sub property of location. The sports event where this action occurred.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference SportsEvent"""

    _prop_schema = 'sportsEvent'
    _expected_schema = 'SportsEvent'
    _enum = False
    _format_as = "ForeignKey"


class exerciseCourseProp(SchemaProperty):

    """
    SchemaField for exerciseCourse
    Usage: Include in SchemaObject SchemaFields as your_django_field = exerciseCourseProp()  
    schema.org description:A sub property of location. The course where this action was taken. Supersedes course.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'exerciseCourse'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"


class opponentProp(SchemaProperty):

    """
    SchemaField for opponent
    Usage: Include in SchemaObject SchemaFields as your_django_field = opponentProp()  
    schema.org description:A sub property of participant. The opponent on this action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'opponent'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
