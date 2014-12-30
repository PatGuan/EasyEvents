from django.conf.urls import patterns, url
from events import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^login/', views.login, name='login'),
	url(r'^register/', views.register, name='register'),
	url(r'^register_user/', views.register_user, name='register_user')
	)