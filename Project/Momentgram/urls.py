from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^init/$', views.init, name='init'),
    url(r'^done/$', views.register, name='register'),
    url(r'^signIn/$', views.signIn, name='signIn')
]

