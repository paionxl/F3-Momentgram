from django.conf.urls import url

from django.contrib import admin
from . import views
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new



urlpatterns = [
    url(r'^$', views.index, name='index'),
 	url(r'^entry/$', views.entry, name='entry' ),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.signIn, name='login'),
    url(r'^logout/$', views.logout, name='logout')
]

#if settings.DEBUG: # new
   # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
