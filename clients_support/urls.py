# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework import routers
from clients_support.views import TicketViewSet, MessageViewSet, TicketTypeViewSet


router = routers.DefaultRouter()
router.register(r'tickets', TicketViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'ticket_types', TicketTypeViewSet)

def clients_support_urls():
    """ Return clients_support urls """
    return (url('^clients_support/', include(router.urls)), )