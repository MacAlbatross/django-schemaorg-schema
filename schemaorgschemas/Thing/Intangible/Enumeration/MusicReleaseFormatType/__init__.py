# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MusicReleaseFormatTypeSchema(SchemaObject):

    """Schema Mixin for MusicReleaseFormatType
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Format of this release (the type of recording media used, ie. compact disc, digital media, LP, etc.).
    """

    def __init__(self):
        self.schema = 'MusicReleaseFormatType'


/MUSICRELEASEFORMAT_CHOICES = (
    ('/CASSETTEFORMAT', '/CassetteFormat'),
    ('/DVDFORMAT', '/DVDFormat'),
    ('/DIGITALAUDIOTAPEFORMAT', '/DigitalAudioTapeFormat'),
    ('/DIGITALFORMAT', '/DigitalFormat'),
    ('/LASERDISCFORMAT', '/LaserDiscFormat'),
    ('/VINYLFORMAT', '/VinylFormat'),
    ('/CDFORMAT', '/CDFormat'),
)


class / musicReleaseFormatProp(SchemaEnumProperty):

    """
    Enumeration for /musicReleaseFormat
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/musicReleaseFormat'
    choices = /MUSICRELEASEFORMAT_CHOICES
    _format_as = "enum"
    adapter = {
        '/CASSETTEFORMAT': '/CassetteFormat',
        '/DVDFORMAT': '/DVDFormat',
        '/DIGITALAUDIOTAPEFORMAT': '/DigitalAudioTapeFormat',
        '/DIGITALFORMAT': '/DigitalFormat',
        '/LASERDISCFORMAT': '/LaserDiscFormat',
        '/VINYLFORMAT': '/VinylFormat',
        '/CDFORMAT': '/CDFormat',
    }


# schema.org version 2.0
