from django.shortcuts import render
from django.core.urlresolvers import reverse
from events.models import User, Comment, Event

def create(request):
	return render(request, 'events/create.html')

def create_event(request):
	try: 
		event = Event.objects.get(event_title=request.POST.get('event_title'))
	except (KeyError, Event.DoesNotExist):
		username = request.session["username"]
		event = Event(event_title=request.POST.get('event_title'), publisher=User.objects.get(username=username))
		event.save()
		return render(request, 'events/main.html', {'event_results':"Event successfully created"})
	else:
		return render(request, 'events/create.html', {'event_results':'Event name already in use. Please choose another'})