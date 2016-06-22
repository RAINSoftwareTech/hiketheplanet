from django.core.urlresolvers import reverse
from django import template

register = template.Library()


@register.simple_tag
def kwargs_url(url_name, view_kwargs):
    return reverse(url_name, kwargs=view_kwargs)
