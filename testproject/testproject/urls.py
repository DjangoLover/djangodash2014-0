# coding=utf-8

from django.conf import settings
from django.conf.urls import patterns, include, url
from index.views import IndexView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin

from clients_support.urls import clients_support_urls

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

# Add django-clients-support urls
urlpatterns += clients_support_urls()