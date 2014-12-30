from django.contrib import admin
from events.models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Comment)
