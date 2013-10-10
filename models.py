from math import floor
from datetime import timedelta
from django.db import models

class Operator(models.Model):
	"""
	A person or group fronting an event.
	"""
	name = models.CharField(max_length=255)
	description = models.TextField()
	link = models.URLField(blank=True, null=True)
	image = models.ImageField(upload_to="operator_images/")
	twitter_handle = models.CharField(max_length=255, blank=True, null=True)

	def __unicode__(self):
		return self.name


class Event(models.Model):
	"""
	An event to be voted for.
	"""
	title = models.CharField(max_length=255)
	description = models.TextField()
	date = models.DateTimeField()
	operator = models.ForeignKey(Operator)
	minimum_backers = models.IntegerField(default=5)

	@property
	def is_backed(self):
		return self.backer_set.count() >= self.minimum_backers

	@property
	def backing_percentage(self):
		backer_count = self.backer_set.count()
		if backer_count >= self.minimum_backers:
			return 100

		if backer_count == 0:
			return 0

		return int(floor(float(backer_count) / self.minimum_backers * 100))

	@property
	def backable_until(self):
		two_weeks = timedelta(weeks = 2)
		return self.date - two_weeks

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['date',]


class Backer(models.Model):
	"""
	A person who invested into an event.
	"""
	name = models.CharField(max_length=255, blank=True, null=True)
	email = models.EmailField()
	twitter_handle = models.CharField(max_length=255, blank=True, null=True)
	comment = models.TextField()
	event = models.ForeignKey(Event)

	def __unicode__(self):
		return self.email


class Subscription(models.Model):
	"""
	A person who is interested in future events.
	"""
	email = models.EmailField()

	def __unicode__(self):
		return self.email