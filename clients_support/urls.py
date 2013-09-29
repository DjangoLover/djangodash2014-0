# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from clients_support.conf import settings
from rest_framework import routers
from clients_support.views import TicketViewSet, MessageViewSet, TicketTypeViewSet


router = routers.DefaultRouter()
router.register(r'tickets', TicketViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'ticket_types', TicketTypeViewSet)

def clients_support_urls():
    urls = url('^clients_support/', include(router.urls)),

    if settings.INCLUDE_AUTOCOMPLETE_LIGHT_URLS:
        urls += url(r'^autocomplete/', include('autocomplete_light.urls')),

    return urls
