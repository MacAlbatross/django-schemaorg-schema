from django.conf import settings
from django import template
from django.template import Library, NodeList
from django.template.base import TemplateSyntaxError, TextNode, Node
from formatters import SchemaPropFormatter, EnumPropFormatter
from django.db.models.loading import get_model
from django.utils.encoding import (
    force_str
)

import sys


SCHEME = getattr(settings, "SCHEME", "http://")

register = Library()

VOID_ELEMENTS = ["<area ", "<base ", "<br", "<col ", "<command ", "<embed ", "<hr", "<img ", "<input ", "<keygen ", "<link ", "<meta ", "<param ", "<source ", "<track ", "<wbr"]
FILE_FIELD_SPECIALS = ['.url', '.path']


class ReturnedRender(object):

    def __init__(self, rendered, variable_node=None):
        self._rendered = rendered
        self._normal = True
        self._variable_node = variable_node

    def __str__(self):
        return str(self._rendered)

    def __unicode__(self):
        return str(self._rendered)

    @property
    def normal(self):
        return self._normal

    @normal.setter
    def normal(self, value):
        self._normal = value

    @property
    def variable_node(self):
        return self._variable_node

    @variable_node.setter
    def variable_node(self, value):
        self._variable_node = value


class OpenTagNode(TextNode):

    def __init__(self):
        return super(OpenTagNode, self).__init__('<')

    def __repr__(self):
        return force_str("<Open Tag Node: <'%s'>" % self.s[:25], 'ascii', errors='replace')


class CloseTagNode(TextNode):

    def __init__(self):
        return super(CloseTagNode, self).__init__('>')

    def __repr__(self):
        return force_str("<Close Tag Node: '%s'>>" % self.s[:25], 'ascii', errors='replace')


class OpenVoidNode(TextNode):

    def __init__(self):
        return super(OpenVoidNode, self).__init__('<')

    def __repr__(self):
        return force_str("<Open Void Node: <'%s'>" % self.s[:25], 'ascii', errors='replace')


@register.simple_tag(takes_context=False)
def schemaprop(item, field_name=None, variable_node=None):
    """takes an instance of an model object and field name
    and returns the schema.org property and value formatted
    version where appropriate.
    """
    magix = None
    if not field_name:
        raise TemplateSyntaxError('need to specify field name')
    if field_name[-8:] == '_display' and field_name[:4] == 'get_':
        cut_name = field_name[4:-8]
        try:
            store_value = getattr(item, cut_name)
            field_name = cut_name
        except:
            raise TemplateSyntaxError("SchemaError, " + field_name + "not in SchemaFields")
    if "." in field_name:
        find_point = field_name.find(".")
        try:
            new_item = getattr(item, field_name[:find_point])
            new_field_name = field_name[find_point + 1:]
            return schemaprop(new_item, new_field_name, variable_node)
        except:
            for last_check in FILE_FIELD_SPECIALS:
                if field_name[-len(last_check):] == last_check:
                    new_field_name = field_name[:-len(last_check)]
                    return schemaprop(item, new_field_name, variable_node)
            raise TemplateSyntaxError("SchemaError, " + field_name + "not in SchemaFields")
    try:
        schema = getattr(item.SchemaFields, field_name)
    except AttributeError:
        schema = None
    try:
        store_value = getattr(item, field_name)
    except AttributeError:
        store_value = None
    if (not store_value):
        try:
            store_value = getattr(settings, field_name, None)
        except AttributeError:
            raise TemplateSyntaxError("SchemaError, " + field_name + " not in SchemaFields")
    if schema:
        magix = SchemaPropFormatter(schema=schema)
        if callable(store_value):
            magix.format_as = 'default'
            magix.value = str(store_value())
            return ReturnedRender(magix.render(), variable_node)
    else:
        ret = ReturnedRender(store_value, variable_node)
        ret.normal = False
        return ret

    format_as = schema._format_as
    if (schema._format_as == 'ForeignKey'):
        if (schema.traceback is True):
            f_obj = getattr(item, field_name)
            item_scope = schemascope(f_obj)
            if item_scope:
                store_value = item_scope
            else:
                format_as = 'default'
        else:
            format_as = 'default'
    if schema._format_as == 'enum':
        magix = EnumPropFormatter(schema=schema)
    if not magix:
        magix = SchemaPropFormatter(schema=schema)
    magix.format_as = format_as
    magix.value = store_value
    ret = ReturnedRender(magix.render(), variable_node)
    return ret


