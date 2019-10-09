from django.conf.urls import url

from django.contrib import admin
from . import views
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^init/$', views.init, name='init'),
    url(r'^done/$', views.register, name='register')
   # path('admin/', admin.site.urls),
    #path('', include('posts.urls'))
]

#if settings.DEBUG: # new
   # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
