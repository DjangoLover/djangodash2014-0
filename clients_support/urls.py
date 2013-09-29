# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import viewsets, routers
from clients_support.conf import settings
from clients_support.models import Ticket, Message


class TicketViewSet(viewsets.ModelViewSet):
    model = Ticket


class MessageViewSet(viewsets.ModelViewSet):
    model = Message


router = routers.DefaultRouter()
router.register(r'tickets', TicketViewSet)
router.register(r'messages', MessageViewSet)


def clients_support_urls():

    urls = url('^clients_support/', include(router.urls)),

    if settings.INCLUDE_AUTOCOMPLETE_LIGHT_URLS:
        urls += url(r'^autocomplete/', include('autocomplete_light.urls')),

    return urls