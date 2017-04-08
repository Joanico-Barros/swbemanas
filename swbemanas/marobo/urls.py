from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^mapamarobo/$', views.Mapa.as_view(), name='mapamarobo'),
]
