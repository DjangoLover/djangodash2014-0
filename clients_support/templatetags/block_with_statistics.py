# coding=utf-8

from datetime import datetime, time, timedelta
from django import template

from clients_support.models import Ticket

register = template.Library()


@register.inclusion_tag('clients_support/admin/block_with_statistics.html')
def block_with_statistics():
    today = datetime.now().date()
    tomorrow = today + timedelta(1)

    today = datetime.combine(today, time())
    tomorrow = datetime.combine(tomorrow, time())

    return {
        'closed_count': Ticket.objects.filter(status=Ticket.CLOSED_STATUS).count(),
        'open_count': Ticket.objects.exclude(status=Ticket.CLOSED_STATUS).exclude(status=Ticket.SOLVED_STATUS).count(),
        'total_count': Ticket.objects.all().count(),
        'add_today_count': Ticket.objects.filter(created_time__gte=today).filter(created_time__lte=tomorrow).count(),
        'closed_today_count': Ticket.objects.filter(closed_time__gte=today).filter(closed_time__lte=tomorrow).count()
    }
