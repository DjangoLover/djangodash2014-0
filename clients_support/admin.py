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
    actions = ['make_published', 'change_importance_to_high', 'change_importance_to_normal', 'change_importance_to_low',
               'change_status_to_read', 'change_status_to_solved']
    change_list_template = 'clients_support/admin/change_list.html'
    readonly_fields = ('created_time',)

    def has_add_permission(self, request):
        return False

    def make_published(modeladmin, request, queryset):
        queryset.update(publish=True)
    make_published.short_description = _("Mark selected tickets as published")

    def change_importance_to_high(modeladmin, request, queryset):
        queryset.update(importance=Ticket.HIGH_IMPORTANT)
    change_importance_to_high.short_description = _("Change the importance of the selected tickets on a high")

    def change_importance_to_normal(modeladmin, request, queryset):
        queryset.update(importance=Ticket.NORMAL_IMPORTANT)
    change_importance_to_normal.short_description = _("Change the importance of the selected tickets on a normal")

    def change_importance_to_low(modeladmin, request, queryset):
        queryset.update(importance=Ticket.NOT_IMPORTANT)
    change_importance_to_low.short_description = _("Change the importance of the selected tickets on a low")

    def change_status_to_read(modeladmin, request, queryset):
        queryset.update(status=Ticket.READ_STATUS)
    change_status_to_read.short_description = _("Change the status of the selected tickets as read")

    def change_status_to_solved(modeladmin, request, queryset):
        queryset.update(status=Ticket.SOLVED_STATUS)
    change_status_to_solved.short_description = _("Change the status of the selected tickets as solved")


admin.site.register(Ticket, TicketAdmin)
admin.site.register(TicketType)