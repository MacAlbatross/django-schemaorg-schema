from django.db import models
from django.db.models.fields.related import ForeignKey
from schemaorgschemas.Thing.CreativeWork import Book as book
from schemaorgschemas.Thing import CreativeWork
from schemaorgschemas.Thing.Intangible.Enumeration import BookFormatType
from schemaorgschemas.Thing import Person
from schemaorgschemas.Thing import Organization
from schemaorgschemas.Thing import Action


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
    suddenly_stopped = models.DateTimeField(blank=True, null=True)
    non_schema_field = models.CharField(max_length="5", blank=True)

    def get_absolute_url(self):
        return ("/test/publisher/%s" % self.pk)

    def __unicode__(self):
        return self.name

    class SchemaFields():
        name = Organization.nameProp()
        website = Organization.urlProp()
        # a testing hack, there aren't any relevant publisher related datetime properties
        suddenly_stopped = Action.endTimeProp()


class Book(models.Model, book.BookSchema):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    book_format = models.TextField(choices=BookFormatType.BOOKFORMAT_CHOICES)
    publisher = ForeignKey(Publisher)
    publication_date = models.DateField(blank=True)
    family_friendly = models.BooleanField()
    copyright_year = models.IntegerField()

    def get_absolute_url(self):
        return ("/test/book/%s" % self.pk)

    class SchemaFields():
        authors = book.authorProp()
        title = book.headlineProp()
        book_format = BookFormatType.bookFormatProp()
        publisher = book.publisherProp()
        publication_date = book.datePublishedProp()
        family_friendly = CreativeWork.isFamilyFriendlyProp()
        copyright_year = book.copyrightYearProp()

    def __unicode__(self):
        return self.title