from django import template
from consulting.models import Consultant, PracticeArea

register = template.Library()


@register.assignment_tag
def consultants():
    return Consultant.published.only('name', 'slug')


@register.assignment_tag
def practiceareas():
    return PracticeArea.published.only('title', 'slug')