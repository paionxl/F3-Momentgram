from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
 	url(r'^entry/$', views.entry, name='entry' ),
    url(r'^signUp/$', views.register, name='register'),
    url(r'^signIn/$', views.signIn, name='signIn')
]

