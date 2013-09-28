from django.contrib import admin

from clients_support.models import Ticket, TicketType, Tag


class TicketAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user', 'manager', 'status', 'type', 'importance', 'updated_time')
    list_filter = ('tags', 'type', 'importance', 'status', 'created_time')
    search_fields = ('subject', 'text')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(TicketType)