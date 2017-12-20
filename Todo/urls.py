from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='Todo'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details, name='details'),
    url(r'^add', views.add, name='add'),
    url(r'^delete', views.delete, name='delete'),
]
