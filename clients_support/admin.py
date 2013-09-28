from django.contrib import admin
from django.utils.translation import ugettext as _

from clients_support.models import Ticket, TicketType, Tag


class AssignManagerFilter(admin.SimpleListFilter):
    title = _('Only my tickets')

    parameter_name = 'assign_manager'

    def lookups(self, request, model_admin):
        return (
            ('yes', _('Yes')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(manager=request.user)
        return queryset


class TicketAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user', 'manager', 'status', 'type', 'importance', 'updated_time')
    list_filter = ('tags', 'type', 'importance', 'status', 'created_time', AssignManagerFilter)
    search_fields = ('subject', 'text')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(TicketType)