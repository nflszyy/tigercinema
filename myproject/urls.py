from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
import django_cas_ng.views

from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myapp/', include('myproject.myapp.urls')),
    url(r'^$', RedirectView.as_view(url='/myapp/welcome/', permanent=False)),
    url(r'^accounts/login/$', 'django_cas.views.login',name='login'),
    url(r'^accounts/logout/$', 'django_cas.views.logout',name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
