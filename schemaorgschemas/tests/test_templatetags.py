import os
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth.tests.utils import skipIfCustomUser
from django.template import Template, Context, TemplateSyntaxError
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime
from django.views.generic import DetailView
from schemaorgschemas.Thing.CreativeWork import Book as book
from schemaorgschemas.Thing import CreativeWork
from schemaorgschemas.Thing.Intangible.Enumeration import BookFormatType
from schemaorgschemas.Thing import Person
from schemaorgschemas.Thing import Organization
from schemaorgschemas.Thing import Action
from django.db.models.fields.related import ForeignKey


class Author(models.Model, Person.PersonSchema):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

    def get_absolute_url(self):
        return ("/test/author/%s" % self.pk) 

    class SchemaFields():
        first_name = Person.givenNameProp()
        last_name = Person.familyNameProp()
        email = Person.emailProp()

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class Publisher(models.Model, Organization.OrganizationSchema):
    name = models.CharField(max_length=30)
    website = models.URLField()
    suddenly_stopped = models.DateTimeField(blank=True)
    non_schema_field = models.CharField(max_length="5", blank=True)


    def get_absolute_url(self):
        return ("/test/publisher/%s" % self.pk) 

    def __unicode__(self):
        return self.name

    class SchemaFields():
        name = Organization.nameProp()
        website = Organization.urlProp()
        #a testing hack, there aren't any relevant publisher related datetime properties 
        suddenly_stopped = Action.endTimeProp()


class Book(models.Model, book.BookSchema):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    book_format = models.TextField(choices=BookFormatType.BOOKFORMAT_CHOICES)
    publisher = ForeignKey(Publisher)
    publication_date = models.DateField(blank=True)
    family_friendly = models.BooleanField()


    def get_absolute_url(self):
        return ("/test/book/%s" % self.pk) 

    class SchemaFields():
        authors = book.authorProp()
        title = book.headlineProp()
        book_format = BookFormatType.bookFormatProp()
        publisher = book.publisherProp()
        publication_date = book.datePublishedProp()
        family_friendly = CreativeWork.isFamilyFriendlyProp()

    def __unicode__(self):
        return self.title


class SchemaTemplateTagTester(TestCase):
    def setUp(self):
        test_date_time = datetime(2000, 1, 1, 1, 1, 1)
        pub_a = Publisher.objects.create(name="publisher a", website="http://example.com/a/", suddenly_stopped=test_date_time, non_schema_field="Tests")
        pub_b = Publisher.objects.create(name="publisher b", website="http://example.com/b/")
        auth_a = Author.objects.create(first_name="Albert", last_name="Abba", email="albertabba@example.com")
        auth_b = Author.objects.create(first_name="Brian", last_name="Bubba", email="brianbubba@example.com")
        book_a = Book.objects.create(title="A for Apple", book_format='EBOOK', publisher=pub_a, publication_date='1999-12-31', family_friendly=True)
        book_a.authors.add(auth_a.pk, auth_b.pk)
        book_b = Book.objects.create(title="B for Banana", book_format='HARDCOVER', publisher=pub_b, publication_date='2013-12-31', family_friendly=False)
        book_b.authors.add(auth_a.pk)


    def test_item_scope(self):
        out = Template("{% load schemadisplay %}"
                       """<section itemscope itemtype={% schemascope object %}></section>"""
                       ).render(Context({'object': Publisher.objects.get(id=1)}))
        expected_string = """<section itemscope="" itemtype="http://schema.org/Organization" link="/test/publisher/1"></section>"""

        self.assertEqual(out, expected_string)

    def test_datatype_boolean(self):
        out = Template("{% load schemadisplay %}"
                       """<p {% schemaprop object 'family_friendly' %}>boolean:{{object.family_friendly}} </p>"""
                       ).render(Context({'object': Book.objects.get(id=1)}))
        expected_string = """<p itemprop="isFamilyFriendly">boolean:True </p>"""
        self.assertEqual(out,expected_string)

    def test_datatype_date(self):
        out = Template("{% load schemadisplay %}"
                       """<p {% schemaprop object 'publication_date' %}>date: {{object.publication_date}}</p>"""
                       ).render(Context({'object': Book.objects.get(id=1)}))
        expected_string = """<p itemprop="datePublished" datetime="1999-12-31">date: Dec. 31, 1999</p>"""
        self.assertEqual(out,expected_string)


    def test_datatype_datetime(self):
        out = Template("{% load schemadisplay %}"
                       """<p {% schemaprop object 'suddenly_stopped' %}>time:{{object.suddenly_stopped}}</p>"""
                       ).render(Context({'object': Publisher.objects.get(id=1)}))
        expected_string = """<p itemprop="endTime" datetime="2000-01-01T01:01:01-06:00">time:Jan. 1, 2000, 1:01 a.m.</p>"""
        self.assertEqual(out,expected_string)

    def test_datatype_number(self):
        out = Template("{% load schemadisplay %}"
                       """<p {% schemaprop object 'copyright_year' %}>integer: {{object.copyright_year}}</p>"""
                       ).render(Context({'object': Book.objects.get(id=1)}))
        expected_string = """<p itemprop="copyrightYear">integer: 2014</p>"""
        self.assertEqual(out,expected_string)

    def test_datatype_text(self):
        out = Template("{% load schemadisplay %}"
                       """<p {% schemaprop object 'title' %}>text: {{object.title}}</p>"""
                       ).render(Context({'object': Book.objects.get(id=1)}))
        expected_string = """<p itemprop="headline">text: A for Apple</p>"""
        self.assertEqual(out,expected_string)

    def test_datatype_time(self):
        pass

    def test_enum_field(self):
        pass

    def test_ennm_field_with_adapter(self):
        pass

    def test_manytomany(self):
        pass

    def test_foreignkey(self):
        pass

    def test_set_all(self):
        pass

