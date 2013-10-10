from django.contrib import admin
from django.contrib.admin import ModelAdmin
from talkstarter.models import *

class EventAdmin(ModelAdmin):
	list_display = ['title', 'date', 'operator', 'minimum_backers', 'backing_percentage', 'is_backed',]

admin.site.register(Operator)
admin.site.register(Event, EventAdmin)
admin.site.register(Backer)
admin.site.register(Subscription)