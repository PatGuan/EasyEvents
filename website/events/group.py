from django.shortcuts import render
from django.core.urlresolvers import reverse
from events.models import User, Comment, Event, Friends, Group
import json, re

def create_group(request):
	try:
		group_title = request.POST['grouptitle']
		group = Group.objects.get(group_name=group_title)
	except (KeyError, Group.DoesNotExist):
		#Group doesn't exist. Create it.
		user = User.objects.get(username=request.session['username'])
		group = Group(host=user, group_name=group_title)
		group.save()
		return render(request, 'events/main.html', {'event_results': 'Group successfully created!'})
	else:
		return render(request, 'events/groups.html', {'result':'Group name already taken! Choose another'})