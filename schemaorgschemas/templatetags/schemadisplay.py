from django import template
from django.template import Template, Context, Library, Variable, NodeList
from django.template.base import TemplateSyntaxError, TemplateDoesNotExist, \
    VariableNode, TextNode
from django.template.loader import render_to_string, get_template
from formatters import SchemaPropFormatter, EnumPropFormatter 

register = Library()



@register.simple_tag(takes_context=False)
def schemaprop(item, field_name=None):
    schema = None
    
    format_as = None
    magix = None
    if not field_name:
        raise TemplateSyntaxError('need to specify field name')
    if field_name[-8:]=='_display' and field_name[:4]=='get_':
            cut_name = field_name[4:-8]
            try:
                store_value = getattr(item, cut_name)
                field_name = cut_name
            except:
                print "SchemaError, field_name not in SchemaFields"
    try:
        store_value = getattr(item, field_name)
    except:
        print "SchemaError, field_name not in SchemaFields"
    schema = getattr(item.SchemaFields, field_name)
    format_as = schema._format_as
    if (schema._format_as == 'ForeignKey'):
        if (schema.traceback == True):
            f_obj = getattr(item, field_name)
            item_scope = schemascope(f_obj)
            store_value = item_scope
        else:
            format_as = 'default'
    if schema._format_as == 'enum':
        magix = EnumPropFormatter(schema=schema)
    if not magix:
        magix = SchemaPropFormatter(schema=schema)
    magix.format_as = format_as
    magix.value=store_value
    ret = magix.render()
    return ret


@register.simple_tag(takes_context=False)
def schemascope(item):
    ret = '"' + item.schema_url + '"'
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
    #defaults the HTML class to section unless over-ride specified
    section = 'section'
    htmlattr = None
    if token.count > 2:
        section = token[2]
    if token.count > 3:
        htmlattr = token[3]
        #remove quotes
        htmlattr = htmlattr[1:-1]
    rets = SchemaNode(nodelist, token[1], section, htmlattr)
    return rets


class SchemaNode(template.Node):
    def __init__(self, nodelist, object_name, html_class=None, html_attribute=None):
        self.nodelist = nodelist
        self.object_name = object_name
        self.html_class = html_class
        self.html_attribute = html_attribute
        for item in self.nodelist:
            print item

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
                item = TextNode(text_node_string[o_f + 1: f+1])
            output.append(item)
            if f == -1:
                return output

    def render(self, context):
        i = context.dicts.__len__() - 1  #going backwards as it seems the information is stored in the last list entry, but I'm not going to bank on it
        while i >= 0:
            dic = context.dicts[i]
            obj = dic.get(self.object_name, None)
            if obj:
                break
            i = i - 1
        if not obj:
            raise Exception(self.object_name + ' not found in template context')
        new_nodes = NodeList()
        variable_nodes = []
        i = self.nodelist.__len__() - 1
        l = 0
        while l <= i:
            this_node = self.nodelist[l]
            node_class = this_node.__class__.__name__
            if node_class == 'TextNode':
                    splitted = self.split_text_node(this_node.s)
                    for item in splitted:
                        new_nodes.append(item)
            else:
                
                new_nodes.append(this_node)
                #variable_nodes list holds the indexes of all the VariableNodes
                variable_nodes.append(new_nodes.__len__() - 1)
            l = l + 1
        for item in variable_nodes:
            node_in_question = new_nodes[item]
            filter_exp = str(node_in_question.filter_expression)
            filter_exp = filter_exp.replace(self.object_name + '.', '')
            #ensure ones with added template tags work properly
            if '|' in filter_exp:
                filter_exp = filter_exp[:filter_exp.find('|')]
            try:
                schema_prop = schemaprop(obj, filter_exp)
            except:
                #someone's snuck in a non-schema field, so lets just ignore it
                schema_prop = ''
            next_node_counter = 1
            next_node = new_nodes[item + next_node_counter]
            next_node_text = next_node.s
            while not "<" in next_node_text:
                next_node_counter = next_node_counter + 1
                next_node = new_nodes[item + next_node_counter]
                next_node_text = next_node.s
            html_class = next_node_text[next_node_text.find("<"):next_node_text.find(">") + 1]
            html_class = html_class.replace("/", "")
            html_class = html_class.replace(">", '')
            prior_node_counter = 1
            prior_node = new_nodes[item - prior_node_counter]
            prior_node_text = prior_node.s
            while not html_class in prior_node_text:
                prior_node_counter = prior_node_counter + 1
                prior_node = new_nodes[item - prior_node_counter]
                prior_node_text = prior_node.s
            cutter = prior_node_text.find('>')
            p_node_len = prior_node_text.__len__()
            prior_node.s = prior_node_text[:cutter] + ' ' + schema_prop + prior_node_text[cutter:]
        scope = schemascope(obj)
        top_text = "<" + self.html_class + ' '
        if self.html_attribute:
            top_text = top_text + self.html_attribute + ' '
        #itemscope itemtype
        top_text = top_text + ' itemscope itemtype=' + scope + '>'
        bottom_text = "</" + self.html_class + ">"
        topnode = TextNode(top_text)
        bottomnode = TextNode(bottom_text)
        new_nodes.insert(0, topnode)
        new_nodes.append(bottomnode)
        output = new_nodes.render(context)
        return output
