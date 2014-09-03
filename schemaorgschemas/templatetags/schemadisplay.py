from django import template
from django.template import Context
from django.template import Library, NodeList, VariableNode
from django.template.defaulttags import ForNode, IfNode
from django.template.base import TemplateSyntaxError, TextNode
from formatters import SchemaPropFormatter, EnumPropFormatter
from django.db.models.loading import get_model

register = Library()


@register.simple_tag(takes_context=False)
def schemaprop(item, field_name=None):
    magix = None
    if not field_name:
        raise TemplateSyntaxError('need to specify field name')
    if field_name[-8:] == '_display' and field_name[:4] == 'get_':
        cut_name = field_name[4:-8]
        try:
            store_value = getattr(item, cut_name)
            field_name = cut_name
        except:
            print "SchemaError, field_name not in SchemaFields"
    if "." in field_name:
        find_point = field_name.find(".")
        try:
            new_item = getattr(item, field_name[:find_point])
            new_field_name = field_name[find_point + 1:]
            return schemaprop(new_item, new_field_name)
        except:
            print "SchemaError"
    try:
        store_value = getattr(item, field_name)
    except:
        print "SchemaError, field_name not in SchemaFields"
    schema = getattr(item.SchemaFields, field_name)
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
    ret = magix.render()
    return ret


@register.simple_tag(takes_context=False)
def schemascope(item):
    try:
        ret = '"' + item.schema_url + '"'
    except:
        # not a schemascope item
        return None
    try:
        url = item.get_absolute_url()
    except:
        return None
    if url:
        ret = ret + ' link="http://' + item.site.domain + url + '"'
    return ret


@register.tag(name="schemaobject")
def do_schema_render(parser, token):
    token = token.split_contents()
    nodelist = parser.parse(('endschemaobject',))
    parser.delete_first_token()
    # defaults the HTML class to section unless over-ride specified
    section = 'section'
    htmlattr = None
    c = token.__len__()
    if c > 2:
        section = token[2]
    if c > 3:
        htmlattr = token[3]
        # remove quotes
        htmlattr = htmlattr[1:-1]
    rets = SchemaNode(nodelist, token[1], section, htmlattr)
    return rets


