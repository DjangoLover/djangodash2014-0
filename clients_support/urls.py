# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import viewsets, routers
from clients_support.models import Ticket, Message, StatusLog, TicketType, Tag


class TicketViewSet(viewsets.ModelViewSet):
    model = Ticket


class MessageViewSet(viewsets.ModelViewSet):
    model = Message


router = routers.DefaultRouter()
router.register(r'tickets', TicketViewSet)
router.register(r'messages', MessageViewSet)


def clients_support_urls():
    return (
        url(r'^autocomplete/', include('autocomplete_light.urls')),
        url('^clients_support/', include(router.urls)),
    )