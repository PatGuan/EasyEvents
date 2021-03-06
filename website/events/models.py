from django.db import models
from django.utils import timezone
import json

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=15, primary_key=True)
	password = models.CharField(max_length=15)

	def __str__(self):
		return self.username

class Event(models.Model):
	publisher = models.ForeignKey(User)
	event_title = models.CharField(max_length=20)
	publish_date = timezone.now()

	def __str__(self):
		return self.event_title

class Comment(models.Model):
	publisher = models.ForeignKey(User)
	publish_date = timezone.now()
	comment_text = models.CharField(max_length=100)

	def __str__(self):
		return self.comment_text

class Friends(models.Model):
	username = models.ForeignKey(User)
	friends = models.CharField(max_length=15)

class Group(models.Model):
	host = models.ForeignKey(User)
	group_name = models.CharField(max_length=30)
	group_members = models.CharField(max_length=20)