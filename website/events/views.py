from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from events.models import User, Comment, Event, Friends
import json


# Create your views here.
def index(request):
	return render(request, 'events/index.html')


#Functions related to the login/register page
def login(request):

	try:
		user = User.objects.get(username=request.POST['username'])
	except (KeyError, User.DoesNotExist):
		return render(request, 'events/main.html', {'loginfail': "Username not found"})
	else:
		#Login successful. Store the username in a session.
		request.session['username'] = user.username
		return render(request, 'events/main.html', {'user': user})


def register(request):
	return render(request, 'events/register.html')


#Function responsible for creating the user and storing it in the database
def register_user(request):

	try:
		user = User.objects.get(username=request.POST['username'])
	except (KeyError, User.DoesNotExist):
		#The user does not exist. In this case, create the user
		user = User(username=request.POST['username'], password=request.POST['password'])
		user.save()
		request.session['username'] = user.username
		return render(request, 'events/main.html')
	else:
		return render(request, 'events/register.html', {'loginfail':"Username already taken. Please choose another"})


def search(request):
	search_results = User.objects.all().filter(username__startswith=
				request.POST.get('searchinput')
				)
	if not search_results:
		return render(request, 'events/main.html', {'results': "No user by that name"})
	else:
		return render(request, 'events/main.html', {'results':search_results})

def view_groups(request):
	return render(request, 'events/groups.html')


def logout(request):
	del request.session['username']
	return render(request, 'events/index.html')