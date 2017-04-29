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
<<<<<<< HEAD
    url(r'accounts/login/$', django_cas_ng.views.login,name='cas_ng_login'),
    url(r'accounts/logout/$', django_cas_ng.views.logout,name='cas_ng_logout'),
    url(r'^accounts/callback$', django_cas_ng.views.callback, name='cas_ng_proxy_callback'),
=======
    url(r'accounts/login/$', django_cas_ng.views.login,name='login'),
    url(r'accounts/logout/$', django_cas_ng.views.logout,name='logout'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
>>>>>>> 7a80867b79668ce16c854e1657f05276fe2c6965
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
