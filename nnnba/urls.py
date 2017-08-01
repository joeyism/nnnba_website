from django.conf.urls import url

from . import views

app_name = 'nnnba'

urlpatterns = [
    url(r'^$', views.main, name='main'), 
    url(r'^(?P<player_id>[0-9]+)/$', views.player_stats, name='player_stats'),
    url(r'^(?P<player_id>[0-9]+)/(?P<model_name>[a-zA-Z\s]+)/$', views.player_worth, name='player_worth'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
