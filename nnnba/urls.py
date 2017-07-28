from django.conf.urls import url

from . import views

app_name = 'nnnba'

urlpatterns = [
    url(r'^$', views.main, name='main'), 
    url(r'^(?P<player_id>[0-9]+)/$', views.player, name='player'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
