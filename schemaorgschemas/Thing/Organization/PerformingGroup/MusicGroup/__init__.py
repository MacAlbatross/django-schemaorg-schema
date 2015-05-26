# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, telephoneProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, foundingLocationProp, locationProp, employeeProp, emailProp, seeksProp, numberOfEmployeesProp, subOrganizationProp, brandProp, ownsProp, awardProp, departmentProp, dissolutionDateProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, memberOfProp, legalNameProp, vatIDProp, globalLocationNumberProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MusicGroupSchema(SchemaObject):

    """Schema Mixin for MusicGroup
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A musical group, such as a band, an orchestra, or a choir. Can also be a solo musician.
    """

    def __init__(self):
        self.schema = 'MusicGroup'


class albumProp(SchemaProperty):

    """
    SchemaField for album
    Usage: Include in SchemaObject SchemaFields as your_django_field = albumProp()  
    schema.org description:A music album. Supersedes albums.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicAlbum"""

    _prop_schema = 'album'
    _expected_schema = 'MusicAlbum'
    _enum = False
    _format_as = "ForeignKey"


class genreProp(SchemaProperty):

    """
    SchemaField for genre
    Usage: Include in SchemaObject SchemaFields as your_django_field = genreProp()  
    schema.org description:Genre of the creative work or group.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'genre'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class trackProp(SchemaProperty):

    """
    SchemaField for track
    Usage: Include in SchemaObject SchemaFields as your_django_field = trackProp()  
    schema.org description:A music recording (track)usually a single song. If an ItemList is given, the list should contain items of type MusicRecording. Supersedes tracks.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicRecording"""

    _prop_schema = 'track'
    _expected_schema = 'MusicRecording'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
