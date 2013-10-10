from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from talkstarter.models import Event


class EventList(ListView):
	model = Event

class EventDetail(DetailView):
	model = Event
