from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.init, name='init'),
    url(r'^login/$', views.signIn, name='login'),
    url(r'^signup/$', views.register, name='signup'),
    url(r'^signup/done/$', views.register, name='doner'),
    url(r'^login/done/$', views.signIn, name='donel')

]
