# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PlaceSchema(SchemaObject):

    """Schema Mixin for Place
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Entities that have a somewhat fixed, physical extension.
    """

    def __init__(self):
        self.schema = 'Place'


class isicV4Prop(SchemaProperty):

    """
    SchemaField for isicV4
    Usage: Include in SchemaObject SchemaFields as your_django_field = isicV4Prop()  
    schema.org description:The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'isicV4'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class openingHoursSpecificationProp(SchemaProperty):

    """
    SchemaField for openingHoursSpecification
    Usage: Include in SchemaObject SchemaFields as your_django_field = openingHoursSpecificationProp()  
    schema.org description:The opening hours of a certain place.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference OpeningHoursSpecification"""

    _prop_schema = 'openingHoursSpecification'
    _expected_schema = 'OpeningHoursSpecification'
    _enum = False
    _format_as = "ForeignKey"


class photoProp(SchemaProperty):

    """
    SchemaField for photo
    Usage: Include in SchemaObject SchemaFields as your_django_field = photoProp()  
    schema.org description:A photograph of this place. Supersedes photos.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ImageObject"""

    _prop_schema = 'photo'
    _expected_schema = 'ImageObject'
    _enum = False
    _format_as = "URLField"


class geoProp(SchemaProperty):

    """
    SchemaField for geo
    Usage: Include in SchemaObject SchemaFields as your_django_field = geoProp()  
    schema.org description:The geo coordinates of the place.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference GeoCoordinates"""

    _prop_schema = 'geo'
    _expected_schema = 'GeoCoordinates'
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


class containedInProp(SchemaProperty):

    """
    SchemaField for containedIn
    Usage: Include in SchemaObject SchemaFields as your_django_field = containedInProp()  
    schema.org description:The basic containment relation between places.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'containedIn'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"


class faxNumberProp(SchemaProperty):

    """
    SchemaField for faxNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = faxNumberProp()  
    schema.org description:The fax number.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'faxNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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


class additionalPropertyProp(SchemaProperty):

    """
    SchemaField for additionalProperty
    Usage: Include in SchemaObject SchemaFields as your_django_field = additionalPropertyProp()  
    schema.org description:A property-value pair representing an additional characteristics of the entitity, e.g. a product feature or another characteristic for which there is no matching property in schema.org. Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. http://schema.org/width, http://schema.org/color, http://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PropertyValue"""

    _prop_schema = 'additionalProperty'
    _expected_schema = 'PropertyValue'
    _enum = False
    _format_as = "ForeignKey"


class addressProp(SchemaProperty):

    """
    SchemaField for address
    Usage: Include in SchemaObject SchemaFields as your_django_field = addressProp()  
    schema.org description:Physical address of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PostalAddress"""

    _prop_schema = 'address'
    _expected_schema = 'PostalAddress'
    _enum = False
    _format_as = "ForeignKey"


class telephoneProp(SchemaProperty):

    """
    SchemaField for telephone
    Usage: Include in SchemaObject SchemaFields as your_django_field = telephoneProp()  
    schema.org description:The telephone number.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'telephone'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class logoProp(SchemaProperty):

    """
    SchemaField for logo
    Usage: Include in SchemaObject SchemaFields as your_django_field = logoProp()  
    schema.org description:An associated logo.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ImageObject"""

    _prop_schema = 'logo'
    _expected_schema = 'ImageObject'
    _enum = False
    _format_as = "URLField"


class hasMapProp(SchemaProperty):

    """
    SchemaField for hasMap
    Usage: Include in SchemaObject SchemaFields as your_django_field = hasMapProp()  
    schema.org description:A URL to a map of the place. Supersedes map, maps.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Map"""

    _prop_schema = 'hasMap'
    _expected_schema = 'Map'
    _enum = False
    _format_as = "ForeignKey"


class eventProp(SchemaProperty):

    """
    SchemaField for event
    Usage: Include in SchemaObject SchemaFields as your_django_field = eventProp()  
    schema.org description:Upcoming or past event associated with this place, organization, or action. Supersedes events.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Event"""

    _prop_schema = 'event'
    _expected_schema = 'Event'
    _enum = False
    _format_as = "ForeignKey"


class globalLocationNumberProp(SchemaProperty):

    """
    SchemaField for globalLocationNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = globalLocationNumberProp()  
    schema.org description:The Global Location Number (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'globalLocationNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
