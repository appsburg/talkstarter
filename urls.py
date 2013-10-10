from django.conf.urls import patterns, include, url
from talkstarter.views import EventList, EventDetail


urlpatterns = patterns('',
    url(r'^$', EventList.as_view(), name='event-list'),
    url(r'^(?P<pk>\d+)/$', EventDetail.as_view(), name='event-detail'),
)
