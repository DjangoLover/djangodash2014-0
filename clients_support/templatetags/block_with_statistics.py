from django import template

register = template.Library()

@register.inclusion_tag('block_with_statistics.html')
def block_with_statistics(context):
    return {}
