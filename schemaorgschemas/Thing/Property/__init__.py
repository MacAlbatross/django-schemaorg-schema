# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PropertySchema(SchemaObject):

    """Schema Mixin for Property
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A property, used to indicate attributes and relationships of some Thing; equivalent to rdf:Property.
    """

    def __init__(self):
        self.schema = 'Property'


class rangeIncludesProp(SchemaProperty):

    """
    SchemaField for rangeIncludes
    Usage: Include in SchemaObject SchemaFields as your_django_field = rangeIncludesProp()  
    schema.org description:Relates a property to a class that constitutes (one of) the expected type(s) for values of the property.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Class"""

    _prop_schema = 'rangeIncludes'
    _expected_schema = 'Class'
    _enum = False
    _format_as = "TextField"


class supersededByProp(SchemaProperty):

    """
    SchemaField for supersededBy
    Usage: Include in SchemaObject SchemaFields as your_django_field = supersededByProp()  
    schema.org description:Relates a term (i.e. a property, class or enumeration) to one that supersedes it.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Property"""

    _prop_schema = 'supersededBy'
    _expected_schema = 'Property'
    _enum = False
    _format_as = "ForeignKey"


class domainIncludesProp(SchemaProperty):

    """
    SchemaField for domainIncludes
    Usage: Include in SchemaObject SchemaFields as your_django_field = domainIncludesProp()  
    schema.org description:Relates a property to a class that is (one of) the type(s) the property is expected to be used on.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Class"""

    _prop_schema = 'domainIncludes'
    _expected_schema = 'Class'
    _enum = False
    _format_as = "TextField"


class inverseOfProp(SchemaProperty):

    """
    SchemaField for inverseOf
    Usage: Include in SchemaObject SchemaFields as your_django_field = inverseOfProp()  
    schema.org description:Relates a property to a property that is its inverse. Inverse properties relate the same pairs of items to each other, but in reversed direction. For example, the &#39;alumni&#39; and &#39;alumniOf&#39; properties are inverseOf each other. Some properties don&#39;t have explicit inverses; in these situations RDFa and JSON-LD syntax for reverse properties can be used.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Property"""

    _prop_schema = 'inverseOf'
    _expected_schema = 'Property'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
