from django.shortcuts import render
from django.core.urlresolvers import reverse
from events.models import User, Comment, Event, Friends
import json, re