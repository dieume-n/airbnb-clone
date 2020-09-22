from django.core.management.base import BaseCommand
from rooms.models import Facility

facilities = [
    'Private entrance',
    'Paid parking on premises',
    'Paid parking off premises',
    'Elevator',
    'Parking',
    'Gym'
]


class Command(BaseCommand):
    help = "This command seed/ create all the facilities"

    def handle(self, *args, **options):
        for facility in facilities:
            try:
                found = Facility.objects.get(name=facility)
            except Facility.DoesNotExist:
                found = None
            if not found:
                Facility.objects.create(name=facility)
            else:
                self.stdout.write(self.style.WARNING('Facility "%s" already exist.' % facility))
        self.stdout.write(self.style.SUCCESS('Facilities seeded'))
