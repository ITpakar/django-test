import datetime
from django import template
from datetime import date

register = template.Library()


@register.simple_tag
def get_eligibility(user):
    return user.get_eligibility()


@register.simple_tag
def get_bizzfuzz(user):
    return user.get_bizzfuzz()
