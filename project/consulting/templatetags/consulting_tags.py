from django import template
from django.utils.safestring import mark_safe
from consulting.models import Consultant, PracticeArea

register = template.Library()


@register.assignment_tag
def consultants():
    """Returns list of consultants for use in navigation."""

    return Consultant.published.only('title', 'slug')


@register.assignment_tag
def practiceareas():
    """Returns list of practiceareas for use in navigation."""

    return PracticeArea.published.only('title', 'slug')

@register.filter
def keeptogether(value):
    return mark_safe(value.replace(" ", "&nbsp;"))