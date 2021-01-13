import decimal
import json

from django.conf import settings
from django.shortcuts import render

from wedding.guests.choices import Role
from wedding.guests.models import Guest
from .models import GalleryItem, PlaceOfInterest, RegistryOrganization, TimelineEntry


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(next(str(o) for o in [o]))
        return super(DecimalEncoder, self).default(o)


def index(request):
    best_man = Guest.objects.filter(role=Role.BEST_MAN).first()
    maid_of_honor = Guest.objects.filter(role=Role.MAID_OF_HONOR).first()
    groomsmen = Guest.objects.filter(role=Role.GROOMSMAN).all()
    maids = Guest.objects.filter(role=Role.BRIDESMAID).all()

    places = PlaceOfInterest.objects.all()

    return render(request, 'index.html', {
        'groomsmen': ([best_man] if best_man else []) + list(groomsmen),
        'maids': ([maid_of_honor] if maid_of_honor else []) + list(maids),
        'timeline_entries': TimelineEntry.objects.all(),
        'maps_key': settings.GOOGLE_API_KEY,
        'gallery': GalleryItem.objects.all(),
        'registry': RegistryOrganization.objects.all(),
        'places': places,
        'places_data': json.dumps([place.as_data() for place in places], cls=DecimalEncoder),
    })