from django.db import models

class Operator(models.Model):
	"""
	A person or group fronting an event.
	"""
	name = models.CharField(max_length=255)
	description = models.TextField()
	link = models.URLField()
	image = models.ImageField(upload_to="operator_images/")


class Event(models.Model):
	"""
	An event to be voted for.
	"""
	title = models.CharField(max_length=255)
	description = models.TextField()
	date = models.DateField()
	operator = models.ForeignKey(Operator)


class Backer(models.Model):
	"""
	A person who invested into an event.
	"""
	email = models.EmailField()
	twitter_handle = models.CharField(max_length=255)
	comment = models.TextField()
	event = models.ForeignKey(Event)


class Subscription(models.Model):
	"""
	A person who is interested in future events.
	"""
	email = models.EmailField()