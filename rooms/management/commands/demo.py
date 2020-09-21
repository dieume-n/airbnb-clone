from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'This command tells DEMO'

    def add_arguments(self, parser):
        parser.add_argument(
            '--times',
            type=int,
            help="How many times do you want me to output DEMO?",
        )

    def handle(self, *args, **options):
        for t in range(0, options['times']):
            print("DEMO")
        self.stdout.write(self.style.SUCCESS('Command executed'))

