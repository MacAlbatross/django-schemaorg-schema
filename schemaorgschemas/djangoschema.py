from django.conf import settings
from django.contrib.sites.models import Site


SCHEMA_ORG = getattr(settings, "SCHEMA_ORG", "http://schema.org/")


class SchemaObject(object):

    """Generic class for all SchemaObject objects"""

    def __init__(self):
        self.schema = ''

    @property
    def schema_url(self):
        self.site = Site.objects.get_current()
        if not self.schema:
            raise Exception('Do not use schemaobject directly')
        return SCHEMA_ORG + self.schema

    class SchemaFields():

        """Holds schema fields in child object, does nothing here"""
        pass


class SchemaProperty(object):

    """Generic class for all SchemaProperty objects"""

    def __init__(self, *args, **kwargs):
        """Setting traceback to False will stop foreign key look ups to the absolute url
        and instead use the property on the field
        """
        self.traceback = kwargs.pop('traceback', True)

    @property
    def schema_url(self):
        if not getattr(self, '_prop_schema'):
            raise Exception(
                'No _prop_schema defined hint:Do not use SchemaProerty object directly')
        return SCHEMA_ORG + self._prop_schema

    @property
    def schema_prop(self):
        if not getattr(self, '_prop_schema'):
            raise Exception(
                'No _prop_schema defined hint:Do not use SchemaProerty object directly')
        return self._prop_schema

    @property
    def format_as(self):
        return self._format_as()


class SchemaEnumProperty(SchemaProperty):

    def __init__(self, adapter=None):
        """The optional adapter is to be used when the current choices values do not match those used by schema.org
        it should be a dictionary with the schema.org enumeration values as keys, and with the values being those
        currently used by the database.  If no adapter is provided then the system will expect those provided by the
        class choices"""
        if adapter:
            self.adapter = adapter
        super(SchemaEnumProperty, self).__init__()

    @property
    def schema_url(self):
        if not getattr(self, '_prop_schema'):
            raise Exception(
                'No _prop_schema defined hint:Do not use SchemaProerty object directly')
        return SCHEMA_ORG + self._prop_schema
