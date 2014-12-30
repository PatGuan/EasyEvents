from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=15)
	password = models.CharField(max_length=15)

	def __str__(self):
		return self.username

class Event(models.Model):
	publisher = models.ForeignKey(User)
	event_title = models.CharField(max_length=20)
	publish_date = timezone.now()

	def __str__(self):
		return event_title

class Comment(models.Model):
	publisher = models.ForeignKey(User)
	#publish_date = models.DateTimeField('date published')
	publish_date = timezone.now()
	comment_text = models.CharField(max_length=100)

	def __str__(self):
		return comment_text