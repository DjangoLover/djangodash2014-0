# -*- coding: utf-8 -*-

from django.conf import settings as django_settings
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _


ADMIN_SHOW_BLOCK_STATISTICS = getattr(django_settings, 'SUPPORT_ADMIN_SHOW_BLOCK_STATISTICS', True)
