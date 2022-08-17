import csv

from django.core.management.base import BaseCommand, CommandError
from wedding.guests.models import Guest, Party


class Command(BaseCommand):
    help = 'Dump guest info as a CSV'

    def handle(self, *args, **options):
        with open('guests.csv', 'w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
            guest: Guest = None
            for guest in Guest.objects.order_by('party').all():
                party: Party = guest.party
                writer.writerow([
                    guest.name,
                    party.name,
                    guest.get_role_display(),
                    guest.get_meal_display(),
                    guest.requests,
                ])