@register.simple_tag(takes_context=False)
def schemascope(item):
    """
    Takes instance of model object and includes the schema.org url
    If there's an internal url that is also included.
    """
    ret = ''
    url = ''
    try:
        ret = '"' + item.schema_url + '"'
    except:
        # not a schemascope item
        return ''
    try:
        url = item.get_absolute_url()
    except:
        return ret
    if url:
        ret = ret + ' link="' + SCHEME + item.site.domain + url + '"'
    return ret


@register.tag(name="schemaobject")
def do_schema_render(parser, token):
    """
    The schemaobject and endschemaobject tag replace the html element that contains the object.
    This is then provided as the second argument should the default 'section' not be desired.
    The third optional parameter is contained inside quotes is the html class details.
    The forth option allows the use of ids for the section,  appending the object.pk to the id text
    {% schemaobject object section "class='otherstuff'" 'obj' %}
    The all fields that have relevant schema.org information associated through their SchemaFields will have the schema.org information inserted into the HTML.
    """
    token = token.split_contents()
    nodelist = parser.parse(('endschemaobject',))
    parser.delete_first_token()
    # defaults the HTML class to section unless over-ride specified
    section = 'section'
    htmlattr = None
    id_attr = None
    c = token.__len__()
    if c > 2:
        section = token[2]
    if c > 3:
        htmlattr = token[3]
        # remove quotes
        htmlattr = htmlattr[1:-1]
    if c > 4:
        id_attr = token[4]
        id_attr = id_attr[1:-1]
    rets = SchemaNode(nodelist, token[1], section, htmlattr, id_attr)
    return rets


