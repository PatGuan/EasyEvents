from django.conf.urls import patterns, url
from events import views, eventview, friend, group

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^login/', views.login, name='login'),
	url(r'^register/', views.register, name='register'),
	url(r'^register_user/', views.register_user, name='register_user'),
	url(r'^search/', views.search, name='search'),
	url(r'^create/', eventview.create, name='create'),
	url(r'^create_event/', eventview.create_event, name='create_event'),
	url(r'^addFriend/(?P<requested_friend>\w+)/$', friend.addFriend, name='addFriend'),
	url(r'^viewfriends/', friend.view_friends, name="viewfriends"),
	url(r'^removeFriend/(?P<friend>\w+)/$', friend.remove_friend, name='removeFriend'),
	url(r'^groups/', views.view_groups, name='view_groups'),
	url(r'^logout/', views.logout, name="logout"),
	url(r'^creategroup/<?P<group_title>\w+)/$', group.create_group, name="creategroup"),
	)