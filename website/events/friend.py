from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from events.models import User, Comment, Event, Friends
import json, re

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
		#Friend has already been added
		if requested_friend in list_of_friends:
			return render(request, 'events/main.html', {'friends':"You've already added that friend"})
		else:
			#Friend has not yet been added. Add the new friend.
			list_of_friends.append(requested_friend)
			model_user_to_friend.friends = json.dumps(list_of_friends)
			model_user_to_friend.save()
			return render(request, 'events/main.html', {'friends':requested_friend + " added"})

def decodeList(list_of_something):
	jsonDec = json.decoder.JSONDecoder()
	return jsonDec.decode(list_of_something)

def view_friends(request):
	try:
		my_friends = Friends.objects.get(username=request.session['username'])
	except (KeyError, Friends.DoesNotExist):
		return render(request, 'events/friends.html', {'friends':'Sorry but you have no friends'})
	else:
		return render(request, 'events/friends.html', {'friends':parseFriends(my_friends.friends)})

def parseFriends(friends_list):
	parsed_list = []
	name = ""
	for char in friends_list:
		#Char is not " or ,
		if (char.isalpha()):
			name = name + char
		#Char is , then we end the name
		elif (char == ","):
			parsed_list.append(name)
			name = ""
		#Char is [ or ] or "
		else:
			continue
	parsed_list.append(name)
	return parsed_list

def remove_friend(request, friend):
	currentUser = User.objects.get(username=request.session['username'])

	try:
		model_user_to_friend = Friends.objects.get(username=currentUser)
		list_of_friends = decodeList(model_user_to_friend.friends)
	except (KeyError, Friends.DoesNotExist):
		return render(request, 'events/friends.html', {'friends':list_of_friends})
	else:
		list_of_friends.remove(friend)
		model_user_to_friend.friends = json.dumps(list_of_friends)
		model_user_to_friend.save()
	return render(request, 'events/friends.html', {'friends':list_of_friends})