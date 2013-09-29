# -*- coding: utf-8 -*-
import autocomplete_light

from django.conf import settings
from django.conf.urls import patterns, include, url
from index.views import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin

from clients_support.urls import clients_support_urls
autocomplete_light.autodiscover()
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', index, name='index'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

# Add django-clients-support urls
urlpatterns += clients_support_urls()