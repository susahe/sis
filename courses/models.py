from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Course(models.Model):
	code = models.CharField(max_length=10,unique=True)
	name = models.CharField(max_length=128)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	fees = models.DecimalField(max_digits=6, decimal_places=2)
	slug = models.SlugField()
	
	def save(self, *args, **kwargs):
            # Uncomment if you don't want the slug to change every time the name changes
            #if self.id is None:
                    #self.slug = slugify(self.name)
			self.slug = slugify(self.name)
			super(Course, self).save(*args, **kwargs)
	
	@property
	def fees(self):
		return "Rs.%s" % self.fees
	
	def __unicode__(self):
		return self.name

		
class Topic(models.Model):
	course = models.ForeignKey(Course)
	code = models.CharField(max_length=5,unique=True)
	name = models.CharField(max_length=128)
	
	
	def __unicode(self):
		return self.name 
		
class CourseGroup(models.Model):
	course = models.ForeignKey(Course)
	user = models.ForeignKey(User)
	name = name = models.CharField(max_length=128)
	
	def __unicode(self):
		return self.name 