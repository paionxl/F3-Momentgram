from django.conf.urls import url
from django.conf.urls.static import static

from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^init/$', views.init, name='init'),
    url(r'^done/$', views.register, name='register')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
