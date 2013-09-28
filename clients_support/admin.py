from django.contrib import admin

from clients_support.models import Ticket, TicketType, Tag


admin.site.register(Ticket)
admin.site.register(TicketType)
admin.site.register(Tag)