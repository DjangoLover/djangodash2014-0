# coding=utf-8

from datetime import datetime, time, timedelta
from django import template

from clients_support.models import Ticket

register = template.Library()

date_params = lambda n, _date: {n+'__year': _date.year, n+'__month': _date.month, n+'__day': _date.day}


@register.inclusion_tag('clients_support/admin/block_with_statistics.html')
def block_with_statistics():
    today = datetime.now().today()
    queryset = Ticket.objects.all()

    return dict(
        closed_count=queryset.filter(status=Ticket.CLOSED_STATUS).count(),
        open_count=queryset.exclude(status__in=[Ticket.CLOSED_STATUS, Ticket.SOLVED_STATUS]).count(),
        total_count=queryset.count(),
        add_today_count=queryset.filter(**date_params('created_time', today)).count(),
        closed_today_count=queryset.filter(status=Ticket.CLOSED_STATUS, **date_params('closed_time', today)).count()
    )
