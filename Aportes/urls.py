from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='Aportes'),
    url(r'^mensal', views.mensal, name='mensal'),
    url(r'^projeto', views.projeto, name='projeto'),
]
