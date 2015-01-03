from django import template
from consulting.models import Consultant, PracticeArea

register = template.Library()


@register.assignment_tag
def consultants():
    return Consultant.published.only('title', 'slug')


@register.assignment_tag
def practiceareas():
    return PracticeArea.published.only('title', 'slug')