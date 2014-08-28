#Schema.org schemas for Django
##Easily add HTML schema mark up to Django models

This application provides mixins for Django models and template tags that format their values according to the schema.org specificiations.

A specimin models.py would be:

	from django.db import models
	from django.core.urlresolvers import reverse
	from django.contrib.auth.models import User
	from schemaorgschemas.Thing.CreativeWork import WebPage
	from django.db.models.fields import CharField, TextField, DateField
	from schemaorgschemas.Thing.Person import PersonSchema, givenNameProp, familyNameProp
	from django.db.models.fields.related import ForeignKey


	class Author(models.Model, PersonSchema):
		user = ForeignKey(User)
		forename = CharField(max_length=200)
		surname = CharField(max_length=200)

		def __unicode__(self):
			return self.forename + ' ' + self.surname

		def get_absolute_url(self):
			return reverse('author', kwargs={'pk': self.pk})

		class SchemaFields():
			forename = givenNameProp()
			surname = familyNameProp()


	class Blog(models.Model, WebPage.WebPageSchema):
		title = CharField(max_length=250)
		sub_title = TextField()
		date_published = DateField(null=True)
		last_updated = DateField(auto_now=True)
		content = TextField()
		keywords = TextField()
		author = ForeignKey(Author)

		def __unicode__(self):
			return self.title

		def get_absolute_url(self):
			return reverse('blog', kwargs={'pk': self.pk})

		class SchemaFields():
			title = WebPage.headlineProp()
			sub_title = WebPage.alternativeHeadlineProp()
			date_published = WebPage.datePublishedProp()
			last_updated = WebPage.dateModifiedProp()
			content = WebPage.textProp()
			keywords = WebPage.keywordsProp()
			author = WebPage.creatorProp()

and the blog_list.html template would be

	{% load schemadisplay %}
	<html>
	<body>
	{% for object in object_list %}
	{% schemaobject object section 'class="blog"' %}
		<hgroup>
			<h3>Published: {{object.date_published}}</h3>
			<h1>Title: {{object.title}}</h1>
			<h2>{{object.sub_title}}</h2>
			<h4>{{object.author}}</h4>
		</hgroup>
		<div>{{object.content|truncatewords:30}}</div>
	{% endschemaobject %}
	{% endfor %}
	</body>
	</html>

which will produce the following output:
	<html>
			<body>
				
				<section class="extrastuff"  itemscope itemtype="http://schema.org/WebPage" link="http://paulfleetwood.co.uk/blog/1/" >
				<hgroup>
				<h3 itemprop="datePublished" datetime="2014-07-10">Published: July 10, 2014 because this hasn't been checked</h3>
				<h1 itemprop="headline">Title: Schema.org schema for django</h1>
				<h2 itemprop="alternativeHeadline">Providing all properties for schema.org in discrete modules</h2>
				<h4 itemscope itemtype="http://schema.org/Person" link="http://paulfleetwood.co.uk/blog/author/1/">Paul Fleetwood</h4>
				</hgroup>
				<div ><p>In simple terms this simply provides access to the data models scraped off the schema.org website, using a template tag ...</div>
				</section>
				
			</body>
	</html>