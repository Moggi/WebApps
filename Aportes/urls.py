from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mensal_fixo', views.mensal_fixo, name='mensal_fixo'),
    url(r'^mensal_progressivo', views.mensal_progressivo, name='mensal_progressivo'),
]
