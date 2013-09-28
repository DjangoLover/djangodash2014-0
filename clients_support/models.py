from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

class Ticket(models.Model):

    NEW_STATUS = 'new'
    READ_STATUS = 'read'
    ASSIGNED_STATUS = 'assigned'
    SOLVED_STATUS = 'solved'
    CLOSED_STATUS = 'closed'
    REOPENED_STATUS = 'reopened'

    STATUSES = (
        (NEW_STATUS, _('New ticket')),
        (READ_STATUS, _('Ticket was read')),
        (ASSIGNED_STATUS, _('Ticket was assigned')),
        (SOLVED_STATUS, _('Ticket was solved')),
        (CLOSED_STATUS, _('Ticket was closed')),
        (REOPENED_STATUS, _('Ticket was reopened'))
    )

    SATISFIED_MARK = 'satisfied'
    NOT_SATISFIED_MARK = 'not_satisfied'
    NOT_RATED_MARK = 'not_rated'

    MARKS = (
        (SATISFIED_MARK, _('User was satisfied')),
        (NOT_SATISFIED_MARK, _('User was not satisfied')),
        (NOT_RATED_MARK, _('User is not rated ticket'))
    )

    HIGH_IMPORTANT = 'high'
    NORMAL_IMPORTANT = 'normal'
    NOT_IMPORTANT = 'not'

    IMPORTANCE = (
        (HIGH_IMPORTANT, _('High importance')),
        (NORMAL_IMPORTANT, _('Normal importance')),
        (NOT_IMPORTANT, _('Not important'))
    )

    subject = models.CharField(max_length=255)
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    guest_name = models.CharField(max_length=255, blank=True, null=True)
    guest_email = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUSES)
    user_mark = models.CharField(max_length=15, choices=MARKS)
    type = models.ForeignKey(TicketType)
    importance = models.CharField(max_length=10, choices=IMPORTANCE)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    # Used to create a secret link (for guests)
    secret_code = models.URLField()
    # Publish a ticket to be seen by other users
    publish = models.BooleanField()
    viewed = models.BooleanField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    closed_time = models.DateTimeField(blank=True, null=True)


class Message(models.Model):
    ticket = models.ForeignKey(Ticket)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    # Sended from guest
    from_guest = models.BooleanField()
    text = models.TextField()
    # If a message is created by the client, then automatically placed in the True, otherwise False.
    was_read = models.BooleanField()
    created_time = models.DateTimeField(auto_now_add=True)


class TicketType(models.Model):
    name = models.CharField(max_length=255)


class Tag(models.Model):
    name = models.CharField(max_length=255)