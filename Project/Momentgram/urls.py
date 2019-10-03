from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^init/$', views.init, name='init'),
    url(r'^signup/$', views.register, name='signup'),
    url(r'^done/$', views.register, name='register')
]

