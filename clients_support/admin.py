# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext as _
from clients_support.conf import settings

from clients_support.models import Ticket, TicketType, StatusLog


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


class TicketForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['status'].choices = \
                self.instance.get_status_choices_specific([Ticket.REOPENED_STATUS]) if self.instance.is_solved else \
                self.instance.get_status_choices_unless([Ticket.SOLVED_STATUS, Ticket.REOPENED_STATUS])


class TicketAdmin(admin.ModelAdmin):

    form = TicketForm

    list_display = ('subject', 'user', 'manager', 'status', 'type', 'importance', 'updated_time')
    list_filter = ('tags', 'type', 'importance', 'status', 'created_time', AssignManagerFilter)
    search_fields = ('subject', 'text')
    actions = ['make_published', 'change_importance_to_high', 'change_importance_to_normal', 'change_importance_to_low',
               'change_status_to_read', 'change_status_to_solved']
    change_list_template = 'clients_support/admin/change_list.html'
    readonly_fields = ('created_time', 'closed_time')

    def has_add_permission(self, request):
        return settings.ADMIN_PERMISSION_ADD_TICKET

    def save_model(self, request, obj, form, change):
        obj.save()
        if 'status' in form.changed_data:
            StatusLog.add_log(obj, request.user, obj.status)

    def make_published(self, request, queryset):
        queryset.update(publish=True)
    make_published.short_description = _("Mark selected tickets as published")

    def change_importance_to_high(self, request, queryset):
        queryset.update(importance=Ticket.HIGH_IMPORTANT)
    change_importance_to_high.short_description = _("Change the importance of the selected tickets on a high")

    def change_importance_to_normal(self, request, queryset):
        queryset.update(importance=Ticket.NORMAL_IMPORTANT)
    change_importance_to_normal.short_description = _("Change the importance of the selected tickets on a normal")

    def change_importance_to_low(self, request, queryset):
        queryset.update(importance=Ticket.NOT_IMPORTANT)
    change_importance_to_low.short_description = _("Change the importance of the selected tickets on a low")

    def change_status_to_read(self, request, queryset):
        for ticket in queryset:
            if ticket.status != ticket.READ_STATUS:
                StatusLog.add_log(ticket, request.user, ticket.READ_STATUS)
        queryset.update(status=Ticket.READ_STATUS)
    change_status_to_read.short_description = _("Change the status of the selected tickets as read")

    def change_status_to_solved(self, request, queryset):
        for ticket in queryset:
            if ticket.status != ticket.SOLVED_STATUS:
                StatusLog.add_log(ticket, request.user, ticket.SOLVED_STATUS)
        queryset.update(status=Ticket.SOLVED_STATUS)
    change_status_to_solved.short_description = _("Change the status of the selected tickets as solved")


class StatusLogAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'user', 'status', 'created_time')
    list_filter = ('ticket', 'user', 'status', 'created_time')
    readonly_fields = ('ticket', 'user', 'status')
    ordering = ('-created_time',)

    def has_add_permission(self, request):
        return False


admin.site.register(Ticket, TicketAdmin)
admin.site.register(StatusLog, StatusLogAdmin)
admin.site.register(TicketType)