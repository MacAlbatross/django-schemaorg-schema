# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Place import isicV4Prop, openingHoursSpecificationProp, photoProp, hasMapProp, reviewProp, telephoneProp, containedInProp, aggregateRatingProp, additionalPropertyProp, addressProp, logoProp, faxNumberProp, geoProp, eventProp, globalLocationNumberProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CivicStructureSchema(SchemaObject):

    """Schema Mixin for CivicStructure
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A public structure, such as a town hall or concert hall.
    """

    def __init__(self):
        self.schema = 'CivicStructure'


class openingHoursProp(SchemaProperty):

    """
    SchemaField for openingHours
    Usage: Include in SchemaObject SchemaFields as your_django_field = openingHoursProp()  
    schema.org description:The opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas &#39;,&#39; separating each day. Day or time ranges are specified using a hyphen &#39;-&#39;.- Days are specified using the following two-letter combinations: Mo, Tu, We, Th, Fr, Sa, Su.- Times are specified using 24:00 time. For example, 3pm is specified as 15:00. - Here is an example: &lt;time itemprop=&quot;openingHours&quot; datetime=&quot;Tu,Th 16:00-20:00&quot;&gt;Tuesdays and Thursdays 4-8pm&lt;/time&gt;. - If a business is open 7 days a week, then it can be specified as &lt;time itemprop=&quot;openingHours&quot; datetime=&quot;Mo-Su&quot;&gt;Monday through Sunday, all day&lt;/time&gt;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'openingHours'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
