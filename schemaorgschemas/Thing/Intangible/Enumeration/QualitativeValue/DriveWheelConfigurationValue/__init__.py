# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Intangible.Enumeration.QualitativeValue import valueReferenceProp, greaterProp, lesserOrEqualProp, equalProp, lesserProp, additionalPropertyProp, greaterOrEqualProp, nonEqualProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DriveWheelConfigurationValueSchema(SchemaObject):

    """Schema Mixin for DriveWheelConfigurationValue
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A value indicating which roadwheels will receive torque.
    """

    def __init__(self):
        self.schema = 'DriveWheelConfigurationValue'


/DRIVEWHEELCONFIGURATION_CHOICES = (
    ('/FOURWHEELDRIVECONFIGURATION', '/FourWheelDriveConfiguration'),
    ('/FRONTWHEELDRIVECONFIGURATION', '/FrontWheelDriveConfiguration'),
    ('/REARWHEELDRIVECONFIGURATION', '/RearWheelDriveConfiguration'),
    ('/ALLWHEELDRIVECONFIGURATION', '/AllWheelDriveConfiguration'),
)


class / driveWheelConfigurationProp(SchemaEnumProperty):

    """
    Enumeration for /driveWheelConfiguration
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/driveWheelConfiguration'
    choices = /DRIVEWHEELCONFIGURATION_CHOICES
    _format_as = "enum"
    adapter = {
        '/FOURWHEELDRIVECONFIGURATION': '/FourWheelDriveConfiguration',
        '/FRONTWHEELDRIVECONFIGURATION': '/FrontWheelDriveConfiguration',
        '/REARWHEELDRIVECONFIGURATION': '/RearWheelDriveConfiguration',
        '/ALLWHEELDRIVECONFIGURATION': '/AllWheelDriveConfiguration',
    }


# schema.org version 2.0
