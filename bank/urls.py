from django.conf.urls import patterns, url
from bank import views

urlpatterns = patterns('',
        url(r'^api/branches/autocomplete/$', views.possible_matches, name='possible_matches'),
        url(r'^api/branches/$', views.all_possible_matches, name='all_possible_matches'),

)
