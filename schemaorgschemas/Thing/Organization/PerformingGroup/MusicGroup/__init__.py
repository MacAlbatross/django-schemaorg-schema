# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, interactionCountProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, locationProp, employeeProp, emailProp, seeksProp, subOrganizationProp, brandProp, ownsProp, telephoneProp, departmentProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, legalNameProp, vatIDProp, globalLocationNumberProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

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
    schema.org description:A music album. Supercedes albums.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicAlbum"""

    _prop_schema = 'album'
    _expected_schema = 'MusicAlbum'
    _enum = False
    _format_as = "ForeignKey"


class trackProp(SchemaProperty):

    """
    SchemaField for track
    Usage: Include in SchemaObject SchemaFields as your_django_field = trackProp()
    schema.org description:A music recording (track)-usually a single song. Supercedes tracks.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicRecording"""

    _prop_schema = 'track'
    _expected_schema = 'MusicRecording'
    _enum = False
    _format_as = "ForeignKey"


class musicGroupMemberProp(SchemaProperty):

    """
    SchemaField for musicGroupMember
    Usage: Include in SchemaObject SchemaFields as your_django_field = musicGroupMemberProp()
    schema.org description:A member of the music group-for example, John, Paul, George, or Ringo.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'musicGroupMember'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"