class SchemaNode(template.Node):

    def __init__(self, nodelist, object_name, html_class=None,
                 html_attribute=None):
        self.nodelist = nodelist
        self.object_name = object_name
        self.html_class = html_class
        self.html_attribute = html_attribute

    @staticmethod
    def split_text_node(text_node_string):
        f = text_node_string.find('>')
        o_f = 0
        item = text_node_string[0:f + 1]
        output = [TextNode(item)]
        while True:
            o_f = f
            f = text_node_string.find('>', o_f + 1)
            if f == -1:
                item = TextNode(text_node_string[o_f + 1:])
            else:
                item = TextNode(text_node_string[o_f + 1: f + 1])
            if item.s:
                output.append(item)
            if f == -1:
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
            raise Exception(
                self.object_name +
                ' not found in template context')
        
    def render_for_node(self, node, context):
        if self.object_name not in str(node.sequence):
            return node.render(context)
        sub_obj = str(node.sequence).replace(self.object_name + '.', '')
        sub_obj = sub_obj[:sub_obj.find("_")]
        my_model = get_model(self.obj._meta.app_label, sub_obj)
        schema_model = my_model.objects.all()[0]
        context.update({node.loopvars[0]: schema_model})
        if not hasattr(my_model, 'SchemaFields'):
            return node.render(context)
        new_nodes = NodeList()
        for item in node.nodelist_loop:
            if item.__class__.__name__ == "TextNode":
                split = self.split_text_node(item.s)
                for sub in split:
                    new_nodes.append(sub)
            else:
                new_nodes.append(item)
        section_text = ""
        while "/" not in section_text:
            end = new_nodes.pop()
            section_text = end.s
        section_text = section_text.replace("<","")
        section_text = section_text.replace(">","")
        section_text = section_text.replace("/","")
        section_text = section_text.strip("\r\n")
        top = new_nodes.pop(0)
        top_text = top.s
        top_text = top_text.replace("<", "")
        top_text = top_text.replace(">", "")
        top_text = top_text.replace(section_text, '')
        top_text = top_text.strip("\r\n")
        output = SchemaNode(new_nodes,node.loopvars[0], section_text, top_text )
        out = output.render(context)
        return out  
        
        #should be topped an tailed
    def render_if_node(self, node, context):
        out = node.render(context)
        new_nodes = NodeList()
        index = 0
        l = node.nodelist.__len__()
        while index != l:
            new_node = node.nodelist[index]
            node_class = new_node.__class__.__name__
            if node_class == "DebugVariableNode":
                if hasattr(new_node, 'filter_expression'):
                    #is it schema?
                    filter_exp = str(new_node.filter_expression)
                    filter_exp = filter_exp.replace(self.object_name + '.', '')
                # ensure ones with added template tags work properly
                    if '|' in filter_exp:
                        filter_exp = filter_exp[:filter_exp.find('|')]
                    try:
                        schema_prop = schemaprop(self.obj, filter_exp)
                    except:
                        schema_prop = ""
                    index_offset = 1
                    prior_node_text = ''
                    while ("<" not in prior_node_text) and (index_offset <= index):
                        prior_node = node.nodelist[index - index_offset]
                        try:
                            prior_node_text = prior_node.s
                        except:
                            prior_node_text = ''
                    if prior_node_text:
                        cutter = prior_node_text.find('>')
                        prior_node.s = prior_node_text[:cutter] + ' ' + schema_prop + prior_node_text[cutter:]
            new_nodes.append(new_node)
            index = index + 1
        out = new_nodes.render(context)
        return out
        

    def render(self, context):
        self.obj = self.get_context_object(context)
        new_nodes = NodeList()
        variable_nodes = []
        for_nodes = []
        i = self.nodelist.__len__() - 1
        l = 0
        for_nodes = self.nodelist.get_nodes_by_type(ForNode)
        while l <= i:
            this_node = self.nodelist[l]
            node_class = this_node.__class__.__name__
            if node_class == "ForNode":
                #try to render them first
                this_node = TextNode(self.render_for_node(this_node, context))
            if node_class == "IfNode":
                this_node = TextNode(self.render_if_node(this_node, context))
            if node_class == 'TextNode':
                splitted = self.split_text_node(this_node.s)
                for item in splitted:
                    new_nodes.append(item)
            else:
                new_nodes.append(this_node)
                # variable_nodes list holds the indexes of all the
                # VariableNodes
            if node_class == "DebugVariableNode":
                variable_nodes.append(new_nodes.__len__() - 1)
            l = l + 1
         
        
        for item in variable_nodes:
            node_in_question = new_nodes[item]
            #print node_in_question
            schema_prop = ''
            if hasattr(node_in_question, 'filter_expression'):
                filter_exp = str(node_in_question.filter_expression)
                filter_exp = filter_exp.replace(self.object_name + '.', '')
                # ensure ones with added template tags work properly
                if '|' in filter_exp:
                    filter_exp = filter_exp[:filter_exp.find('|')]
                try:
                    schema_prop = schemaprop(self.obj, filter_exp)
                except:
                    # someone's snuck in a non-schema field, so lets just ignore it
                    pass
            if schema_prop:
                next_node_counter = 1
                next_node = new_nodes[item + next_node_counter]
                next_node_text = next_node.s
                while "<" not in next_node_text:
                    next_node_counter = next_node_counter + 1
                    next_node = new_nodes[item + next_node_counter]
                    next_node_text = next_node.s
                html_class = next_node_text[
                    next_node_text.find("<"):next_node_text.find(">") +
                    1]
                html_class = html_class.replace("/", "")
                html_class = html_class.replace(">", '')
                prior_node_counter = 1
                prior_node = new_nodes[item - prior_node_counter]
                prior_node_text = prior_node.s
                while html_class not in prior_node_text:
                    prior_node_counter = prior_node_counter + 1
                    prior_node = new_nodes[item - prior_node_counter]
                    if hasattr(prior_node, "s"):
                        prior_node_text = prior_node.s
                cutter = prior_node_text.find('>')
                prior_node.s = prior_node_text[
                    :cutter] + ' ' + schema_prop + prior_node_text[cutter:]
        scope = schemascope(self.obj)
        top_text = "<" + self.html_class + ' '
        if self.html_attribute:
            top_text = top_text + self.html_attribute + ' '
        top_text = top_text + ' itemscope itemtype=' + scope + '>'
        bottom_text = "</" + self.html_class + ">"
        topnode = TextNode(top_text)
        bottomnode = TextNode(bottom_text)
        new_nodes.insert(0, topnode)
        new_nodes.append(bottomnode)
        output = new_nodes.render(context)
        nl = []
        for node in new_nodes:
            result = node.render(context)
            nl.append(result)
        return ''.join(nl)
