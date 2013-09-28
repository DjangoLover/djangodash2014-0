from django import template

register = template.Library()

@register.inclusion_tag('clients_support/block_with_statistics.html')
def block_with_statistics():
    return {}
