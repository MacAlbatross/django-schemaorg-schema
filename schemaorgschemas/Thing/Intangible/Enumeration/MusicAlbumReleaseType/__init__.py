# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MusicAlbumReleaseTypeSchema(SchemaObject):

    """Schema Mixin for MusicAlbumReleaseType
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The kind of release which this album is: single, EP or album.
    """

    def __init__(self):
        self.schema = 'MusicAlbumReleaseType'


ALBUMRELEASETYPE_CHOICES = (
    ('BROADCASTRELEASE', 'BroadcastRelease: BroadcastRelease.'),
    ('EPRELEASE', 'EPRelease: EPRelease.'),
    ('SINGLERELEASE', 'SingleRelease: SingleRelease.'),
    ('ALBUMRELEASE', 'AlbumRelease: AlbumRelease.'),
)


class albumReleaseTypeProp(SchemaEnumProperty):

    """
    Enumeration for albumReleaseType
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'albumReleaseType'
    choices = ALBUMRELEASETYPE_CHOICES
    _format_as = "enum"
    adapter = {
        'BROADCASTRELEASE': 'BroadcastRelease',
        'EPRELEASE': 'EPRelease',
        'SINGLERELEASE': 'SingleRelease',
        'ALBUMRELEASE': 'AlbumRelease',
    }


# schema.org version 2.0
