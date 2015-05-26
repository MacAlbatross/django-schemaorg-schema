# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EventSchema(SchemaObject):

    """Schema Mixin for Event
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the &#39;offers&#39; property. Repeated events may be structured as separate Event objects.
    """

    def __init__(self):
        self.schema = 'Event'


class inLanguageProp(SchemaProperty):

    """
    SchemaField for inLanguage
    Usage: Include in SchemaObject SchemaFields as your_django_field = inLanguageProp()  
    schema.org description:The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. Supersedes language.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'inLanguage'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class attendeeProp(SchemaProperty):

    """
    SchemaField for attendee
    Usage: Include in SchemaObject SchemaFields as your_django_field = attendeeProp()  
    schema.org description:A person or organization attending the event. Supersedes attendees.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'attendee'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class performerProp(SchemaProperty):

    """
    SchemaField for performer
    Usage: Include in SchemaObject SchemaFields as your_django_field = performerProp()  
    schema.org description:A performer at the eventfor example, a presenter, musician, musical group or actor. Supersedes performers.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'performer'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class workPerformedProp(SchemaProperty):

    """
    SchemaField for workPerformed
    Usage: Include in SchemaObject SchemaFields as your_django_field = workPerformedProp()  
    schema.org description:A work performed in some event, for example a play performed in a TheaterEvent.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference CreativeWork"""

    _prop_schema = 'workPerformed'
    _expected_schema = 'CreativeWork'
    _enum = False
    _format_as = "ForeignKey"


class startDateProp(SchemaProperty):

    """
    SchemaField for startDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = startDateProp()  
    schema.org description:The start date and time of the item (in ISO 8601 date format).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'startDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class previousStartDateProp(SchemaProperty):

    """
    SchemaField for previousStartDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = previousStartDateProp()  
    schema.org description:Used in conjunction with eventStatus for rescheduled or cancelled events. This property contains the previously scheduled start date. For rescheduled events, the startDate property should be used for the newly scheduled start date. In the (rare) case of an event that has been postponed and rescheduled multiple times, this field may be repeated.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'previousStartDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class superEventProp(SchemaProperty):

    """
    SchemaField for superEvent
    Usage: Include in SchemaObject SchemaFields as your_django_field = superEventProp()  
    schema.org description:An event that this event is a part of. For example, a collection of individual music performances might each have a music festival as their superEvent.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Event"""

    _prop_schema = 'superEvent'
    _expected_schema = 'Event'
    _enum = False
    _format_as = "ForeignKey"


class reviewProp(SchemaProperty):

    """
    SchemaField for review
    Usage: Include in SchemaObject SchemaFields as your_django_field = reviewProp()  
    schema.org description:A review of the item. Supersedes reviews.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Review"""

    _prop_schema = 'review'
    _expected_schema = 'Review'
    _enum = False
    _format_as = "ForeignKey"


class recordedInProp(SchemaProperty):

    """
    SchemaField for recordedIn
    Usage: Include in SchemaObject SchemaFields as your_django_field = recordedInProp()  
    schema.org description:The CreativeWork that captured all or part of this Event. Inverse property: recordedAt.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference CreativeWork"""

    _prop_schema = 'recordedIn'
    _expected_schema = 'CreativeWork'
    _enum = False
    _format_as = "ForeignKey"


class aggregateRatingProp(SchemaProperty):

    """
    SchemaField for aggregateRating
    Usage: Include in SchemaObject SchemaFields as your_django_field = aggregateRatingProp()  
    schema.org description:The overall rating, based on a collection of reviews or ratings, of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AggregateRating"""

    _prop_schema = 'aggregateRating'
    _expected_schema = 'AggregateRating'
    _enum = False
    _format_as = "ForeignKey"


class subEventProp(SchemaProperty):

    """
    SchemaField for subEvent
    Usage: Include in SchemaObject SchemaFields as your_django_field = subEventProp()  
    schema.org description:An Event that is part of this event. For example, a conference event includes many presentations, each of which is a subEvent of the conference. Supersedes subEvents.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Event"""

    _prop_schema = 'subEvent'
    _expected_schema = 'Event'
    _enum = False
    _format_as = "ForeignKey"


class offersProp(SchemaProperty):

    """
    SchemaField for offers
    Usage: Include in SchemaObject SchemaFields as your_django_field = offersProp()  
    schema.org description:An offer to provide this itemfor example, an offer to sell a product, rent the DVD of a movie, or give away tickets to an event.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Offer"""

    _prop_schema = 'offers'
    _expected_schema = 'Offer'
    _enum = False
    _format_as = "ForeignKey"


class eventStatusProp(SchemaProperty):

    """
    SchemaField for eventStatus
    Usage: Include in SchemaObject SchemaFields as your_django_field = eventStatusProp()  
    schema.org description:An eventStatus of an event represents its status; particularly useful when an event is cancelled or rescheduled.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference EventStatusType"""

    _prop_schema = 'eventStatus'
    _expected_schema = 'EventStatusType'
    _enum = False
    _format_as = "ForeignKey"


class typicalAgeRangeProp(SchemaProperty):

    """
    SchemaField for typicalAgeRange
    Usage: Include in SchemaObject SchemaFields as your_django_field = typicalAgeRangeProp()  
    schema.org description:The typical expected age range, e.g. &#39;7-9&#39;, &#39;11-&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'typicalAgeRange'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class durationProp(SchemaProperty):

    """
    SchemaField for duration
    Usage: Include in SchemaObject SchemaFields as your_django_field = durationProp()  
    schema.org description:The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Duration"""

    _prop_schema = 'duration'
    _expected_schema = 'Duration'
    _enum = False
    _format_as = "TimeField"


class endDateProp(SchemaProperty):

    """
    SchemaField for endDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = endDateProp()  
    schema.org description:The end date and time of the item (in ISO 8601 date format).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'endDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class organizerProp(SchemaProperty):

    """
    SchemaField for organizer
    Usage: Include in SchemaObject SchemaFields as your_django_field = organizerProp()  
    schema.org description:An organizer of an Event.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'organizer'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class doorTimeProp(SchemaProperty):

    """
    SchemaField for doorTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = doorTimeProp()  
    schema.org description:The time admission will commence.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'doorTime'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class locationProp(SchemaProperty):

    """
    SchemaField for location
    Usage: Include in SchemaObject SchemaFields as your_django_field = locationProp()  
    schema.org description:The location of the event, organization or action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'location'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
