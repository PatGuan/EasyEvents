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
		# return HttpResponseRedirect(reverse('events:mainpage', args=(user.username,)))
		request.session['username'] = user.username
		return render(request, 'events/main.html', {'user': user})

def register(request):
	return render(request, 'events/register.html')

def register_user(request):
	try:
		user = User.objects.get(username=request.POST['username'])
	except (KeyError, User.DoesNotExist):
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

def addFriend(request, requested_friend):
	currentUser = User.objects.get(username=request.session['username'])

	try:
	 	model_user_to_friend = Friends.objects.get(username=currentUser)
	 	list_of_friends = decodeList(model_user_to_friend.friends)
	except (KeyError, Friends.DoesNotExist):
		#User has no friends, create a new list of friends
		new_friends = Friends(username=currentUser)
		list_of_friends = [requested_friend]
		new_friends.friends = json.dumps(list_of_friends)
		new_friends.save()
		return render(request, 'events/main.html', {'friends':requested_friend + " added"})
	else:
		list_of_friends.append(requested_friend)
		model_user_to_friend.friends = json.dumps(list_of_friends)
		model_user_to_friend.save()
		return render(request, 'events/main.html', {'friends':requested_friend + " added"})

def decodeList(list_of_something):
	jsonDec = json.decoder.JSONDecoder()
	return jsonDec.decode(list_of_something)