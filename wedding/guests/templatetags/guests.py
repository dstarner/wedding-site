from django import template
from django.db.models import Sum
from ..models import Party


register = template.Library()


@register.simple_tag
def num_guests():
    attending = Party.objects.aggregate(total=Sum('attending'))['total']
    allowed = Party.objects.aggregate(total=Sum('guests_allowed'))['total']
    return f'{attending} / {allowed}'
