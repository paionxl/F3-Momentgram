from django.conf.urls import url

from django.contrib import admin
from . import views
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    url(r'^$', views.index, name='init'),
    url(r'^login/$', views.signIn, name='login'),
    url(r'^signup/$', views.register, name='signup'),
    url(r'^signup/done/$', views.register, name='doner'),
    url(r'^login/done/$', views.signIn, name='donel'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^post/$', views.publish_post, name='publish')

    #path('admin/', admin.site.urls),
    #path('', include('posts.urls'))

]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

