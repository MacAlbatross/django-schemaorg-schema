from django.template import Context
from django.template.base import TemplateDoesNotExist
from schemaorgschemas.djangoschema import SCHEMA_ORG
from django.template.loader import get_template


class SchemaPropFormatter(object):

    def __init__(self, **kwargs):
        self.format_as = kwargs.pop('format_as', '')
        self.schema = kwargs.pop('schema', None)
        self.value = kwargs.pop('value', None)
        if self.schema:
            self.schema_prop = self.schema.schema_prop
        if not self.schema_prop:
            self.schema_prop = kwargs.pop('schema_prop', None)

    def render(self):
        try:
            t = get_template(self.format_as + '.txt')
        except TemplateDoesNotExist:
            t = get_template('default.txt')
        c = Context()
        c['value'] = self.value
        c['schema_prop'] = self.schema_prop
        out = t.render(c)
        return out


class EnumPropFormatter(SchemaPropFormatter):

    def __init__(self, **kwargs):
        self.format_as = kwargs.pop('format_as', '')
        self.schema = kwargs.pop('schema', None)
        self.value = kwargs.pop('value', None)

    def render(self):
        if self.schema.adapter:
            enum_prop = self.schema.adapter[self.value]
        else:
            enum_prop = self.value
        try:
            t = get_template(self.format_as + '.txt')
        except TemplateDoesNotExist:
            t = get_template('default.txt')
        c = Context()
        c['schema_prop'] = self.schema.schema_prop
        c['enum_prop'] = SCHEMA_ORG + enum_prop
        out = t.render(c)
        return out
