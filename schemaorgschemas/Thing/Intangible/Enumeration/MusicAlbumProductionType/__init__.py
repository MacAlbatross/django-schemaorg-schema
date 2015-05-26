# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MusicAlbumProductionTypeSchema(SchemaObject):

    """Schema Mixin for MusicAlbumProductionType
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Classification of the album by it&#39;s type of content: soundtrack, live album, studio album, etc.
    """

    def __init__(self):
        self.schema = 'MusicAlbumProductionType'


/ALBUMPRODUCTIONTYPE_CHOICES = (
    ('/DJMIXALBUM', '/DJMixAlbum'),
    ('/DEMOALBUM', '/DemoAlbum'),
    ('/LIVEALBUM', '/LiveAlbum'),
    ('/MIXTAPEALBUM', '/MixtapeAlbum'),
    ('/REMIXALBUM', '/RemixAlbum'),
    ('/SOUNDTRACKALBUM', '/SoundtrackAlbum'),
    ('/SPOKENWORDALBUM', '/SpokenWordAlbum'),
    ('/STUDIOALBUM', '/StudioAlbum'),
    ('/COMPILATIONALBUM', '/CompilationAlbum'),
)


class / albumProductionTypeProp(SchemaEnumProperty):

    """
    Enumeration for /albumProductionType
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/albumProductionType'
    choices = /ALBUMPRODUCTIONTYPE_CHOICES
    _format_as = "enum"
    adapter = {
        '/DJMIXALBUM': '/DJMixAlbum',
        '/DEMOALBUM': '/DemoAlbum',
        '/LIVEALBUM': '/LiveAlbum',
        '/MIXTAPEALBUM': '/MixtapeAlbum',
        '/REMIXALBUM': '/RemixAlbum',
        '/SOUNDTRACKALBUM': '/SoundtrackAlbum',
        '/SPOKENWORDALBUM': '/SpokenWordAlbum',
        '/STUDIOALBUM': '/StudioAlbum',
        '/COMPILATIONALBUM': '/CompilationAlbum',
    }


# schema.org version 2.0
