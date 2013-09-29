# -*- coding: utf-8 -*-
import autocomplete_light
from clients_support.models import Tag


autocomplete_light.register(Tag, autocomplete_light.AutocompleteModelTemplate,
                            choice_template='clients_support/admin/tags_choice.html')