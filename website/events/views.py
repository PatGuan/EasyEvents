from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from events.models import User, Comment, Event


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
		return render(request, 'events/main.html', {'user':user})
	else:
		return render(request, 'events/register.html', {'loginfail':"Username already taken. Please choose another"})

def search(request):
	# search_results = User.objects.all().filter(username=request.POST.get['search_input'])
	try:
		search_results = User.objects.all().filter(username__startswith=
			# username=request.POST.get('searchinput')
			request.POST.get('searchinput')
			)
	except (KeyError, User.DoesNotExist):
		results = User.objects.all()
		return render(request, 'events/main.html', {'results': "No user by that name"})
	else:
		return render(request, 'events/main.html', {'results':search_results})