class SchemaNode(template.Node):

    def __init__(self, nodelist, object_name, html_class=None,
                 html_attribute=None, id_attr=None):
        self.nodelist = nodelist
        self.object_name = object_name
        self.html_class = html_class
        self.html_attribute = html_attribute
        self.id_attr = id_attr

    @staticmethod
    def split_text_node(text_node_string):

        def close_tag_nodes(node_text):
            if '/>' in node_text:
                close_string = '/>'
            else:
                close_string = '>'
            cut_off = node_text.find(close_string)
            if cut_off == -1:
                return [TextNode(node_text)]
            else:
                output = [TextNode(node_text[:cut_off])]
                nod = CloseTagNode()
                nod.s = close_string
                cut_text = node_text[cut_off + 1:]
                if cut_text:
                    nod.s = nod.s + cut_text
                output.append(nod)
                return output

        text_node_string = text_node_string.replace('\r', '')
        text_node_string = text_node_string.replace('\n', '')
        if '<' not in text_node_string:
            closes = close_tag_nodes(text_node_string)
            return closes
        text_node_string = text_node_string.lstrip()
        split_start = text_node_string.find('<')
        tags = text_node_string.split('<')
        output = []
        for tag in tags:
            tag = tag.lstrip()
            if not tag:
                tag_node = None
            else:
                if not split_start:
                    tag_node = OpenTagNode()
                else:
                    tag_node = None
                    split_start = 0
                void_test = "<" + tag
                void_ele = ''
                for vi in VOID_ELEMENTS:
                    if vi in void_test:
                        void_ele = vi[1:]
                        break
                if void_ele:
                    tag = tag.replace(void_ele, '', 1)
                    tag_node = OpenVoidNode()
                    tag_node.s = '<' + void_ele + ' '
                if tag_node:
                    output.append(tag_node)
                if tag:
                    closes = close_tag_nodes(tag)
                    for item in closes:
                        output.append(item)
        return output

    def get_context_object(self, context):
        i = context.dicts.__len__() - 1
        # going backwards as it seems the information is stored in the last
        while i >= 0:
            dic = context.dicts[i]
            obj = dic.get(self.object_name, None)
            if obj:
                return obj
            i = i - 1
        if not obj:
            raise TemplateSyntaxError(
                self.object_name +
                ' not found in template context')

    @staticmethod
    def strip_annoying_text(text_to_strip, text_replace=''):
        text_to_strip = text_to_strip.replace(text_replace, "")
        text_to_strip = text_to_strip.strip("\r\n")
        return text_to_strip

    def assemble_for_node(self, node, context):
        if self.object_name not in str(node.sequence):
            return node
        sub_obj = str(node.sequence).replace(self.object_name + '.', '')
        sfind = sub_obj.find("_")
        if sfind != -1:
            sub_obj = sub_obj[:sfind]
        my_model = get_model(self.obj._meta.app_label, sub_obj)
        if not my_model:
            sfind = sub_obj.find(".")
            if sfind != -1:
                sub_obj = sub_obj[:sfind]
            my_model = get_model(self.obj._meta.app_label, sub_obj)
        if not my_model:
            obj_manager = getattr(self.obj, sub_obj)
            my_model = obj_manager.model
        # see if the object is actually a manager rather than a field
        schema_model = my_model.objects.all()[0]
        if not hasattr(my_model, 'SchemaFields'):
            return node
        new_nodes = self.process_node_list(node.nodelist_loop, context)
        new_nodes = self.process_node_list(new_nodes, context)
        outlist = []
        filter_dict = {}
        if hasattr(self.obj, sub_obj + '_set'):
            attrholder = getattr(self.obj, sub_obj + '_set')
            filter_dict = attrholder.core_filters
        if not filter_dict.__len__():
            if hasattr(self.obj, sub_obj):
                # manager
                filter_dict = getattr(self.obj, sub_obj).core_filters
        if filter_dict:
            schema_models = my_model.objects.filter(**filter_dict)
            for schema_model in schema_models:
                context.update({node.loopvars[0]: schema_model})
                output = SchemaNode(new_nodes, node.loopvars[0], self.html_class, self.html_attribute)
                outlist.append(output)
        node.nodelist = outlist
        return node

    def assemble_if_node(self, node, context):
        new_conditions = []
        # iterate through list
        for condition in node.conditions_nodelists:
            # condition is tuple index 0 points to a template literal object
            # index 1 points to a NodeList
            t_lit = condition[0]
            new_nodes = self.process_node_list(condition[1], context)
            new_conditions.append((t_lit, new_nodes))
        node.conditions = new_conditions
        return node

    def process_node_list(self, nodelist, context):
        new_nodes = NodeList()
        variable_nodes = []
        i = nodelist.__len__() - 1
        l = 0
        while l <= i:
            while l <= i:
                this_node = nodelist[l]
                node_class = this_node.__class__.__name__
                if node_class == "ForNode":
                    this_node = self.assemble_for_node(this_node, context)
                if node_class == "IfNode":
                    this_node = self.assemble_if_node(this_node, context)
                if node_class == 'TextNode':
                    splitted = self.split_text_node(this_node.s)
                    for item in splitted:
                        new_nodes.append(item)
                else:
                    new_nodes.append(this_node)
                if "VariableNode" in node_class:
                    variable_nodes.append(new_nodes.__len__() - 1)
                l = l + 1
            schema_props = []
            for item in variable_nodes:
                node_in_question = new_nodes[item]
                schema_prop = ''
                if hasattr(node_in_question, 'filter_expression'):
                    filter_exp = str(node_in_question.filter_expression)
                    filter_exp = filter_exp.replace(self.object_name + '.', '')
                    # ensure ones with added template tags work properly
                    if '|' in filter_exp:
                        filter_exp = filter_exp[:filter_exp.find('|')]
                    try:
                        schema_prop = schemaprop(self.obj, filter_exp, item)
                    except:
                        e = sys.exc_info()[0]
                        raise TemplateSyntaxError(e)
                    schema_props.append(schema_prop)
            prop_count = schema_props.__len__() - 1
            prop_index = 0
            while prop_index <= prop_count:
                prior_node_counter = 1
                this_prop = schema_props[prop_index]
                prior_node = new_nodes[this_prop.variable_node - prior_node_counter]
                found_prior = False
                while not (found_prior or (prior_node_counter == this_prop.variable_node)):
                    if prior_node.__class__.__name__ == 'CloseTagNode':
                        prior_node.s = ' ' + str(this_prop) + prior_node.s
                        found_prior = True
                    elif prior_node.__class__.__name__ == 'OpenVoidNode':
                        found_prior = True
                        prior_node.s = prior_node.s + str(this_prop) + ' '
                    elif prior_node.__class__.__name__ == 'OpenTagNode':
                        found_prior = True
                    else:
                        prior_node_counter = prior_node_counter + 1
                        prior_node = new_nodes[this_prop.variable_node - prior_node_counter]
                prop_index = prop_index + 1
            scope = schemascope(self.obj)
            top_text = "<" + self.html_class + ' '
            if self.html_attribute:
                top_text = top_text + self.html_attribute
            if self.id_attr:
                top_text = top_text + ' id="#' + self.id_attr + str(self.obj.pk) + '"'
            top_text = top_text + ' itemscope itemtype=' + scope + '>'
            bottom_text = "</" + self.html_class + ">"
            topnode = TextNode(top_text)
            bottomnode = TextNode(bottom_text)
            new_nodes.insert(0, topnode)
            new_nodes.append(bottomnode)
        return new_nodes

    def render(self, context):
        self.obj = self.get_context_object(context)
        new_nodes = self.process_node_list(self.nodelist, context)
        output = new_nodes.render(context)
        return output
