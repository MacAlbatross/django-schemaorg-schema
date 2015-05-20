import os
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth.tests.utils import skipIfCustomUser
from django.template import Template, Context, TemplateSyntaxError
from django.test import TestCase
from django.core.urlresolvers import reverse
from datetime import datetime
from django.views.generic import DetailView
from .models import Author, Book, Publisher, Site


class SchemaTemplateTagTests(TestCase):
    def setUp(self):
        site = Site.objects.create(domain="http://example.com", name="example")
        test_date_time = datetime(2000, 1, 1, 1, 1, 1)
        pub_a = Publisher.objects.create(name="publisher a", website="http://example.com/a/", suddenly_stopped=test_date_time, non_schema_field="Tests")
        pub_b = Publisher.objects.create(name="publisher b", website="http://example.com/b/")
        auth_a = Author.objects.create(first_name="Albert", last_name="Abba", email="albertabba@example.com")
        auth_b = Author.objects.create(first_name="Brian", last_name="Bubba", email="brianbubba@example.com")
        book_a = Book.objects.create(title="A for Apple", book_format='EBOOK', publisher=pub_a, publication_date='1999-12-31', copyright_year=1999, family_friendly=True)
        book_a.authors.add(auth_a.pk, auth_b.pk)
        book_b = Book.objects.create(title="B for Banana", book_format='HARDCOVER', publisher=pub_b, publication_date='2013-12-31', copyright_year=2013, family_friendly=False)
        book_b.authors.add(auth_a.pk)

    def test_item_scope(self):
        out = Template("{% load schemadisplay %}"
                       """<section itemscope itemtype={% schemascope object %}></section>"""
                       ).render(Context({'object': Publisher.objects.get(id=1)}))
        expected_string = """<section itemscope itemtype="http://schema.org/Organization" link="http://example.com/test/publisher/1"></section>"""
        self.assertEqual(out, expected_string)

    def test_datatype_boolean(self):
        out = Template("{% load schemadisplay %}"
                       """<p {% schemaprop object 'family_friendly' %}>boolean:{{object.family_friendly}} </p>"""
                       ).render(Context({'object': Book.objects.get(id=1)}))
        expected_string = """<p itemprop="isFamilyFriendly">boolean:True </p>"""
        self.assertEqual(out, expected_string)

    def test_datatype_date(self):
        out = Template("{% load schemadisplay %}"
                       """<p {% schemaprop object 'publication_date' %}>date: {{object.publication_date}}</p>"""
                       ).render(Context({'object': Book.objects.get(id=1)}))
        expected_string = """<p itemprop="datePublished" datetime="1999-12-31">date: Dec. 31, 1999</p>"""
        self.assertEqual(out, expected_string)

    def test_datatype_datetime(self):
        out = Template("{% load schemadisplay %}"
                       """<p {% schemaprop object 'suddenly_stopped' %}>time:{{object.suddenly_stopped}}</p>"""
                       ).render(Context({'object': Publisher.objects.get(id=1)}))
        expected_string = """<p itemprop="endTime" datetime="2000-01-01T01:01:01">time:Jan. 1, 2000, 1:01 a.m.</p>"""
        self.assertEqual(out, expected_string)

    def test_datatype_number(self):
        out = Template("{% load schemadisplay %}"
                       """<p {% schemaprop object 'copyright_year' %}>integer: {{object.copyright_year}}</p>"""
                       ).render(Context({'object': Book.objects.get(id=1)}))
        expected_string = """<p itemprop="copyrightYear">integer: 1999</p>"""
        self.assertEqual(out, expected_string)

    def test_datatype_text(self):
        out = Template("{% load schemadisplay %}"
                       """<p {% schemaprop object 'title' %}>text: {{object.title}}</p>"""
                       ).render(Context({'object': Book.objects.get(id=1)}))
        expected_string = """<p itemprop="headline">text: A for Apple</p>"""
        self.assertEqual(out, expected_string)

    def test_datatype_time(self):
        pass

    def test_enum_field(self):
        out = Template("{%load schemadisplay %}"
                       """<p {% schemaprop object 'book_format' %}>Format: {{object.book_format}}</p>"""
                       ).render(Context({'object': Book.objects.get(id=1)}))
        expected_string = """<p itemprop="bookFormat" href="http://schema.org/EBook">Format: EBOOK</p>"""
        self.assertEqual(out, expected_string)

    def test_ennm_field_with_adapter(self):
        pass

    def test_set_all(self):
        out = Template("{%load schemadisplay %}"
                       """{% schemaobject object section "class='author'" "author" %}<span>{{object.first_name}}</span>&nbsp;<span>{{object.last_name}}</span>"""
                       """<table>{% for book in object.book.set_all %}<tr><td>{{book.title}}</td><td>{{book.publication_date}}</td></tr>{% endfor %}</table>"""
                       """{% endschemaobject %}"""
                       ).render(Context({'object': Author.objects.get(id=1)}))
        expected_string = """<section class='author' id="#author1" itemscope itemtype="http://schema.org/Person" link="http://example.com/test/author/1"><span>Albert</span>&nbsp;<span>Abba</span><table><tr  itemscope itemtype="http://schema.org/Book" link="http://example.com/test/book/1"><td>A for Apple</td><td>Dec. 31, 1999</td></tr><tr  itemscope itemtype="http://schema.org/Book" link="http://example.com/test/book/2"><td>B for Banana</td><td>Dec. 31, 2013</td></tr></table></section>"""
        self.assertEqual(out, expected_string)
