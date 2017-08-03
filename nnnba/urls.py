from django.conf.urls import url, include
from rest_framework import routers

from . import views


app_name = 'nnnba'

router = routers.DefaultRouter()
router.register(r'api/coef', views.CoefViewSet, base_name="coef")

urlpatterns = [
    url(r'^$', views.main, name='main'), 
    url(r'^', include(router.urls, namespace="api")),
    url(r'^(?P<player_id>[0-9]+)/$', views.player_stats, name='player_stats'),
    url(r'^(?P<player_id>[0-9]+)/(?P<model_name>[a-zA-Z\s]+)/$', views.player_worth, name='player_worth'),
    url(r'^(?P<model_name>[a-zA-Z\s]+)/$', views.model_details, name='model_details'),
]
