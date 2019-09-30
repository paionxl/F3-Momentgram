from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hola/$', views.index, name='hola'),
    url(r'^init/$', views.init, name='init')
]

