from django.core.management.base import BaseCommand, CommandError
from rooms.models import Amenity

amenities = [
    'Kitchen',
    'Heating',
    'Washer',
    'Wifi',
    'Indoor fireplace',
    'Iron',
    'Laptop friendly workspace',
    'Crib',
    'Self Check-in',
    'Carbon monoxide detector',
    'Shampoo',
    'Air conditioning',
    'Dryer',
    'Breakfast',
    'Hangers',
    'Hair dryer',
    'TV',
    'High chair',
    'Smoke detector',
    'Private bathroom'
]


class Command(BaseCommand):
    help = "This command generate/ seed all Amenities"

    def handle(self, *args, **options):
        for amenity in amenities:
            try:
                found = Amenity.objects.get(name=amenity)
            except Amenity.DoesNotExist:
                found = None

            if not found:
                Amenity.objects.create(name=amenity)
            else:
                self.stdout.write(self.style.WARNING('Amenity "%s" already exist.' % amenity))
        self.stdout.write(self.style.SUCCESS('Amenities seeded'))
