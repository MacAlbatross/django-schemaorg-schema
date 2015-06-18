#Schema.org schemas for Django
##Easily add HTML schema mark up to Django models

This application provides mixins for Django models and template tags that format their values according to the schema.org specificiations.

A specimin models.py would be:

from django.core.urlresolvers import reverse
from django.db import models

from schemaorgschemas.Thing import Organization
from schemaorgschemas.Thing.CreativeWork import Book as BookSch
from schemaorgschemas.Thing.Intangible.Enumeration import BookFormatType
from schemaorgschemas.Thing.Intangible.StructuredValue.ContactPoint import PostalAddress,\
    emailProp
from schemaorgschemas.Thing.Person import PersonSchema, givenNameProp,\
    familyNameProp


class Address(models.Model, PostalAddress.PostalAddressSchema):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=40)
    country = models.CharField(max_length=50)

    class SchemaFields():
        street_address = PostalAddress.streetAddressProp()
        city = PostalAddress.addressLocalityProp()
        state_province = PostalAddress.addressRegionProp()
        postal_code = PostalAddress.postalCodeProp()
        country = PostalAddress.addressCountryProp()

    def __unicode__(self):
        return self.street_address


class Publisher(models.Model, Organization.OrganizationSchema):
    name = models.CharField(max_length=30)
    address = models.ForeignKey(Address)
    website = models.URLField()

    def get_absolute_url(self):
        return reverse('publisher', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name

    class SchemaFields():
        name = Organization.nameProp()
        address = Organization.addressProp(traceback=False)
        website = Organization.urlProp()


class Author(models.Model, PersonSchema):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

    def get_absolute_url(self):
        return reverse('author', kwargs={'pk': self.pk})

    class SchemaFields():
        first_name = givenNameProp()
        last_name = familyNameProp()
        email = emailProp()

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class Book(models.Model, BookSch.BookSchema):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    cover = models.ImageField(upload_to='images/', blank=True)

    def get_absolute_url(self):
        return reverse('book', kwargs={'pk': self.pk})

    class SchemaFields():
        authors = BookSch.authorProp()
        title = BookSch.headlineProp()
        publisher = BookSch.publisherProp()
        publication_date = BookSch.datePublishedProp()
        cover = BookSch.imageProp()

    def __unicode__(self):
        return self.title

and the author_detail.html template would be

{% load schemadisplay %}
{% block content %}
{% schemaobject object section "class='author'" "author" %}
<span>{{object.first_name}}</span>&nbsp;<span>{{object.last_name}}</span>
{% if object.email %}
<p>email:{{object.email}}</p>
{% endif %}
<table>
{% for book in object.book_set.all %}
{% schemaobject book tr "" "book" %}
<td>{{book.title}}</td>
<td>{{book.publication_date}}</td>
{% endschemaobject %}
{% endfor %}
</table>
{% endschemaobject %}
{% endblock %}

which will produce the following output:

<section class='author' id="#author3" itemscope itemtype="http://schema.org/Person" link="http://localhost/demo/author/3/">
<span itemprop="givenName">Allen</span>&nbsp;<span itemprop="familyName">Downey</span>
<table>
<tr  id="#book3" itemscope itemtype="http://schema.org/Book" link="http://localhost/demo/book/3/">
<td itemprop="headline">Think Python</td>
<td itemprop="datePublished" datetime="2014-09-08">Sept. 8, 2014</td>
</tr>
<tr  id="#book4" itemscope itemtype="http://schema.org/Book" link="http://localhost/demo/book/4/">
<td itemprop="headline">Think Complexity</td>
<td itemprop="datePublished" datetime="2012-02-01">Feb. 1, 2012</td>
</tr>
</table>
</section>

filled with correctly formatted schema.org markup.